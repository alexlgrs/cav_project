import sqlite3
import style 

def affich_base():
    style.css()
    print("""
        <!DOCTYPE html>
        <html lang ="fr">
            <head>
                <meta charset="utf-8"/>
            </head>
            <body>""")
 
    # connexion à la base 
    connexion = sqlite3.connect('base_livres.db') 
    curseur = connexion.cursor() 
    # sélection de tous les attributs de la table illustrateur 
    curseur.execute("""SELECT * FROM Livres""")
    print("<h1>Contenu de la table Livres</h1>") # titre 
    print("<table border = '1'>") # tableau 
    print("<tr><th colspan = '4'> Livres </th></tr>") # nom de la table 
    print("<tr><th>Identifiant</th><th>Titre</th><th>Auteur</th></tr>") # en-tête 
     
    for tuple in curseur: # affichage des tuples 
        print("<tr>") 
        liste = list(tuple) 
        for champ in liste: 
            print("<td>" + str(champ) + "</td>") 
        print("</tr>") 
    print("</table>") 
    print("</body> </html>") 
     
    connexion.close() 
 
affich_base()