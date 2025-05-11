const menuToggle = document.getElementById("menuToggle")
const navLinks = document.getElementById("navLinks")
const menuIcon = document.getElementById("menuIcon")

menuToggle.addEventListener("click", () => {
    navLinks.classList.toggle("active")
    if (navLinks.classList.contains("active")) {
        menuIcon.classList.replace("fa-bars", "fa-times")
    }
    else {
        menuIcon.classList.replace("fa-times", "fa-bars")
    }
})