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
            deckContainner[0].innerHTML += `<span>${element.name}</span>`
          
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