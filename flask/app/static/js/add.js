// Switch Page

const tag_field = document.getElementById("tag-field");

class MyData {

    constructor() {
        this.currentPage = "prop";
        this.tags = []; // { id: number, tag: string, dbid: number # 0 is to insert } 
        this.db_tags = [];
        this.getDBtagFromServer();
    }

    async getDBtagFromServer() {
        const response = await fetch("/api/tag", {method: "GET"});
        const result = await response.json();
        this.db_tags = result.data.map(val=>{return {id: val.id, name: val.name};});
    }

    getDBtag() {
        return this.db_tags;
    }

    getPage() {
        return this.currentPage;
    }

    togglePage() {
        if (this.currentPage==="prop") {
            this.currentPage="card";
        } else {
            this.currentPage="prop";
        }
    }

    getTags() {
        return this.tags;
    }
    
    removeTag(id) {
        this.tags = this.tags.filter(val=>val.id!==id);
    }

    addTag(name, dbid=0) {
        let id = 0;
        if (this.tags.length!==0) {
            id = this.tags[this.tags.length-1].id + 1;
        }
        const tag_tag = document.createElement("div");
        tag_tag.append(document.createTextNode(name));
        const delete_tag = document.createElement("div");
        delete_tag.classList.add("x");
        delete_tag.addEventListener("click", (e)=>{
            this.tags.filter(val=>{
                if (val.id===id) {
                    val.element.remove();
                    return false;
                }
                return true;
            });
        });
        delete_tag.innerHTML = "<div></div><div></div>";
        tag_tag.append(delete_tag);
        tag_field.append(tag_tag);
        this.tags.push({ id, tag: name, dbid, element: tag_tag });
    }

}

const my_state = new MyData();

const prop_btn = document.getElementById("prop-btn");
const card_btn = document.getElementById("card-btn");
const bg_btn = document.getElementById("bg-btn");
const prop_form = document.getElementById("prop-form");
const card_mng = document.getElementById("card-mng");

function onChangePage(page) {
    if (page!==my_state.getPage()) {
        my_state.togglePage();
        if (page==="card") {
            bg_btn.classList.add("switch");
            card_btn.classList.add("activate");
            prop_btn.classList.remove("activate");
            prop_form.classList.remove("activate");
            card_mng.classList.add("activate");
        } else {
            bg_btn.classList.remove("switch");
            prop_btn.classList.add("activate");
            card_btn.classList.remove("activate");
            card_mng.classList.remove("activate");
            prop_form.classList.add("activate");
        }
    }
}

// toggle status

const status_toggle = document.getElementById("status-toggle");
const status_input = document.getElementById("status");

function onStatusToggle() {
    const private_toggle = document.getElementById("private-toggle");
    const public_toggle = document.getElementById("public-toggle");
    const current = status_input.value;
    const circle = status_toggle.getElementsByClassName("circle");
    if (current==="private") {
        status_input.value = "public"
        circle[0].classList.add("switch");
        private_toggle.classList.remove("activate");
        public_toggle.classList.add("activate");
        status_toggle.classList.add("activate");
    } else {
        status_input.value = "private"
        circle[0].classList.remove("switch");
        public_toggle.classList.remove("activate");
        private_toggle.classList.add("activate");
        status_toggle.classList.remove("activate");
    }
}

// Add
const form_add = document.getElementById("card-form");

function onAdd() {
    let number_input = 0;
    onChangePage("card");
    if (form_add.lastElementChild) {
        const last_number = parseInt(form_add.lastElementChild.getAttribute("order_"));
        if (!isNaN(last_number)) {
            number_input = last_number+1;
        }
    }
    const tag = `<div class="card-form-grp" order_="${number_input}">
        <input style="grid-area: in1;" id="question${number_input}" name="question${number_input}" type="text" placeholder="Question...">
        <input style="grid-area: in2;" id="answer${number_input}" name="answer${number_input}" type="text" placeholder="Answer...">
        <button style="grid-area: btn1;" type="button" onclick="onSuggestClick(this);">Sug</button>
        <button style="grid-area: btn2;" type="button" onclick="onRemoveClick(this);">-</button>
        <input type="text" name="is_recom${number_input}" value="f" hidden>
        <input type="text" name="own_recom${number_input}" value="f" hidden>
        <input type="text" name="edit_origin${number_input}" value="f" hidden>
        <input type="text" name="ref${number_input}" value="0" hidden>
    </div>`
    form_add.innerHTML+=tag;
}


function onRemoveClick(element) {
    const parent = element.parentElement;
    if (parent) {
        parent.remove();
    }
}

function onSuggestClick(element) {
    console.log("Hello");
}

// tag inclease

const tag_input = document.getElementById("tag-insert");
const rec_tab = document.getElementById("tag-recm");

function onSearchTag(word) {
    const word_length = word.length;
    const db_tags = my_state.getDBtag();
    let result = [];
    for (const val of db_tags) {
        if (val.name.slice(0, word_length)===word) {
            result.push(val);
            if (result.length===3) {
                return result;
            }
        }
    }
    return result;
}

function deleteAllChildren(element) {
    while (element.firstChild) {
        element.removeChild(element.lastChildren);
    }
}

tag_input.addEventListener("input", (e)=>{
    // deleteAllChildren(rec_tab);
    rec_tab.replaceChildren()
    if (e.target.value.length > 0) {
        onSearchTag(e.target.value).forEach(element => {
            const li_tag = document.createElement("li");
            li_tag.addEventListener("click", (e)=>{
                my_state.addTag(element.name, element.id);
                tag_input.value = "";
                rec_tab.replaceChildren();
            });
            li_tag.innerHTML = element.name;
            rec_tab.append(li_tag);
        });
    }
});

const tag_form = document.getElementById("tag-form");
tag_form.addEventListener("submit", (e)=>{
    e.preventDefault();
    my_state.addTag(tag_input.value, 0);
});

// footer