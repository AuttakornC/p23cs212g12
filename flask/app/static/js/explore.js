$(document).ready(function () {
    (function () {
        $.get("api/explore/all/decks", (decks)=>{
            //console.log(decks[0].name)
            $.each(decks, (key, value) =>{
                console.log(value)    
                addDataDecks(value)
            })
            
            
        });
    })();
});

function addDataDecks(decks){
    //console.log(decks["name"]);
    //document.getElementsByClassName("deckName").innerHTML = decks["name"].innerHTML;
   //console.log(document.getElementsByClassName("deckName").innerHTML)
   const post_block = `<div class="box" onclick="onSuggestClick(this);>
    <div class="profile">
        <img class="profile-icon" src="/static/image/profile-icon.png" alt="">
        <span class="people">${decks.player_name}</span>
    </div>
    <div class="description"><h4 class="deckName">${decks.name}</h4><h5 class="cardNum">${decks.num_card} Cards</h5></div>
    <div></div>
    </div>`;
    $(".container").html($(".container").html()+post_block);
}

function onSuggestClick(element) {
        // console.log(element.parentElement.children[0].value);
        if (element.parentElement.children[0].value) {
            preview.onpreview(element, element.parentElement.children[0].value);
        }
}

class preview {
    sug_close = document.getElementById("sug-close");
    sug_window = document.getElementById("preview");

    sug_own = document.getElementById("sug-own");

    constructor() {
        this.sug_close.addEventListener("click", (e)=>{
            this.sug_window.style.display = "none";
            this.clearList();
        });
    }

    clearList() {
        document.getElementById("sug-own").replaceChildren([]);
        // document.getElementById("sug-dict").replaceChildren([]);
        // document.getElementById("sug-other").replaceChildren([]);
        
    }


    onpreview(element_btn, word) {
        const element = element_btn.parentElement;
        const sug_own = document.getElementById("sug-own");
        // const sug_other = document.getElementById("sug-other");
        // const sug_dict = document.getElementById("sug-dict");
        const sug_window = document.getElementById("preview");

        function changeBTN() {
            element_btn.innerHTML = "Edit";
            element_btn.setAttribute("onclick", "onEdit(this);");
        }

        const clear_list = this.clearList;

        function checkRefRepeat(id_) {
            for (const input_data of my_state.getInputTag()) {
                if (input_data.element.children[2].value==="t" && parseInt(input_data.element.children[5].value)===id_) {
                    return false;
                }
            }
            return true;
        }

        async function getpreview() {    
            const response = await fetch(`/api/explore/all/decks?search=${decks}`);
            console.log(decks)
            const result = await response.json();
            result.data.owner.forEach(decks=>{
                sug_own.innerHTML += `<li><b>${decks.card.question}</b><b>${decks.card.answer}</b></li>`;
                sug_own.lastChild.addEventListener("click", (e)=>{
                    if (checkRefRepeat(val.id)) {
                        element.children[0].value = val.question;
                        element.children[0].disabled = true;
                        element.children[1].value = val.answer;
                        element.children[1].disabled = true;
                        element.children[2].value = 't';
                        element.children[3].value = 't';
                        element.children[5].value = val.id;
                        sug_window.style.display = "none";
                        changeBTN();
                        clear_list();
                    } else {
                        confirm_.open(
                            "Repeat Alert!!",
                            "There're some repeat previewion. The system'll not add this card to the deck. Please create new card or edit that preview card."
                        );
                    }
                });
            });

        }

        
        this.sug_window.style.display = "flex";
        getpreview();
    }

}


const suggest = new Suggest()