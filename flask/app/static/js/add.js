// Switch Page

class MyData {

    constructor() {
        this.currentPage = "prop";
        this.tags = []; // { id: number, tag: string, dbid: number # 0 is to insert } 
        this.db_tags = [];
        this.getDBtag()
    }

    async getDBtag() {
        const response = await fetch("/api/tag")
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

    addTag(name) {
        let id = 0;
        if (this.tags.length!==0) {
            id = this.tags[this.tags.length-1].id+1;
        }
        this.tags.push({ id: id, tag: name });
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
    
}

tag_input.addEventListener("change", (e)=>{
    if (e.target.value.length > 0) {
        
    }
});

// footer