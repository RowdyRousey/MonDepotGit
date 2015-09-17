#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Header import *
from Date import *
from Main import * 
from Journalisation import * 
from Requeter import * 

# ###############################################################
# ExtraireDonneesFichiers
# Extraction des données utiles d'un fichier
# En entrée : La Fenêtre où inscrire les données
#             La Zone de texte où inscrire les données
#             Le nom du fichier à dépouiller
# En sortie : Rien
# ###############################################################

def ExtraireDonneesFichiers(Fenetre,ZoneTexte,NomFichier):
    start_time = time.time()  
    EnTete = ExtraireEnTete(NomFichier)    
    Fenetre.set_title("Dépouillement d'un fichier "+str(EnTete['Type']))
    
    #Ouverture du fichier
    try:
        IdFichier = open(NomFichier,"rb")
    except: 
        EcrireLog(FILE(),LINE(),"Ouverture de "+NomFichier+" impossible")
        exit(0)
    
    # Boucle de lecture    
    Messages=[]

    while True:
      try:
        Donnees=IdFichier.read(LONG_BUFFER)        
      except:
        EcrireLog(FILE(),LINE(),"Erreur de lecture du fichier "+NomFichier)
        exit(0)
      if len(Donnees)==0:
        break

      Donnees = Donnees[LONG_HEAD_BUFFER:]
      Buffer=""
 
      while not ExprFinMessage.search(Donnees):
         
        EnteteBloc = Donnees[:LONG_HEAD_BLOC]
        LongBloc = (ord(EnteteBloc[3])*2) + 4

        ## S'il s'agit d'un message OLDI
        if ExprModuleOldi.search(EnteteBloc):          
          if EnteteBloc[1] == "\x01":
            
            # On elimine les series d'espace par un seul
            Bloc = ExprSpace.sub( " ", Donnees[LONG_HEAD_BLOC:LongBloc])
          
            # S'il s'agit du 1er bloc
            if EnteteBloc[5] == "\x01":              
              # On recherche l'expression de la date dans le bloc
              ResultDate = ExprDate.search(Bloc)
              Buffer = Buffer + ResultDate.group(0) + "\n"              
              
            ## On elimine les caractere parasite du SGT
            Message = ExprMess.search(Bloc)
            if Message:
              Message_=Message.group(0)[1:]
              Champ = Message_.split("-")

              # Pour l'instant je fais le message ABI
              TypeMessage = Champ[0][0:3] #Doit être dans la base des messages gérés
              if GetIdTypeMessage(TypeMessage) == 0 :
                print "Le type message n'est pas valide"
              
              NumSeq = Champ[0][len(Champ[0])-3:len(Champ[0])] #Doit être 3 chiffres
              if not re.search("[0-9]{3}",NumSeq,re.MULTILINE):
                EcrireLog(FILE(),LINE(),"Le numéro de séquence "+NumSeq+" est invalide")
              
              # Les deux champs suivants doivent être dans une base
              ATCSender = Champ[0][3:len(Champ[0])-3].split('/')[0]
              ATCReceiver = Champ[0][3:len(Champ[0])-3].split('/')[1]
              # Pour du LAM, champ supplémentaire à voir
              
              Indicatif = Champ[1].split("/")[0] #Des chiffres et des lettres ?
              if Champ[1].split("/")[1][0] != 'A':                
                EcrireLog(FILE(),LINE(),"Le Mode SSR est invalide")
              
              CodeSSR = Champ[1].split("/")[1][1:] 
              if not re.search("[0-7]{4}",CodeSSR,re.MULTILINE):
                EcrireLog(FILE(),LINE(),"Le Code SSR est invalide")
              
              AeroportDepart = Champ[2]
              if IsAnAirport(str(AeroportDepart))==1: # Base Airport n'est pas à jour
                EcrireLog(FILE(),LINE(),"L'aéroport de départ "+AeroportDepart+" n'est pas valide")
              
              PointCoordination = Champ[3].split('/')[0]
              # HeureCoordination HH:MM avec H et M sont des chiffres
              HeureCoordination = str(Champ[3].split('/')[1][0:2])+"H"+str(Champ[3].split('/')[1][2:4])
              FLCoordination = Champ[3].split('/')[1][5:8] # 3 chiffres
              
              AeroportArrivee = Champ[4]
              if IsAnAirport(str(AeroportArrivee))==1:
                EcrireLog(FILE(),LINE(),"L'aéroport d'arrivée "+AeroportArrivee+" n'est pas valide")

              # Numero du sous-champ facultatif du champ 22 : Champ[5].split('/')[0]
              TypeAeronef = Champ[5].split('/')[1]
              TurbulenceSillage = Champ[5].split('/')[2][0]

              # Numero du sous-champ facultatif du champ 22 : Champ[6].split('/')[0]
              #TypeVol = Champ[6].split('/')[1]
              
              
              Messages.append(Buffer + Message_ + "\n\n")          
        
          Donnees = Donnees[LongBloc:]   
    
    InsererTexte(ZoneTexte,' '.join(Messages)+"\n")      
    IdFichier.close()
    interval = time.time() - start_time  
    print 'Total time in seconds:', interval 
     


# ###############################################################
# ExtraireEnTete
# Extraire l'en-tête du fichier
# En entrée : Le nom du fichier
# En sortie : Un dictionnaire contenant les informations 
# ###############################################################

def ExtraireEnTete(NomFichier):

  # Ouverture du fichier
  try:
    IdFichier = open(NomFichier,"rb")
  except: 
    EcrireLog(FILE(),LINE(),"Ouverture de "+NomFichier+" impossible")
  
  try:
    Donnees=IdFichier.read(LONG_BUFFER)
  except: 
    EcrireLog(FILE(),LINE(),"Lecture de "+NomFichier+" impossible")
  
  try:
    IdFichier.close()
  except:
    EcrireLog(FILE(),LINE(),"Fermeture de "+NomFichier+" impossible") 

  # Extraction de l'en-tête du fichier
  [Day,Month,Year] = ExtraireDate(Donnees)
  
  # La Date sous forme Jour/Mois/Annee
  DateConvenable = str(Day)+'/'+str(Month)+'/'+str(Year)
      
  EnTeteFichier = Donnees[0:LONG_HEAD_BUFFER] 
      
  # Nombre d'activation par les librairies MOD_C MOD_E
  NbActivation = ord(EnTeteFichier[4:5])*256 + ord(EnTeteFichier[5:6])
      
  #Numéro du bloc Fichier
  NumBlocFic = ord(EnTeteFichier[6:7])*256 + ord(EnTeteFichier[7:8])
   
  #Numéro Heure Journée
  Heure = ord(EnTeteFichier[8:9])*256 + ord(EnTeteFichier[9:10])

  # Nombre de pas de 100 ms écoulés dans l'heure
  NbMillisec = ord(EnTeteFichier[10:11])*256 + ord(EnTeteFichier[11:12])
  NbSec = NbMillisec/10
  Minutes = NbSec/60
  Secondes = NbSec%60      

  # Le type d'enregistrement en EBCDIC (Extended Binary Coded Decimal Interchange Code)
  TypeEnreg=EnTeteFichier[12:20].decode('EBCDIC-CP-BE').encode('ascii')

  if TypeEnreg.rstrip() != "OLDI" :
    EcrireLog(FILE(),LINE(),"Ce type de fichier n'est pas pris en charge par l'application")
  DonneesUtiles = Donnees[LONG_HEAD_BUFFER:]
                
  # Debut d'analyse des blocs contenus dans le Bufferfer 
  EnteteBloc = DonneesUtiles[:LONG_HEAD_BLOC] 
  LongBloc = (ord(EnteteBloc[3])*2) + 4
  
  return {"Date":DateConvenable,"NumeroActivation":NbActivation,"NumeroBloc":NumBlocFic,"Heure":Heure,"Minutes":Minutes,"Secondes":Secondes,"Type":TypeEnreg}
 

