#! /usr/bin/python
# -*- coding: latin-1 -*-

# #########################################################
# Journalisation.py
# R�le : Journaliser le fonctionnement de l'application
# CRNA/N-ST-CAW-CAUTRA
# 15/05/2015
# #########################################################

from Date import * 
from Header import *
import os
import inspect # D�ja install� avec Python 2.7

# ###############################################################
# EcrireLog
# Ecriture de message dans un fichier quotidien de journalisation
# En entr�e : Le fichier concern� par le message
#             La ligne concern�e dans le fichier
#             Le message � �crire
# En sortie : Rien
# ###############################################################

def EcrireLog(Fichier,Ligne,MessageJournalisation):
 
  Horodatage = DateCourante()
  
  if not (os.path.exists(PATH_LOG)):    
    os.mkdir(PATH_LOG)
    
  NomFichier = PATH_LOG+str(Horodatage[2])+str(Horodatage[1])+str(Horodatage[0])+".log"

  MessageJournalisation2=str(Horodatage[3])+':'+str(Horodatage[4])+':'+str(Horodatage[5])+" - File : "+str(Fichier)+" - Ligne : "+str(Ligne)+" - "+str(MessageJournalisation)+"\n";
 
  FIC=open(NomFichier,"a" )
  FIC.write(MessageJournalisation2)
  FIC.close()
  ERROR = 1

# ###############################################################
# LINE
# Renvoie la ligne du fichier lors de l'appel de fonction
# ###############################################################
def LINE():
    return inspect.currentframe().f_back.f_lineno

# ###############################################################
# FILE
# Renvoie le nom complet du fichier lors de l'appel de fonction
# ###############################################################
def FILE():
    return os.path.basename(inspect.currentframe().f_back.f_code.co_filename)

 
