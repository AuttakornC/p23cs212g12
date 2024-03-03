//write by Mesanee Laihueang 650510676


$(document).ready(function () {
    function add() {
        $.get("api/explore/all/decks", (decks)=>{
            // console.log("decks:", decks[0]["name"])
            $.each(decks, (key, value) =>{
                // console.log(value)    
                addDataDecks(value)
            })
        });
    }
    add();
});


function addDataDecks(decks){
    // console.log(decks.avatar_url)
    let tagHtml = '';
    for (let i in decks.tags) {
        tagHtml += `<span class="tag">#${decks.tags[i]}</span><nobr></nobr>`;
    }
    const post_block = `<div class="box" onclick="onPreview(this)" dataDecks='${JSON.stringify(decks)}';>
    <div class="profile">
        <img class="profile-icon" src="${decks.avatar_url}" alt="">
        <span class="people">${decks.player_name}</span>
    </div>
    <div class="description"><h4 class="deckName">${decks.name}</h4><h5 class="cardNum">${decks.num_card} Cards</h5></div>
    <span class="tags">${tagHtml}</span> 
    </div>`;
    $(".container").html($(".container").html()+post_block);
}



function onPreview(data) {
    const decks = JSON.parse(data.getAttribute('dataDecks'));
    const cards = decks.cards

    //clear หน้า preview ส่วน head
    $(".header").html("")
    //clear หน้า preview ส่วน word
    $("#sug-own").html("")


    addPreview(decks)

    // console.log("decks:", decks)
    for (const key in cards){
        // console.log(key, cards[key])
        addWordPreview(key, cards[key])
    }

    $('#preview').show();
    $('.box').hide();
}

function onClose() {
    $('#preview').hide();
    $('.box').show();
}

function addPreview(decks) {
    const head = `<h1>${decks.name}<div id="sug-close" class="x" onclick="onClose()"><div></div><div></div></div></h1>
    <h4>${decks.num_card} Cards</h4> `;
    $(".header").html($(".header").html() + head)
}

function addWordPreview(question, answer) {
    const word = `<tr><th>${question}</th><th>${answer}</th></tr>
    <hr>`;
    $("#sug-own").html($("#sug-own").html()+word)
}


function searchInput(word) {
    $.get("api/explore/all/decks", (decks)=>{
        //console.log(decks[0].name)
        $(".container").html("")
        if (word.length!==0) {
            word = word.toLowerCase();
            const word_len = word.length;
            $.each(decks, (key, value) =>{
                
                // value["name"].forEach(name=>{
                const name = value.name.toLowerCase();
                console.log(name) 
                if (name.length < word_len) {
                    
                } else if (name.slice(0, word_len)!==word) {
                    
                } else {
                    addDataDecks(value)
                }

                $.each(value.tags, (k, v) =>{
                    const tag = v.toLowerCase();
                    if (tag.length < word_len) {
                    
                    } else if (tag.slice(0, word_len)!==word) {
                        
                    } else {
                        addDataDecks(value)
                    }
                });
            })
        } else {
            $.each(decks, (key, value) =>{
                addDataDecks(value);
            })
            
        }
    });
    
}


const search_icon = document.getElementById("search-icon");
const search_form = document.getElementById("formSearch");
const search_input = document.getElementById("search-input");

search_icon.addEventListener("click", (e)=>{
    searchInput(search_input.value);
});

search_form.addEventListener("submit", (e)=>{
    e.preventDefault();
    searchInput(search_input.value); // Use search_input.value to access the input value
});

