#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gtk

############################################
### Classe Fenêtre A propos
### Ne fonctionne pas
### N'arrive pas à fermer sur Bouton Fermer
############################################

class AboutWin:
    def __init__(self):
        AboutInterface = gtk.Builder()
        AboutInterface.add_from_file("About.glade")
        #AboutInterface.connect_signals(self)
        
        self.AboutWindows = AboutInterface.get_object("AboutWindows")
        self.AboutWindows.show()
        
    def OnClickFermer(self,event):
      self.AboutWindows.destroy()
     
