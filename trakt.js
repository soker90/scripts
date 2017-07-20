// ==UserScript==
// @name        Trakt
// @namespace   trakt.soker
// @description Traducción de trakt.tv al español
// @include     https://trakt.tv/*
// @version     1
// @grant       none
// ==/UserScript==
//Titulo
if(document.title = "Dashboard - Trakt.tv") { document.title = "Inicio - Trakt.tv"; }

//Cabecera
$('#main-nav ul:first').html('<li><a href="/shows/trending">TV</a></li><li><a href="/movies/trending">Peliculas</a></li><li><a href="/calendars">Calendario</a></li>')
$('#main-nav ul:last').html('<li><a href="/discover">Descubrir</a></li><li><a href="/apps">Aplicaciones</a></li><li><a href="/vip">VIP</a></li>')

//Dashboard
var text = $('#results-top-wrapper div:nth-child(2) div:first H1').html().replace('Hello','Hola')
$('#results-top-wrapper div:nth-child(2) div:first H1').html(text)
var text = $('#results-top-wrapper div:nth-child(2) div:first h2').html().replace('Member since','Miembro desde')
$('#results-top-wrapper div:nth-child(2) div:first h2').html(text)
$('#results-top-wrapper div:nth-child(2) div:nth-child(3)').html('Año en<br>Datos')
$('#results-top-wrapper div:nth-child(2) a:nth-child(2) div:first div:first').html('Tu<br>Perfil')

$('#user-menu ul').html('<li><a href="/dashboard">Inicio</a></li><li><a href="/users/soker">Perfil</a></li><li><a href="/users/soker/history">Historial</a></li><li><a href="/users/soker/progress">Progreso</a></li><li><a href="/users/soker/collection">Colección</a></li><li><a href="/users/soker/ratings">Calificaciones</a></li><li><a href="/users/soker/lists">Listas</a></li><li><a href="/users/soker/comments">Comentarios</a></li><li><a href="/users/soker/network">Amigos</a></li><li><a href="/widgets">Widgets</a></li><li><a href="/users/soker/year">Año en números</a></li><li><a href="/settings">Configuración</a></li><li><a href="/logout">Salir</a></li>')

