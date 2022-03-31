import cgi  
from new import *
import sqlite3 
 
# récupération des données du formulaire 
formulaire = cgi.FieldStorage()
name = formulaire.getvalue("name") 
color = formulaire.getvalue("color") 
appelation = formulaire.getvalue("appelation") 
number = formulaire.getvalue("number") 
 
# insertion des données du formulaire dans la base
connexion = sqlite3.connect('database/base_vin.db') 
curseur = connexion.cursor() 
 
data = (name, color, appelation, number) 
curseur.execute("""INSERT INTO wines(name, color, appelation, count) VALUES(?, ?, ?, ?)""", data) 
 
connexion.commit()
 
formulaire()
