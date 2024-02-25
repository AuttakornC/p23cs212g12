// Switch Page

const tag_field = document.getElementById("tag-field");

class MyData {

    constructor() {
        this.currentPage = "prop";
        this.tags = []; // { id: number, tag: string, dbid: number # 0 is to insert } 
        this.db_tags = [];
        this.getDBtagFromServer();
        this.input_tag = []; // { order_id: number, element: element }
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

    addInputTag(order_id, node) {
        this.input_tag.push({ order_id, element: node });
    }

    removeInputTag(order_id) {
        this.input_tag = this.input_tag.filter((val)=>{
            if (order_id===val.order_id) {
                val.element.remove();
                return false;
            }
            return true;
        });
    }

    searchInput(word) {
        tag_field.ch
        if (word.length!==0) {
            word = word.toLowerCase();
            const word_len = word.length;
            this.input_tag.forEach(val=>{
                const qus = val.element.children[0].value.toLowerCase();
                const ans = val.element.children[1].value.toLowerCase();
                if (qus.length < word_len && ans.length < word_len) {
                    val.element.style.display = "none";
                } else if (qus.slice(0, word_len)!==word && ans.slice(0, word_len)!==word) {
                    val.element.style.display = "none";
                } else {
                    val.element.style.display = "grid";
                }
            });
        } else {
            this.clearSearch()
        }
    }

    clearSearch() {
        this.input_tag.forEach(val=>{
            val.element.style.display = "grid";
        });
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

function createElementFromStr(string) {
    const div = document.createElement("div");
    div.innerHTML = string.trim();
    return div.firstChild;
}

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
        <input type="text" name="is_recom${number_input}" value="f" hidden>
        <input type="text" name="own_recom${number_input}" value="f" hidden>
        <input type="text" name="edit_origin${number_input}" value="f" hidden>
        <input type="text" name="ref${number_input}" value="0" hidden>
        <button style="grid-area: btn1;" type="button" onclick="onSuggestClick(this);">Sug</button>
        <button style="grid-area: btn2;" type="button" onclick="onRemoveClick(this);">-</button>
    </div>`
    const node = createElementFromStr(tag);
    my_state.addInputTag(number_input, node);
    form_add.append(node);
}


function onRemoveClick(element) {
    const parent = element.parentElement;
    const order_id = parseInt(parent.getAttribute("order_"));
    my_state.removeInputTag(order_id);
}

function onSuggestClick(element) {
    // console.log(element.parentElement.children[0].value);
    if (element.parentElement.children[0].value) {
        suggest.onSuggest(element.parentElement, element.parentElement.children[0].value);
    }
}

const search_btn = document.getElementById("search-btn");
const search_form = document.getElementById("search");
const search_input = document.getElementById("search-input");

search_btn.addEventListener("click", (e)=>{
    console.log(search_input.value);
    my_state.searchInput(search_input.value);
});

search_form.addEventListener("submit", (e)=>{
    e.preventDefault();
    
    my_state.searchInput(e.target.search_input.value);
});

// tag inclease

const tag_input = document.getElementById("tag-insert");
const rec_tab = document.getElementById("tag-recm");

function onSearchTag(word) {
    const word_length = word.length;
    const db_tags = my_state.getDBtag();
    let result = [];
    for (const val of db_tags) {
        if (val.name.toLowerCase().slice(0, word_length)===word.toLowerCase()) {
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

// suggest

class Suggest {
    sug_close = document.getElementById("sug-close");
    sug_window = document.getElementById("suggest");

    sug_own = document.getElementById("sug-own");
    sug_dict = document.getElementById("sug-dict");
    sug_other = document.getElementById("sug-other");

    sug_nav_own = document.getElementById("sug-nav-own");
    sug_nav_dict = document.getElementById("sug-nav-dict");
    sug_nav_other = document.getElementById("sug-nav-other");
    sug_nav_bg = document.getElementById("sug-nav-bg");

    constructor() {
        this.sug_close.addEventListener("click", (e)=>{
            this.sug_window.style.display = "none"
            this.sug_own.replaceChild()
            this.sug_dict.replaceChild()
            this.sug_other.replaceChild()
        });

        this.sug_nav_own.addEventListener("click", (e)=>{
            this.sug_own.style.display = "block";
            this.sug_dict.style.display = "none";
            this.sug_other.style.display = "none";
            this.sug_nav_bg.style.left = "0";
            this.sug_nav_own.classList.add("activate");
            this.sug_nav_dict.classList.remove("activate");
            this.sug_nav_other.classList.remove("activate");
        });

        this.sug_nav_dict.addEventListener("click", (e)=>{
            this.sug_own.style.display = "none";
            this.sug_dict.style.display = "block";
            this.sug_other.style.display = "none";
            this.sug_nav_bg.style.left = "33.33%";
            this.sug_nav_own.classList.remove("activate");
            this.sug_nav_dict.classList.add("activate");
            this.sug_nav_other.classList.remove("activate");
        });

        this.sug_nav_other.addEventListener("click", (e)=>{
            this.sug_own.style.display = "none";
            this.sug_dict.style.display = "none";
            this.sug_other.style.display = "block";
            this.sug_nav_bg.style.left = "66.66%";
            this.sug_nav_own.classList.remove("activate");
            this.sug_nav_dict.classList.remove("activate");
            this.sug_nav_other.classList.add("activate");
        });
    }

    onSuggest(element, word) {
        const sug_own = document.getElementById("sug-own");
        const sug_other = document.getElementById("sug-other");
        const sug_dict = document.getElementById("sug-dict");
        const sug_window = document.getElementById("suggest");

        async function getSuggest() {    
            const response = await fetch(`/api/suggest?search=${word}`);
            const result = await response.json();
            result.data.owner.forEach(val=>{
                sug_own.innerHTML += `<li><b>${val.question}</b><b>${val.answer}</b></li>`;
                sug_own.lastChild.addEventListener("click", (e)=>{
                    element.children[0].value = val.question;
                    element.children[0].disabled = true;
                    element.children[1].value = val.answer;
                    element.children[1].disabled = true;
                    element.children[2].value = 't';
                    element.children[3].value = 't';
                    element.children[4].value = val.id;
                    sug_window.style.display = "none";
                });
            });

            result.data.other.forEach(val=>{
                sug_own.innerHTML += `<li><b>${val.question}</b><b>${val.answer}</b></li>`;
                sug_own.lastChild.addEventListener("click", (e)=>{
                    element.children[0].value = val.question;
                    element.children[0].disabled = true;
                    element.children[1].value = val.answer;
                    element.children[1].disabled = true;
                    element.children[2].value = 't';
                    element.children[3].value = 'f';
                    element.children[4].value = val.id;
                    sug_window.style.display = "none";
                });
            });
        }

        this.sug_window.style.display = "grid";
        getSuggest();
    }

}

const suggest = new Suggest()


// footer