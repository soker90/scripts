// ==UserScript==
// @name        Trakt
// @namespace   trakt.soker
// @description Traducción de trakt.tv al español
// @include     https://trakt.tv/*
// @version     1
// @grant       none
// ==/UserScript==
//Titulo


//Cabecera
$('#main-nav ul:first').html('<li><a href="/shows/trending">TV</a></li><li><a href="/movies/trending">Peliculas</a></li><li><a href="/calendars">Calendario</a></li>')
$('#main-nav ul:last').html('<li><a href="/discover">Descubrir</a></li><li><a href="/apps">Aplicaciones</a></li><li><a href="/vip">VIP</a></li>')

$('#user-menu ul').html('<li><a href="/dashboard">Inicio</a></li><li><a href="/users/soker">Perfil</a></li><li><a href="/users/soker/history">Historial</a></li><li><a href="/users/soker/progress">Progreso</a></li><li><a href="/users/soker/collection">Colección</a></li><li><a href="/users/soker/ratings">
                        caciones</a></li><li><a href="/users/soker/lists">Listas</a></li><li><a href="/users/soker/comments">Comentarios</a></li><li><a href="/users/soker/network">Amigos</a></li><li><a href="/widgets">Widgets</a></li><li><a href="/users/soker/year">Revisión del año</a></li><li><a href="/settings">Configuración</a></li><li><a href="/logout">Salir</a></li>')

$('#links-wrapper div a:first').text('Perfil')
$('#links-wrapper div a:nth-child(2)').text('Historial')
$('#links-wrapper div a:nth-child(3)').text('Progreso')
$('#links-wrapper div a:nth-child(4)').text('Colección')
$('#links-wrapper div a:nth-child(5)').text('Calificaciones')
$('#links-wrapper div a:nth-child(6)').text('Listas')
$('#links-wrapper div a:nth-child(7)').text('Comentarios')
$('#links-wrapper div a:nth-child(8)').text('Amigos')
$('#links-wrapper div a:nth-child(9)').text('Revisión del año')

//Dashboard
if(document.title.indexOf("Dashboard") > -1) 
{ 
  document.title = "Inicio - Trakt.tv"; 
  var text = $('#results-top-wrapper div:nth-child(2) div:first H1').html().replace('Hello','Hola')
  $('#results-top-wrapper div:nth-child(2) div:first H1').html(text)
  var text = $('#results-top-wrapper div:nth-child(2) div:first h2').html().replace('Member since','Miembro desde')
  $('#results-top-wrapper div:nth-child(2) div:first h2').html(text)
  $('#results-top-wrapper div:nth-child(2) div:nth-child(3)').html('Año en<br>Datos')
  $('#results-top-wrapper div:nth-child(2) a:nth-child(2) div:first div:first').html('Tu<br>Perfil')
}

//Progress
if(document.title.indexOf("progress") > -1) { 
  var i = 1;
  while (typeof $('#progress-wrapper div:first div:nth-child('+i+') div:nth-child(2)').html() !== 'undefined') {
    var text = $('#progress-wrapper div:first div:nth-child('+i+') div:nth-child(2) p').html();
    text = text.replace(/episode/g,'episodio');
    text = text.replace('Watched','Vistos');
    text = text.replace('of','de');
    text = text.replace('for','con');
    text = text.replace('plays','reproducciones');
    text = text.replace('which leaves',', quedan');
    text = text.replace('left to watch','para acabar');
    text = text.replace('Last watched','Último visto');
    text = text.replace('"</span></a>','"</span></a> hace');
    text = text.replace('minutes ago on','minutos el');
    text = text.replace('Great job, every episodio is watched!','¡Gran trabajo, todos los episodios vistos!');
    text = text.replace('about','alrededor de');
    text = text.replace('hours ago on ','horas el ');
    text = text.replace('hour ago on ','hora el ');
    text = text.replace('day ago on ','día el ');
    text = text.replace('days ago on','dias el');
    text = text.replace('month ago on','mes el');
    text = text.replace('months ago on','meses el');
    text = text.replace('year ago on','año el');
    text = text.replace('years ago on','años el');
    text = text.replace('over','más de');
    text = text.replace('almost','casi');
    $('#progress-wrapper div:first div:nth-child('+i+') div:nth-child(2) p').html(text);
    i= i+1;
  }
  
  var text = $('.subnav-wrapper div:first div:first span').html();
  text = text.replace(/Watched/g,'Vistos');
  text = text.replace(/Collected/g,'Coleccionados');
  $('.subnav-wrapper div:first div:first span').html(text);
  
}


