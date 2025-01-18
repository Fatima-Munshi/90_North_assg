function toggleMenu() { 
    var menu = document.getElementById("leftMenu"); 
    menu.classList.toggle("visible");
}

window.addEventListener('resize', function() {
    adjustPageScale();
});

function adjustPageScale() {
    const width = window.innerWidth;
    let scale = 1;

    if (width > 992 && width <= 1600) {
        scale = 0.9;
    } else if (width >= 700 && width <= 767) {
        scale = 0.8;
    } else if (width >= 600 && width < 700) {
        scale = 0.75;
    } else if (width <= 600) {
        scale = 0.5;
    }

    document.body.style.transform = `scale(${scale})`;
}

// Initial adjustment on page load
adjustPageScale();
