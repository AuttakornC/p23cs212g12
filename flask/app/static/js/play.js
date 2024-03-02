class Play {

    deck_data = null;
    main_show = document.getElementById("card-show");
    right_btn = document.getElementById("next-btn");
    left_btn = document.getElementById("back-btn");
    none_btn = document.getElementById("disable");
    show_btn = document.getElementById("show-btn");
    current = 0;
    queue = [];
    onANS = () => {};

    constructor(deck_data) {
        this.deck_data = deck_data;
        this.queue = [...Array(this.deck_data.cards.length).keys()];
        console.log(this.queue)
        this.main_show.innerHTML = this.deck_data.cards[this.queue[this.current]].question;
        this.onANS = (e) => {
            this.main_show.innerHTML = this.deck_data.cards[this.queue[this.current]].answer;
            this.right_btn.innerHTML = "Keep";
            this.left_btn.innerHTML = "Discard";
            this.left_btn.setAttribute("onclick", "play.onDiscard();");
            none_btn.style.display = "none";
        }
        this.left_btn.setAttribute("onclick", "play.onPrevious();");
        this.main_show.parentElement.addEventListener("click", this.onANS);
    }



    onNext() {
        if (this.current>=this.queue.length) {
            this.current = this.queue.length-1;
        } else {
            this.current++;
            // console.log(this.current);
        }

        this.main_show.parentElement.removeEventListener("click", this.onANS);
        this.main_show.innerHTML = this.deck_data.cards[this.queue[this.current]].question;
        this.onANS = (e) => {
            this.main_show.innerHTML = this.deck_data.cards[this.queue[this.current]].answer;
            this.right_btn.innerHTML = "Keep";
            this.left_btn.innerHTML = "Discard";
            this.left_btn.setAttribute("onclick", "play.onDiscard();");
        };
        this.main_show.parentElement.addEventListener("click", this.onANS);
        this.right_btn.innerHTML = "Skip";
        this.left_btn.innerHTML = "Previous";
        this.left_btn.classList.remove("disable");
        this.left_btn.setAttribute("onclick", "play.onPrevious();");
        none_btn.style.display = "block";
    }

    onKeep() {
        this.show_btn.style.display = '';
        this.queue.push(this.queue[this.current]);
    }

    onDiscard() {
        this.show_btn.style.display = '';
        this.queue = [...this.queue.slice(0, this.current), ...this.queue.slice(this.current+1)];
        this.current--;
        this.onNext();
    }

    onPrevious() {
        if (this.current!==0) {
            this.current--;
            this.main_show.parentElement.removeEventListener("click", this.onANS);
            this.main_show.innerHTML = this.deck_data.cards[this.queue[this.current]].question;
            this.onANS = (e) => {
                this.main_show.innerHTML = this.deck_data.cards[this.queue[this.current]].answer;
                this.right_btn.innerHTML = "Keep";
                this.left_btn.innerHTML = "Discard";
                this.left_btn.classList.add("disable");
                this.left_btn.classList.remove("disable");
                this.left_btn.setAttribute("onclick", "play.onDiscard();");
            };
            this.main_show.parentElement.addEventListener("click", this.onANS);
            this.right_btn.innerHTML = "Skip";
            this.left_btn.innerHTML = "Previous";
            if (this.current === 0) {
                this.left_btn.classList.add("disable");
            }
            this.left_btn.setAttribute("onclick", "play.onPrevious();");
            none_btn.style.display = "block";
        }
    }
    
}

const play = new Play(deck_data);

function next() {
    play.onKeep();
    play.onNext();
}

function onClose(){
    confirm_.open("Quit","Are you sure you want you quit?",() =>{
        window.location.href = '/';
    })
    
}


