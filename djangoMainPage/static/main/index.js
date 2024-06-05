// Получить модальный
let modal = document.getElementById("myModal");

// Получить кнопку, которая открывает модальный
let btn = document.getElementById("myBtn");

// Получить элемент <span>, который закрывает модальный
let span = document.getElementsByClassName("close")[0];

if (modal != null & btn != null) {

// Когда пользователь нажимает на кнопку, откройте модальный
btn.onclick = function() {
  modal.style.display = "block";
}

// Когда пользователь нажимает на <span> (x), закройте модальное окно
span.onclick = function() {
  modal.style.display = "none";
}

// Когда пользователь щелкает в любом месте за пределами модального, закройте его
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
}


// Получить модальный
let modal1 = document.getElementById("myModal-2");

// Получить кнопку, которая открывает модальный
let btn1 = document.getElementById("myBtn-2");

// Получить элемент <span>, который закрывает модальный
let span1 = document.getElementsByClassName("close-2")[0];

// Когда пользователь нажимает на кнопку, откройте модальный
btn1.onclick = function() {
  modal1.style.display = "block";
}

// Когда пользователь нажимает на <span> (x), закройте модальное окно
span1.onclick = function() {
  modal1.style.display = "none";
}

// Когда пользователь щелкает в любом месте за пределами модального, закройте его
window.onclick = function(event) {
  if (event.target == modal1) {
    modal1.style.display = "none";
  }
}