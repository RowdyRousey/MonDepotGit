#!/usr/bin/env python
# -*- coding: latin-1 -*-

# Import de librairies ou de fichiers externes
from Header import * 
from GestionFichier import *

############################################
### Classe Application
### Classe de la fenêtre principale
############################################
      
class Application:
    def __init__(self):
        MainInterface = gtk.Builder()
        MainInterface.add_from_file("TIFO.glade") #On fait le lien avec le fichier GLADE
        MainInterface.connect_signals(self) #Connexion des signaux définis
        
        self.window = MainInterface.get_object("MainWindows")
        self.VisuDepouillement = MainInterface.get_object("VisuDepouillement")
               
        self.window.show()
        
    def on_MenuItemQuit_click(self,event):
        self.window.destroy()
        
    def on_MenuItemOuvrir_click(self,event):
        FileChooser=gtk.FileChooserDialog(
        title="Sélection d'un fichier Enregistrement",
        action=gtk.FILE_CHOOSER_ACTION_OPEN,
        buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_OPEN,gtk.RESPONSE_OK))
        FileChooser.set_current_folder(os.getcwd())
        
        MonFiltre = gtk.FileFilter()
        MonFiltre.set_name("Fichier Enregistrement")
        MonFiltre.add_pattern("ve*[!.txt]")
        FileChooser.add_filter(MonFiltre)
        
        Response = FileChooser.run()
        if Response == gtk.RESPONSE_OK:
          FileChooser.hide()
          ExtraireDonneesFichiers(self.window,self.VisuDepouillement,FileChooser.get_filename())          
        FileChooser.destroy()
        
    def on_MenuItemSave_click(self,event):
        print "J'ai clique sur Enregistrer"
        
    def on_MenuItemSaveAs_click(self,event):
        FileChooser=gtk.FileChooserDialog(title="Enregistrement d'un fichier dépouillé",
        action=gtk.FILE_CHOOSER_ACTION_SAVE,
        buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_SAVE,gtk.RESPONSE_OK))
        FileChooser.set_current_folder(os.getcwd())
        
        MonFiltre = gtk.FileFilter()
        MonFiltre.set_name("Fichier Dépouillé")
        MonFiltre.add_pattern("*.txt")
        FileChooser.add_filter(MonFiltre)
        
        Response = FileChooser.run()
        if Response == gtk.RESPONSE_OK:
          return FileChooser.get_filename()
        FileChooser.destroy()
        
    def on_MenuItemSettings_click(self,event):
        print "J'ai clique sur Param"
        
    def on_MenuItemAPropos_click(self,event):
        print "J'ai appuyé sur About"
               
if __name__ == "__main__":
	Application()
	gtk.main()
