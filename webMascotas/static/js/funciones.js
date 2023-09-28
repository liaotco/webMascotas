
let btnMenu = document.getElementById('btn-menu');
let mainNav = document.getElementById('main-nav');
btnMenu.addEventListener('click', function(){
  mainNav.classList.toggle('mostrar');
});

$(document).ready(function () {
  // POP up 
function showPopupCar(){
    $('.pop-up').addClass('show');
    $('.pop-up-wrap').addClass('show');
    $('.modal_carrito').addClass('show');
           
}
function showPopupNews(){
  $('.pop-up').addClass('show');
  $('.pop-up-wrap').addClass('show');
  $('.modal_news').addClass('show');
}
function showPopupLogin(){
  $('.pop-up').addClass('show');
  $('.pop-up-wrap').addClass('show');
  $('.modal_login').addClass('show');
}
function showPopupSubs(){
  $('.pop-up').addClass('show');
  $('.pop-up-wrap').addClass('show');
  $('.mensaje_subscripcion').addClass('show');
}
function showPopupContacto(){
  $('.pop-up').addClass('show');
  $('.pop-up-wrap').addClass('show');
  $('.mensaje_contacto').addClass('show');
}

function showPopupAgregar(){
  $('.mensaje_añadir').addClass('show');
  setTimeout(4000);
}
function showPopupEliminar(){
  $('.mensaje_eliminar').addClass('show');
  setTimeout(4000);
}


$("#close").click(function(){
    $('.pop-up').removeClass('show');
    $('.pop-up-wrap').removeClass('show');
    $('.modal_carrito').removeClass('show');
    $('.modal_news').removeClass('show');
    $('.modal_login').removeClass('show');
    $('.modal_subscripcion').removeClass('show');
    $('.mensaje_contacto').removeClass('show');
});

/* Modales tienda y mensajes de gestion carrito*/
$(".btn-abrir").click(showPopupCar);
$(".btn-news").click(showPopupNews);
$(".btn-login").click(showPopupLogin);
$(".btn-agregar").click(showPopupAgregar);
$(".btn-eliminar").click(showPopupEliminar);
$(".modal_btn").click(showPopupSubs);
$(".button_formulario").click(showPopupContacto);
});





/*VENTANA EMERGENTE PARA DETALLE*/
function ventanaSecundaria (URL){
  window.open(URL,"Detalle Producto","width=520,height=300,scrollbars=NO")
}


