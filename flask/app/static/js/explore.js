$(document).ready(function () {
    (function () {
        $.get("api/explore/all/decks", (decks)=>{
            //console.log(decks[0].name)
            $.each(decks, (key, value) =>{
                // console.log(value)    
                addDataDecks(value)
            })
            
            
        });
    })();
});

function addDataDecks(decks){
    //console.log(decks["name"]);
    //document.getElementsByClassName("deckName").innerHTML = decks["name"].innerHTML;
   //console.log(document.getElementsByClassName("deckName").innerHTML)
   const post_block = `<div class="box" onclick="onPreview(this)" dataDecks='${JSON.stringify(decks)}';>
    <div class="profile">
        <img class="profile-icon" src="/static/image/profile-icon.png" alt="">
        <span class="people">${decks.player_name}</span>
    </div>
    <div class="description"><h4 class="deckName">${decks.name}</h4><h5 class="cardNum">${decks.num_card} Cards</h5></div>
    <div></div>
    </div>`;
    $(".container").html($(".container").html()+post_block);
}


function onPreview(data) {
    const decks = JSON.parse(data.getAttribute('dataDecks'));
    const cards = decks.cards
    
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

function addWordPreview(question, answer) {
    const word = `<li><b>${question}</b><b>${answer}</b></li>
    <hr>`;
    $(".sug-list").html($(".sug-list").html()+word)

}

