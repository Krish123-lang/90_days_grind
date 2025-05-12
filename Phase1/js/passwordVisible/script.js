const password = document.getElementById('password')
const passToggle = document.getElementById('toggle')

passToggle.addEventListener('click', function () {
    const type = password.getAttribute("type") === "password" ? "text" : "password"
    password.setAttribute("type", type)

    this.classList.toggle('toggle')
})

const form = document.querySelector("form")
form.addEventListener("submit", (e) => {
    e.preventDefault()
})
