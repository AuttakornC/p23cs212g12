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
            deckContainner[0].innerHTML += `<div class="box">
            <div class="profile">
                <img class="profile-icon" src="/static/image/profile-icon.png" alt="">
                <span class="people">${element.username}</span>
            </div>
            <div class="description"><h4 id="nameD" class="deckName">${element.name}</h4><h5 class="cardNum">${element.len_card} Cards</h5></div>
            <button class="button">Preview</button>
        </div>`
          
        });
        
    }
}

// add Deck
// const deckBg = document.getElementsByClassName('deck-bg');
// function onAdd()
// {
//     if (deckBg.lastElementChild) {
//         const last_number = parseInt(deckBg.lastElementChild.getAttribute("order_"));
//         if (!isNaN(last_number)) {
//             number_input = last_number+1;
//         }
//     }
// }

const handler = new Deck();
// handler.getDeck();
console.log('Aaaaaaa');