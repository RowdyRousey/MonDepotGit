#! /usr/bin/python
# -*- coding: latin-1 -*-

# #########################################################
# Journalisation.py
# Rôle : Journaliser le fonctionnement de l'application
# CRNA/N-ST-CAW-CAUTRA
# 15/05/2015
# #########################################################

from Date import * 
from Header import *
import os
import inspect # Déja installé avec Python 2.7

# ###############################################################
# EcrireLog
# Ecriture de message dans un fichier quotidien de journalisation
# En entrée : Le fichier concerné par le message
#             La ligne concernée dans le fichier
#             Le message à écrire
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

 
