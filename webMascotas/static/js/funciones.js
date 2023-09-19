
let btnMenu = document.getElementById('btn-menu');
let mainNav = document.getElementById('main-nav');
btnMenu.addEventListener('click', function(){
  mainNav.classList.toggle('mostrar');
});


$(document).ready(function () {
  // POP up 
function showPopup(){
    $('.pop-up').addClass('show');
    $('.pop-up-wrap').addClass('show');
}

$("#close").click(function(){
    $('.pop-up').removeClass('show');
    $('.pop-up-wrap').removeClass('show');
});

$(".btn-abrir").click(showPopup);

});

/*VENTANA EMERGENTE PARA DETALLE*/
function ventanaSecundaria (URL){
  window.open(URL,"Detalle Producto","width=520,height=300,scrollbars=NO")
}

/*CARRUSEL FOTOS*/
/*let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}
*/
/*LOGIN*/
let loginForm = document.querySelector(".my-form");

loginForm.addEventListener("submit", (e) => {
    e.preventDefault();
    let email = document.getElementById("email");
    let password = document.getElementById("password");

    console.log('Email:', email.value);
    console.log('Password:', password.value);
    // process and send to API 
});
function ventanaLogin (URL){
  window.open(URL,"Login","width=520px,height=400px,scrollbars=YES")
}

