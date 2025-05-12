const btn1 = document.getElementById("btn1")
/* function clickme() {
    alert("Button clicked!")
}

btn1.addEventListener('click', clickme) */

btn1.addEventListener('click', () => {
    alert("Button was clicked!")
})

let link = document.querySelector('a')
link.addEventListener("click", (event) => {
    console.log('clicked');
    event.preventDefault()
})