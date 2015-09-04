#! /usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
from Journalisation import *

#--------------------
# Requeter
# Fonction qui permet de passer une requete SQL à une base
# En entrée : La requete
# En sortie : Le résultat de la requete ou "ERROR"
# Exemple : Requeter("localhost","root","","tifom","SELECT Code_OACI from aeroport where nom=%s","LFPG")[j][i]
#           renvoie le i_eme champ du j_ieme enregistrement
# 
#--------------------

def Requeter(Requete,Param=[]):

    # Ouverture de la base de données
    try:
      db = MySQLdb.connect(host=HOSTNAME, user=LOGIN, passwd=MDP, db=BASE)
    except:
      EcrireLog(FILE(),LINE(),"Ouverture de la base "+BASE+" impossible")
      return "ERROR";

    # Récupération d'un curseur
    curseur = db.cursor();
   
    # Execution de la requete et récupération du résultat
    try :
      curseur.execute(Requete,Param)
      Resultat = curseur.fetchall()
      curseur.close()
      return Resultat
    except :
      curseur.close()
      return "ERROR"

# ======================================
# IsAnAiport
# Rôle : Déterminer si un Code_OACI correspond bien à un aéroport
# Entrée : Un code OACI potentiel
# Sortie : 0 si oui
#          1 sinon
#          2 si erreur
# ======================================

def IsAnAirport (Code):
  if Requeter("SELECT nom from aeroport where Code_OACI=%s",Code) != "ERROR":
    if len(Requeter("SELECT nom from aeroport where Code_OACI=%s",Code))>=1:   
      return 0
    else:
      return 1
  else:
    return 2

print IsAnAirport("LFP")
