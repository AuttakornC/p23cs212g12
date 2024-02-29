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
        this.getDeck();
    }

    async getDeck() {
        const respond = await fetch("/api/deck");
        const data = await respond.json();
        console.log(data);
        const deckContainner = document.getElementsByClassName('deck-bg');
        data["data"].forEach(element => {
            console.log(element);
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
                    <button id='edit' onclick="onChange('/edit');" type="button">
                        icon
                    </button>
                    <button id='play' onclick="onChange('/play');" type="button">
                        icon
                    </button>
                    <button id='delete' onclick="delete();" type="button">
                        icon
                    </button>
                </div>

            </div>`
          
        });
        
    }
}

function onChange(redirectUrl)
{
    // const redirectUrl = '/create_deck';
    window.location.href = redirectUrl;
}

const handler = new Deck();

console.log($('.title-deck'))