// Rachata
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
                <div class="profile">
                    <img class="profile-icon" src="/static/image/profile-icon.png" alt="">
                    <span class="people"><h3>${element.username}</h3></span>
                </div>
                <div class="description">
                    <h3 id="nameD" class="deckName">${element.name}</h3>
                    <span class="cardNum">${element.len_card} Cards</span>
                </div>
                <div class="window-size">
                    <button id='edit' onclick="onChange('/edit/${element.id}');" type="button">
                        <img class="btn" src="/static/image/profile-icon.png" alt="">
                    </button>
                    <button id='play' onclick="onChange('/play/${element.id}');" type="button">
                        <img class="btn" src="/static/image/profile-icon.png" alt="">
                    </button>
                    <button id='delete' onclick="delete();" type="button">
                        <img class="btn" src="/static/image/profile-icon.png" alt="">
                    </button>
                </div>
                
            </div>`
            
            
        });
        // add event to deck
        let decks = $('.box');
        // console.log(decks);
        decks.each(function(index, ele) {
            
            ele.addEventListener("click", function() {
                popup(this.children[1].children[0].textContent)
            })
        })
        
        load.toggle();
    }
}

const handler = new Deck();

function onChange(redirectUrl)
{
    // const redirectUrl = '/create_deck';
    window.location.href = redirectUrl;
}

function popup(deckName) {
    if (deckName == '') {
        $('.header > h1').html('Unknow');
    } else {
        $('.header > h1').html(deckName);
    }
    
    $('#deck-menu').css("display", "flex");
}

function onClose() {
    $('#deck-menu').css("display", "none");
}

function handleSize() {
    let deck = $(".box")
    if ($(window).width() >= 601) {
        // Add onclick event if screen width is greater than or equal to 601 pixels
        deck.on('click', handleClick);
    } else {
        // Remove onclick event if screen width is less than 601 pixels
        deck.off('click', handleClick);
    }
}
