#!/usr/bin/python

##################################################################################
##                                                                              ##
##    Este es un script para sincronizar los archivos de dos directorios        ##
##    Copyright (C) 2015  Eduardo Parra Mazuecos                                ##
##                                                                              ##
##    This software is free software: you can redistribute it and/or modify     ##
##    it under the terms of the GNU General Public License as published by      ##
##    the Free Software Foundation, version 3 of the License,                   ##
##    or any later version.                                                     ##
##                                                                              ##
##    This program is distributed in the hope that it will be useful,           ##
##    but WITHOUT ANY WARRANTY; without even the implied warranty of            ##
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             ##
##    GNU General Public License for more details.                              ##
##                                                                              ##
##    You should have received a copy of the GNU General Public License         ##
##    along with this program.  If not, see <http://www.gnu.org/licenses/>.     ##
##                                                                              ##
##   MegaUp version 0.1, Copyright (C) 2015 Eduardo Parra Mazuecos              ##
##   email: eduparra90@gmail.com                                                ##
##   Website: http://www.eduardoparra.es                                        ##
##                                                                              ##
##################################################################################
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import os
        
class main(Gtk.Window):
	def __init__(self):
		rutas_origen = ["/home/directorio1/","/"] #Rutas de la carpeta de origen
		rutas_destino = ["/home/directorio2", "/"]  # Rutas de la carpeta de destino
		self.origen = None
		self.destino = None


		Gtk.Window.__init__(self, title="Sincronizador de directorios")
		self.set_border_width(10)
		
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.add(vbox)
		
		label = Gtk.Label("Sincronice los archivos con diferencias en "+
		"la carpeta de destino.") 
		label.set_justify(Gtk.Justification.FILL)
		vbox.pack_start(label, True, True, 0)
		label = Gtk.Label("Software desarrollado por Eduardo Parra Mazuecos <eduparra90@gmail.com>") 
		label.set_justify(Gtk.Justification.FILL)
		vbox.pack_start(label, True, True, 0)
		label = Gtk.Label("Licencia GNU GPLv3 o superior.\n") 
		label.set_justify(Gtk.Justification.FILL)
		vbox.pack_start(label, True, True, 0)

		
		label = Gtk.Label("Ruta del directorio de orígen:")
		vbox.pack_start(label, True, True, 0)

		combo_origen = Gtk.ComboBoxText()
		combo_origen.set_entry_text_column(0)
		combo_origen.connect("changed", self.origenSeleccionado)
		for currency in rutas_origen:
			combo_origen.append_text(currency)
		vbox.pack_start(combo_origen, False, False, 0)


		label = Gtk.Label("Ruta del directorio de destino:")
		vbox.pack_start(label, True, True, 0)

		combo_destino = Gtk.ComboBoxText()
		combo_destino.set_entry_text_column(0)
		combo_destino.connect("changed", self.origenDestino)
		for currency in rutas_destino:
			combo_destino.append_text(currency)
		vbox.pack_start(combo_destino, False, False, 0)

		button = Gtk.Button.new_with_label("¡Sincronizar!")
		button.connect("clicked", self.sincronizar)
		vbox.pack_start(button, True, True, 0)


	def sincronizar(self,button):
		if self.origen !=None and self.destino != None:
			print("hshhs")
			os.system('rsync -avzP "' + self.origen + '" "' + self.destino + '"')

	def origenSeleccionado(self,combo):
		text = combo.get_active_text()
		if text != None:
			self.origen = text

	def origenDestino(self,combo):
		text = combo.get_active_text()
		if text != None:
			self.destino = text


win = main()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
