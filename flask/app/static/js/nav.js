const hidden_nav = document.getElementById("hidden-nav");
const ham_bar = document.getElementById("ham-nav");

ham_bar.addEventListener("click", (e)=>{
    if (hidden_nav.classList.contains("activate")) {
        hidden_nav.classList.remove("activate");
    } else {
        hidden_nav.classList.add("activate");
    }
});