class MyData {

    constructor() {
        this.currentPage = "prop";
    }

    getPage() {
        return this.currentPage;
    }

    togglePage() {
        if (this.currentPage==="prop") {
            this.currentPage="card";
        } else {
            this.currentPage="prop";
        }
    }
}

const my_state = new MyData();

const prop_btn = document.getElementById("prop-btn");
const card_btn = document.getElementById("card-btn");
const bg_btn = document.getElementById("bg-btn");

function onChangePage(page) {
    if (page!==my_state.getPage()) {
        my_state.togglePage();
        if (page==="card") {
            bg_btn.classList.add("switch");
            card_btn.classList.add("activate");
            prop_btn.classList.remove("activate");
        } else {
            bg_btn.classList.remove("switch");
            prop_btn.classList.add("activate");
            card_btn.classList.remove("activate");
        }
    }
}

const status_toggle = document.getElementById("status-toggle");
const status_input = document.getElementById("status");

function onStatusToggle() {
    const private_toggle = document.getElementById("private-toggle");
    const public_toggle = document.getElementById("public-toggle");
    const current = status_input.value;
    const circle = status_toggle.getElementsByClassName("circle");
    if (current==="private") {
        status_input.value = "public"
        circle[0].classList.add("switch");
        private_toggle.classList.remove("activate");
        public_toggle.classList.add("activate");
        status_toggle.classList.add("activate");
    } else {
        status_input.value = "private"
        circle[0].classList.remove("switch");
        public_toggle.classList.remove("activate");
        private_toggle.classList.add("activate");
        status_toggle.classList.remove("activate");
    }
}