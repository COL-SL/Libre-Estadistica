#!/usr/bin/python
# -*- coding: latin-1 -*-
'''
Copyright (C) 2017  Manuel David Jim�nez Pati�o

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>
'''
import pygtk
pygtk.require('2.0')
import gtk
from shutil import copyfile


class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title(u"Libre Estad�stica")
        self.set_size_request(450, 400)
        self.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(6400, 6400, 6440))
        self.set_position(gtk.WIN_POS_CENTER)

        mb = gtk.MenuBar()

        filemenu = gtk.Menu()
        filem = gtk.MenuItem("File")
        filem.set_submenu(filemenu)

        imenu = gtk.Menu()
        importm = gtk.MenuItem("Import")
        importm.set_submenu(imenu)
        inews = gtk.MenuItem("Importar fichero cvs...")
        inews.connect("activate", self.importar_fichero_cvs, None)
        ibookmarks = gtk.MenuItem("Import bookmarks...")
        imail = gtk.MenuItem("Import mail...")
        imenu.append(inews)
        imenu.append(ibookmarks)
        imenu.append(imail)
        filemenu.append(importm)

        mb.append(filem)

        toolmenu = gtk.Menu()
        toolm = gtk.MenuItem("Herramientas")
        toolm.set_submenu(toolmenu)

        imenu_two = gtk.Menu()
        mediam = gtk.MenuItem(u"Medidas Tendencia Central")
        mediam.set_submenu(imenu_two)
        mediam_sub = gtk.MenuItem(u"Media aritm�tica")
        mediam_sub.connect("activate", self.media_aritmetica, None)

        imenu_three = gtk.Menu()
        dispersionm = gtk.MenuItem(u"Medidas Dispersi�n")
        dispersionm.set_submenu(imenu_three)
        dispersionm_sub = gtk.MenuItem(u"Rango")
        dispersionm_sub.connect("activate", self.rango, None)
        imenu_three.append(dispersionm_sub)
        imenu_two.append(mediam_sub)
        toolmenu.append(mediam)
        toolmenu.append(dispersionm)
        mb.append(toolm)

        exit = gtk.MenuItem("Exit")
        exit.connect("activate", gtk.main_quit)
        filemenu.append(exit)

        vbox = gtk.VBox(False, 2)
        vbox.pack_start(mb, False, False, 0)

        self.add(vbox)

        self.connect("destroy", gtk.main_quit)
        self.show_all()

    def media_aritmetica(self, widget, data=None):
        print u"Calculamos Media Aritm�tica"

    def rango(self, widget, data=None):
        print u"Rango"

    def importar_fichero_cvs(self, widget, data=None):
        dialog = gtk.FileChooserDialog("Abrir..",
                                       None,
                                       gtk.FILE_CHOOSER_ACTION_OPEN,
                                       (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                        gtk.STOCK_OPEN, gtk.RESPONSE_OK))
        dialog.set_default_response(gtk.RESPONSE_OK)

        '''
        filter = gtk.FileFilter()
        filter.set_name("All files")
        filter.add_pattern("*")
        dialog.add_filter(filter)

        filter = gtk.FileFilter()
        filter.set_name("Images")
        filter.add_mime_type("image/png")
        filter.add_mime_type("image/jpeg")
        filter.add_mime_type("image/gif")
        filter.add_pattern("*.png")
        filter.add_pattern("*.jpg")
        filter.add_pattern("*.gif")
        filter.add_pattern("*.tif")
        filter.add_pattern("*.xpm")
        dialog.add_filter(filter)
        '''
        response = dialog.run()
        if response == gtk.RESPONSE_OK:
            print dialog.get_filename(), 'selected'
            copyfile(dialog.get_filename(), "ojete_2.pdf")
        elif response == gtk.RESPONSE_CANCEL:
            print 'Closed, no files selected'
        dialog.destroy()


PyApp()
gtk.main()