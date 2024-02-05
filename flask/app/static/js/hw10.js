async function getData() {
    const response = await fetch("/hw10/blog");
    const result = await response.json();
    return result;
}

function clearErr() {
    let err_tag = document.getElementById("err_tag");
    while (err_tag) {
        err_tag.remove();
        err_tag = document.getElementById("err_tag");
    }
}

function formValidate(form_data) {
    let have_err = false;
    let err = {};
    if (form_data.name.length > 50) {
        have_err = true;
        err.name = "Name must less than 51 charactors.";
    }
    if (form_data.email.length > 50) {
        have_err = true;
        err.email = "Email must less than 51 charactors.";
    } else if (
        form_data.email.split("").filter(char=>char==="@").length!==1
        || form_data.email.split("@")[1].split(".").filter(char=>char.length>0).length === 1
    ) {
        have_err = true;
        err.email = "Email's wrong format.";
    }
    if (form_data.message.length > 280) {
        have_err = true;
        err.message = "Message must less than 281 charactors.";
    }
    return [have_err, err];
}

function errHandle(key, value) {
    const tag_to_add = document.getElementById(`${key}_f`);
    const err_tag = document.createElement("p");
    err_tag.id = "err_tag";
    err_tag.className = "err";
    err_tag.innerHTML = value;
    tag_to_add.append(err_tag);
}

function onEdit(id, name, email, message) {
    const form_ = document.getElementById("post-form");
    form_[0].value=name;
    form_[1].value=email;
    form_[2].value=message;
    form_[3].value=id;
}

function onDelete(id) {
    const form_data = new FormData();
    form_data.append("id", id);
    
    fetch("/hw10/blog", {
        method: "DELETE",
        body: form_data
    }).then(response=>{
        updateBlogs();
    });
}

function padZero(numb, length) {
    return String(numb).padStart(length, "0");
}

function createBlog(id, name, email, message, create_time, update_time) {
    const create_date = new Date(`${create_time} UTC`);
    const update_date = new Date(`${update_time} UTC`);
    
    return `<div class="tweet">
    <div class="row">
        <div class="col-md-2 text-center">
            <img class="tw-user-medium rounded-circle" src="static/img/user-icon.png">
        </div>
        <div class="col-md-10">
            <div class="row tweet-info">
                <div class="col-md-auto">
                    <span class="tweet-username">${name}</span>
                    <span class="tweet-usertag text-muted">${email}</span>-
                    <span class="tweet-age text-muted" style="font-size: 0.65rem">${padZero(create_date.getDate(), 2)}/${padZero(create_date.getMonth()+1, 2)}/${create_date.getFullYear()%100} - ${padZero(create_date.getHours(), 2)}:${padZero(create_date.getMinutes(), 2)}</span>
                </div>
            </div>
            <div class="tweet-text content-message">
                ${message}
            </div>
            ${create_date.valueOf()!==update_date.valueOf() ?
            `<div class="edit-text">
                Last Edit : ${padZero(update_date.getDate(), 2)}/${padZero(update_date.getMonth()+1, 2)}/${update_date.getFullYear()%100} - ${padZero(update_date.getHours(), 2)}:${padZero(update_date.getMinutes(), 2)}
            </div>` : ""}
            <div class="row text-muted btn-post">
                <div class="col-md-2"><span class="oi oi-bullhorn"></span></div>
                <div class="col-md-2"><span class="oi oi-loop-circular"></span></div>
                <div class="col-md-2"><span class="oi oi-heart"></span></div>
                <div class="col-md-2"><span class="oi oi-envelope-open"></span></div>
                <div class="col-md-2"><span class="oi oi-pencil" onclick="onEdit('${id}', '${name}', '${email}', '${message}')"></span></div>
                <div class="col-md-2"><span class="oi oi-trash" onclick="onDelete('${id}')"></span></div>
            </div>
        </div>
    </div>
</div>`
}

async function updateBlogs() {
    const main_feed = document.getElementById("feed");
    while (main_feed.children.length>1) {
        main_feed.removeChild(main_feed.lastChild);
    }

    const data = await getData();
    data.forEach(val=>{
        main_feed.innerHTML += createBlog(val.id, val.name, val.email, val.message, val.date_created, val.date_updated);
    });
}

async function sendData(data) {
    const form_data = new FormData();
    for (const key in data) {
        form_data.append(key, data[key]);
    }

    const response = await fetch(
        "/hw10/blog", 
        {
            method: "POST",
            body: form_data
        }
    );
    
    return {status: response.status, data: response.status===200 ? "OK" : await response.json()};
}

function formSubmit(form) {
    clearErr();

    let data = {
        name: form[0].value,
        email: form[1].value,
        message: form[2].value
    }
    if (form[3].value!=="-1") {
        data["id"] = Number(form[3].value);
    }

    const validated = formValidate(data);

    if (validated[0]) {
        for (const key in validated[1]) {
            errHandle(key, validated[1][key])
        }
    } else {
        sendData(data).then((val)=>{
            updateBlogs();
        });
    }
    return false;
}

document.addEventListener("DOMContentLoaded", () => {
    updateBlogs();
});