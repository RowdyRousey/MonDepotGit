#! /usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
from Journalisation import *

#--------------------
# Requeter
# Fonction qui permet de passer une requete SQL à une base
# En entrée : Le hostname du serveur SQL
#             Le login du compte SQL
#             Le mot de passe du compte
#             La BDD
#             La requete
# En sortie : Le résultat de la requete
# Exemple : Requeter("localhost","root","","tifom","SELECT Code_OACI from aeroport where nom=%s","LFPG")[j][i]
#           renvoie le i_eme champ du j_ieme enregistrement
# 
#--------------------

def Requeter(Hostname,Login,Mdp,Base,Requete,Param=[]):

    # Ouverture de la base de données
    try:
      db = MySQLdb.connect(host=Hostname, user=Login, passwd=Mdp, db=Base)
    except:
      EcrireLog(FILE(),LINE(),"Ouverture de la base "+Base+" impossible")
      exit(1);

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

def IsAnItem (Base,Item):
  if Requeter("localhost","root","","tifom","SELECT nom from "+Base+" aeroport where Code_OACI=%s",Item) != "ERROR":
    if len(Requeter("localhost","root","","tifom","SELECT nom from aeroport where Code_OACI=%s",Item))>=1:   
      return 0
    else:
      return 1
  else:
    return 2

