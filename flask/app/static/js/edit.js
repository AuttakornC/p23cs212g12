// set data

class DataManage {
    title = document.getElementById("title");
    tag_field = document.getElementById("tag-field");
    tags = [];
    input_tags = [];
    old_data = {}
    db_tags = [];

    constructor(deck_data) {
        this.old_data = deck_data;
        this.title.value = deck_data.name;
        deck_data.tags.forEach(tag_data => {
            console.log(tag_data)
            this.addTag(tag_data["name"], tag_data["id"]);
        });
        this.getDBtagFromServer();
    }

    async getDBtagFromServer() {
        const response = await fetch("/api/tag", {method: "GET"});
        const result = await response.json();
        this.db_tags = result.data.map(val=>{return {id: val.id, name: val.name};});
    }

    getTags() {
        return this.tags;
    }
 
    getDBtag() {
        return this.db_tags;
    }

    removeTag(id) {
        this.tags = this.tags.filter(val=>val.id!==id);
    }

    addTag(name, dbid=0) {
        if (!name) {
            return;
        }
        let id = 0;
        if (this.tags.length!==0) {
            id = this.tags[this.tags.length-1].id + 1;
        }
        let already_have = false;
        for (const tag of this.tags) {
            if (tag.tag.toLowerCase()===name || tag.dbid===dbid) {
                already_have = true;
                break;
            }
        }
        if (already_have) {
            confirm_.open("This tag is already there.", "The tag you mentioned is already present in the field. Could you please consider adding a different name tag?")
            return;
        }
        const tag_tag = document.createElement("div");
        tag_tag.append(document.createTextNode(name));
        const delete_tag = document.createElement("div");
        delete_tag.classList.add("x");
        delete_tag.addEventListener("click", (e)=>{
            this.tags = this.tags.filter(val=>{
                if (val.id===id) {
                    val.element.remove();
                    return false;
                }
                return true;
            });
        });
        delete_tag.innerHTML = "<div></div><div></div>";
        tag_tag.append(delete_tag);
        this.tag_field.append(tag_tag);
        this.tags.push({ id, tag: name, dbid, element: tag_tag });
    }

    createInputTag() {
        const tag = `<div class="card-form-grp" order_="${number_input}">
            <input style="grid-area: in1;" id="question${number_input}" name="question${number_input}" type="text" placeholder="Question...">
            <input style="grid-area: in2;" id="answer${number_input}" name="answer${number_input}" type="text" placeholder="Answer...">
            <input type="text" name="is_recom${number_input}" value="f" hidden>
            <input type="text" name="own_recom${number_input}" value="f" hidden>
            <input type="text" name="edit_origin${number_input}" value="t" hidden>
            <input type="text" name="ref${number_input}" value="0" hidden>
            <button style="grid-area: btn1;" type="button" onclick="onSuggestClick(this);">Sug</button>
            <button style="grid-area: btn2;" type="button" onclick="onRemoveClick(this);">-</button>
        </div>`
    }
}

const datamng = new DataManage(deck_data);

const tag_input = document.getElementById("tag-insert");
const rec_tab = document.getElementById("tag-recm");

function onSearchTag(word) {
    const word_length = word.length;
    const db_tags = datamng.getDBtag();
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
                datamng.addTag(element.name, element.id);
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
    datamng.addTag(tag_input.value, 0);
    rec_tab.replaceChildren();
    tag_input.value = "";
});