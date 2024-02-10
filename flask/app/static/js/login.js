
const login_f = document.getElementById("login-form");
login_f.addEventListener("submit", (e)=>{
    e.preventDefault();

    const form_object = {
        email: e.target.email.value,
        password: e.target.password.value
    };
    clearErr();
    const form_checked = formValidate(form_object);
    if (form_checked[0]) {
        // not pass
        errHandle(form_checked[1]);
    } else {
        // pass
        onLogin(form_object);
    }
});

async function onLogin(body) {
    const res = await fetch("/api/login", body);
    const result = await res.json();
    if (res.status===400) {
        let err_message = {}
        result.err.forEach(err_code=>{
            if (err_code==="EMAIL_NFOUND") {
                err_message["email"] = "Not found this email."
            } else if (err_code==="PASS_WRONG") {
                err_message["password"] = "Password's not correct."
            }
        });
        errHandle(err_message);
    } else if (res.status===200) {
        const token = result.data.token;
        sessionStorage.setItem("token", token);
        window.location.reload()
    }
}

// function for validate form
function formValidate(data) {
    let have_err = false;
    let err_message = {};
    
    // email check
    if (!data.email || data.email.split("@").length!==2 || !data.email.split("@")[1].includes(".") || data.email[data.email.length-1]==".") {
        have_err = true;
        err_message["email"] = "email's invalid.";
    }
    // password check
    if (!data.password || data.password.length < 8 || data.password.length > 20) {
        have_err = true;
        err_message["password"] = "password must be in range 8-20 charactors";
    }

    return [have_err, err_message];
}

// function for err show
function errHandle(data) {
    for (const key in data) {
        console.log(key);
        const element = document.getElementById(key);

        // console.log(element.children);
        const input = element.children[1];
        const err_message = document.createElement("p");
        err_message.classList.add("err_text");
        err_message.innerHTML = data[key];
        input.classList.add("err");
        element.appendChild(err_message);
    }
}

// function for clear err
function clearErr() {
    const err_text_tags = document.getElementsByClassName("err_text");
    for (const err_text_tag of err_text_tags) {
        err_text_tag.parentNode.removeChild(err_text_tag);
    }

    const err_ps = document.getElementsByClassName("err");
    for (const err_p of err_ps) {
        err_p.classList.remove("err");
    }
    
}