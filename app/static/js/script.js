localStorage.clear()
const inputBox1    = document.getElementById('input-box1')
const inputBox2  = document.getElementById('input-box2')
const inputBox3  = document.getElementById('input-box3')
const listContainer = document.getElementById('list-container')



function addTask() {
    if (inputBox1.value == "" || inputBox2.value == "" || inputBox3.value == "") {
        alert("You must type something!")
    } else {
        let li = document.createElement('li')
        li.innerHTML = '{\"object_id\":\"'+inputBox1.value +'\",\"name\":\"' + inputBox2.value+ '\",\"type\":\"'+inputBox3.value+'\"}'
        listContainer.appendChild(li)
        let span = document.createElement("span")
        span.innerHTML = "\u00d7"
        li.appendChild(span)
    }
    inputBox.value = ""
    saveData()
}

listContainer.addEventListener("click", (e) => {
    if (e.target.tagName === "LI") {
        e.target.classList.toggle("checked")
        saveData()
    } else if (e.target.tagName === "SPAN") {
        e.target.parentElement.remove()
        saveData()
    }
}, false)

function saveData() {
    localStorage.setItem("data", listContainer.innerHTML)
}

function showTasks() {
    listContainer.innerHTML = localStorage.getItem('data')
}

showTasks()
