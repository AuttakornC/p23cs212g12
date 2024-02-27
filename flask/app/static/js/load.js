class Loader {
    load_window = document.getElementById("window-loader");

    toggle() {
        if (this.load_window.style.display==="flex") {
            this.load_window.style.display="none";
        } else {
            this.load_window.style.display="flex";
        }
    }
}

const load = new Loader();