#! /usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
from Journalisation import *

HOSTNAME="localhost"
LOGIN = "root"
MDP = ""
BASE="tifom"

class MyDatabaseConnection():
  
  def __init__(self, host, user, passwd, database):
    try:
      self.connection = MySQLdb.connect (host, user, passwd, database)
      self.s = self.connection.cursor()    
    except:
      EcrireLog(FILE(),LINE(),"Ouverture de la base "+BASE+" impossible")
      print "La connection a la base ne s'est pas realisee correctement"
  
  def close(self):
    self.connection.close()
    
#----------------------------------------------------------------
# Requeter
# Fonction qui permet de passer une requete SQL à une base
# En entrée : La requete
# En sortie : Le résultat de la requete ou "ERROR"
# Exemple : Requeter("localhost","root","","tifom","SELECT Code_OACI from aeroport where nom=%s","LFPG")[j][i]
#           renvoie le i_eme champ du j_ieme enregistrement
# 
#----------------------------------------------------------------

  def Requeter(self,Requete,Param=[]):   
      self.s.execute(Requete,Param)
      Resultat = self.s.fetchall()
      return Resultat
      # Execution de la requete et récupération du résultat
      #try :
      #    print curseur.execute(Requete,Param)
      #    Resultat = curseur.fetchall()
      #    return Resultat
      #except :
      #    return "ERROR"

  # ======================================
  # IsAnAiport
  # Rôle : Déterminer si un Code_OACI correspond bien à un aéroport
  # Entrée : Un code OACI potentiel
  # Sortie : 0 si oui
  #          1 sinon
  #          2 si erreur
  # ======================================

  def IsAnAirport(self,Code):
      if self.Requeter("SELECT nom from aeroport where Code_OACI=%s",Code) != "ERROR":
          if len(self.Requeter("SELECT nom from aeroport where Code_OACI=%s",Code))>=1:   
              return 0
          else:
              return 1
      else:
          return 2

  # ======================================
  # GetIdTypeMessage
  # Rôle : Retourner l'identifiant du type de message
  # Entrée : Le type de message
  # Sortie : 0 si oui
  #          1 sinon
  #          2 si erreur
  # ======================================
  def GetIdTypeMessage(self,Type):
      try:
          return self.Requeter(self,"SELECT id FROM type_message WHERE trigramme=%s",Type)[0][0]
      except:
          return 0

  # ======================================
  # GetNomAirport
  # Rôle :  
  # Entrée :  
  # Sortie :  
  #           
  #           
  # ======================================
  def GetNomAirport(self,Code):
      
      try:
          return self.Requeter("SELECT Nom FROM aeroport WHERE Code_OACI=%s",Code)[0][0]
      except:
          return 0

