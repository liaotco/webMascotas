/*RESPONSIVE*/

function alternar(menu)
{
   var oMenu = document.getElementById(menu);
   //Si el menu tiene clase abierto
   //cambia clase a cerrado y cambia el botón
if (oMenu.classList.contains('abierto')){
   oMenu.classList.remove('abierto');
   oMenu.classList.add('cerrado');
   
   }
//Si no está abierto, cambia clase a abierto y cambia el botón
else{
   oMenu.classList.remove('cerrado');
   oMenu.classList.add('abierto');

   }
}

/*VENTANA EMERGENTE PARA DETALLE*/
function ventanaSecundaria (URL){
  window.open(URL,"Detalle Producto","width=520,height=300,scrollbars=NO")
}

/*CARRUSEL FOTOS*/
let slideIndex = 1;
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

/*CARRITO*/
