// write by Rachata 650510638
class Deck {
    constructor() {
        /* deck_lst schema:
        [
            {
                player_id: 1,
                id: 1, 
                name: "animal",
                is_public: true,
                is_deleted: false,
                deleted_at: datetime(2024, 2, 12)
                element: <div>
            }, 
            {}, {}, ...
        ]
        */
        this.deck_lst = [];
        try {
            this.getDeck();
        } catch(error) {
            load.toggle();
        }
    }
    // Rachata create function for generate deck from database 
    async getDeck() {
        load.toggle();
        const respond = await fetch("/api/deck");
        const data = await respond.json();
        // console.log(data);
        const deckContainner = document.getElementsByClassName('deck-bg');
        deckContainner[0].innerHTML = ``
        data["data"].forEach(element => {
            // console.log(element);
            /*
            { avatar_url: "https://ui-avatars.com/api/?name=d+i&background=f6d394&color=725c3a",
             create_at: "2024-02-29 21:11:33", delete_at: null,
            id: 3, is_deleted: false, is_public: false, len_card: 1, 
            name: "ta", player_id: 3, username: "Didi" }
            */
            deckContainner[0].innerHTML += `
            <div class="box">
                <div class="deck-popup"></div>
                <div class="profile">
                    <img class="profile-icon" src="/static/image/profile-icon.png" alt="">
                    <span class="people">${element.username}</span>
                </div>
                <div class="description">
                    <h4 id="nameD" class="deckName">${element.name}</h4>
                    <span class="cardNum"><h5>${element.len_card} Cards</h5></span>
                </div>
                <div class="window-size">
                    <button onclick="onChange('/edit/${element.id}');" type="button">
                        <div class='icon-img edit'></div>
                    </button>
                    <button onclick="onChange('/play/${element.id}');" type="button">
                        <div class='icon-img play'></div>
                    </button>
                    <button onclick="handler.onDelete(${element.id})" type="button">
                        <div class='icon-img delete'></div>
                    </button>
                </div>
                
            </div>`
            
            
        });
        // add event to deck
        let decks = $('.deck-popup');
        decks.each(function(index, ele) {
            $(ele).click(function() {
                let deckName = $(this).siblings(".description").find(".deckName").text();
                popup(deckName);
            })
        })
        
        load.toggle();
    }

    // delete deck
    onDelete(id) {
        
        async function del(append) {
                load.toggle();
            try {
                await fetch(`api/deck?id=${id}`, {
                    method: "DELETE",
                    
                });
                append();  
            } catch {}

            load.toggle()
        } 
        confirm_.open("Warning", "Are you sure to delete?", () => {
            del(this.getDeck)
        })
    }
    
}
const handler = new Deck();

// redirect function
function onChange(redirectUrl)
{
    // const redirectUrl = '/create_deck';
    window.location.href = redirectUrl;
}

//  popup option deck
function popup(deckName) {
    if (deckName == '') {
        $('.header > h1').html('Unknow');
    } else {
        $('.header > h1').html(deckName);
    }
    
    $('#deck-menu').css("display", "flex");
}

// close popup option deck
function onClose() {
    $('#deck-menu').css("display", "none");
}

// edit home html to this >>
// 
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

// search deck
async function searchInput(word) {
    const respond = await fetch("/api/deck");
    const raw_data = await respond.json();
    const decks = raw_data['data'];
    decks.forEach(function(index, ele) {
        // log deck to check data --------1---------
        if (word.length!==0) {
            word = word.toLowerCase();
            const word_len = word.length;
            $.each(decks, (key, value) =>{
                
                // value["name"].forEach(name=>{
                const name = value.name.toLowerCase();
                // console.log(name) 
                // -----2------ check addDataDecks
                if (name.length < word_len) {
                    
                } else if (name.slice(0, word_len)!==word) {
                    
                } else {
                    addDataDecks(value)
                }
                // ------3------- check 'value' 
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
    })
    // $.get("api/decks", (decks)=>{
    //     console.log(decks[0])
        
    // });
    
}

const search_icon = document.getElementById("search-btn");
const search_form = document.getElementById("search-form");
const search_input = document.getElementById("search-input");

search_icon.addEventListener("click", (e)=>{
    searchInput(search_input.value);
});

search_form.addEventListener("submit", (e)=>{
    e.preventDefault();
    searchInput(search_input.value); // Use search_input.value to access the input value
});