#! /usr/bin/python
# -*- coding: utf-8 -*-

import wx

class MainPanel(wx.Panel):
    """
    Définit une ligne de composants pour les pièces remplacées
    Génère un événement EVT_PIECE_DELETED lors du click sur le bouton `[-]`
    """

    def __init__(self, parent, index):
        w=wx.Panel(parent)
        w.SetBackgroundColour("red")
        self._index = index
        self.CreateControls()
        
        
    def CreateControls(self):
        # Choix de la pièce
        self.sttPiece = wx.StaticText(self, wx.ID_ANY, u'Piece :')
        self.pieces = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, [], wx.CB_SORT)
        # Quantité
        self.sttQuantity = wx.StaticText(self, wx.ID_ANY, u'Quantite :')
        self.quantity = wx.SpinCtrl(self, wx.ID_ANY, u'11111111111111', wx.DefaultPosition, wx.Size(60, -1), wx.SP_ARROW_KEYS, 1, 20, 1)
       
        # Sizer
        bxs = wx.BoxSizer(wx.HORIZONTAL)
       
        bxs.Add(self.sttPiece,    0,  wx.LEFT, 4)
        bxs.Add(self.pieces,      1,  wx.LEFT, 4)
        bxs.Add(self.sttQuantity, 2,  wx.LEFT, 4)
        bxs.Add(self.quantity,    3,  wx.LEFT, 4)
       
        
           
        
        self.SetSizer(bxs)
        
 
