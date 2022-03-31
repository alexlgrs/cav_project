import cgi  
from new import *
import sqlite3 
 
# récupération des données du formulaire
formulaire = cgi.FieldStorage()
name = formulaire.getvalue("name") 
country = formulaire.getvalue("country") 
region = formulaire.getvalue("region") 
 
# insertion des données du formulaire dans la base
connexion = sqlite3.connect('database/base_vin.db') 
curseur = connexion.cursor() 
 
data = (name, country, region) 
curseur.execute("""INSERT INTO appelations(name, country, region) VALUES(?, ?, ?)""", data) 
 
connexion.commit()

affich_formulaire()