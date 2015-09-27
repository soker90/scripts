#!/usr/bin/python

##################################################################################
##										                                        ##
##    Este es un script para sincronizar los archivos de dos directorios 	    ##
##    Copyright (C) 2015  Eduardo Parra Mazuecos				                ##
##										                                        ##
##    This software is free software: you can redistribute it and/or modify		##
##    it under the terms of the GNU General Public License as published by	    ##
##    the Free Software Foundation, version 3 of the License, 			        ##
##    or any later version.					                                    ##
##										                                        ##
##    This program is distributed in the hope that it will be useful,		    ##
##    but WITHOUT ANY WARRANTY; without even the implied warranty of		    ##
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the		        ##
##    GNU General Public License for more details.				                ##
##										                                        ##
##    You should have received a copy of the GNU General Public License		    ##
##    along with this program.  If not, see <http://www.gnu.org/licenses/>. 	##
##										                                        ##
##   MegaUp version 0.1, Copyright (C) 2015 Eduardo Parra Mazuecos		        ##
##   email: eduparra90@gmail.com		                  			            ##
##   Website: http://www.eduardoparra.es 					                    ##
##										                                        ##
##################################################################################

from gi.repository import Gtk
        
class main(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="jj")
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
		
		self.progressbar = Gtk.ProgressBar()
		vbox.pack_start(self.progressbar, True, True, 0)
		label = Gtk.Label("") 
		vbox.pack_start(label, True, True, 0)
		
		label = Gtk.Label("Ruta del directorio de orígen:")
		vbox.pack_start(label, True, True, 0)
		
		lista_origen = Gtk.ListStore(int, str)
		lista_origen.append([1,"/home/$user"])
		lista_origen.append([2,"/boot"])
        
		combo_origen = Gtk.ComboBox.new_with_model_and_entry(lista_origen)
		#name_combo.connect("changed", self.on_name_combo_changed)
		combo_origen.set_entry_text_column(1)
		vbox.pack_start(combo_origen, False, False, 0)
		
		label = Gtk.Label("Ruta del directorio de destino:")
		vbox.pack_start(label, True, True, 0)
		
		lista_destino = Gtk.ListStore(int, str)
		lista_destino.append([1,"aaa"])
		lista_destino.append([2,"sss"])
		
		combo_destino = Gtk.ComboBox.new_with_model_and_entry(lista_destino)
		#name_combo.connect("changed", self.on_name_combo_changed)
		combo_destino.set_entry_text_column(1)
		vbox.pack_start(combo_destino, False, False, 0)
		
		button = Gtk.Button(label="¡Sincronizar!")
		label.set_mnemonic_widget(button)
		vbox.pack_start(button, True, True, 0)
		
	
win = main()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
