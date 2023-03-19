
function expand(id) {

    btn = document.getElementById(id)

    nav = document.getElementById('navigation')

    nav.classList.toggle('transform')

    if (btn.getAttribute("src") == "static/images/close.png") {
        btn.setAttribute("src", "static/images/menu.png")
    }

    if (btn.getAttribute("src") == "static/images/menu.png") {
        btn.setAttribute("src", "static/images/close.png")
    }

    console.log(btn.getAttribute("src"))
}

function dis() {

    msg = document.getElementById("messages")

    msg.style.display = "none";
}


