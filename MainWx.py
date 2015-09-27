#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

try:
  import wx
except ImportError:
  raise ImportError,"Le module wxPython est requis pour ce programme"

from Header import *
from MainPanel import *

class MonApplication(wx.Frame):
    def __init__(self,parent,id,title):
      p = wx.Frame.__init__(self,parent,id,title,size=(LARGEUR,HAUTEUR))
      self.SetBackgroundColour(COULEUR_FOND)
      self.parent = parent
      self.Initialiser()
      self.Proprietes()
      self.MyMenu()
      
      w = wx.Panel(self)
      MainPanel(self,p)
      
      
        
        
      

    def Initialiser(self):
        self.Show(True)
        
    def Proprietes(self): 
      self.Centre(2) #2 correspond aux deux directions Horizontales et Verticales

      icon = wx.EmptyIcon()
      icon.CopyFromBitmap(wx.Bitmap("ex.ico", wx.BITMAP_TYPE_ANY))
      self.SetIcon(icon) 
      
    def MyMenu(self):
      self.BarreMenu = wx.MenuBar()
      Menu1 = wx.Menu()
      Menu1.Append(101, "&Ouvrir", "Ouverture d'un fichier Enregistrement")
      Menu1.Append(102, "&Enregistrer", "Sauvegarde d'un fichier dépouillé")
      Menu1.Append(103, "&Enregistrer Sous", "Sauvegarde d'un fichier dépouillé en modifiant son nom")
      Menu1.Append(104, "&Imprimer", "Impression d'un fichier dépouillé")
      Menu1.Append(105, "&Quitter", "")
      self.BarreMenu.Append(Menu1, "&Fichier")
      
      Menu2 = wx.Menu()
      Menu2.Append(201, "&Configuration", "Paramétrage de l'application")
      self.BarreMenu.Append(Menu2, "&Paramétrage")     
      
      Menu3 = wx.Menu()
      Menu3.Append(301, "&A Propos", "")
      Menu3.Append(302, "&Manuel Utilisateur", "")
      self.BarreMenu.Append(Menu3, "&?")   
      
      # Menu events
    

      self.Bind(wx.EVT_MENU, self.OuvrirFichier, id=101)
      #self.Bind(wx.EVT_MENU, self.Menu102, id=102)
      #self.Bind(wx.EVT_MENU, self.Menu103, id=103)
      self.Bind(wx.EVT_MENU, self.CloseWindows, id=105)  
      
      self.SetMenuBar(self.BarreMenu)
    
    def OuvrirFichier(self,event):
      DialogOuvrirFichier = wx.FileDialog(self, message="Choisir un fichier Enregistrement OLDI",
            defaultDir=os.getcwd(), defaultFile="", wildcard="Fichiers OLDI (*OLDI*)|*OLDI*",
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
            )

      if DialogOuvrirFichier.ShowModal() == wx.ID_OK:           
        FicSelect = DialogOuvrirFichier.GetPaths()[0]
        IdFichier = OuvrirFichier(FicSelect)
        

      DialogOuvrirFichier.Destroy()
      

    def CloseWindows(self,event):
      self.Destroy()

if __name__ == "__main__":
    app = wx.App()
    frame = MonApplication(None,-1,TITRE)
    app.MainLoop()
