import sqlite3
base_vin = sqlite3.connect('database/base_vin.db')

curseur = base_vin.cursor()


def get_appelations():
    """
    Retourne une liste de toutes les appelations
    """
    
    curseur.execute("""SELECT * FROM appelations""")
    return curseur
    
    
def insert(table, data):
    if(table == "wines"):
        curseur.execute("""INSERT INTO wines(name, color, appelation, count) VALUES(?, ?, ?, ?)""", data)
        
    elif(table == "appelations"):
        curseur.execute("""INSERT INTO appelations(name, country, region) VALUES(?, ?, ?)""", data)
        
    
    base_vin.commit() 
    

def navbar():
    print("""
        <div id = 'navbar'>nav</div>
    """)

def create_header(title):
    print("""
       <!DOCTYPE html>
       <html lang ="fr">
           <head>
               <meta charset="utf-8"/>
               <title>""")
    print(title)
    print("""</title>
           </head>
           <body>
           
           <div id = "navbar">
                <div id = "project-name">Wine Stock</div>
                <div class = "navbar-item" id = "edit-button"><a href = "home.py">GESTION</a></div>
                <div class = "navbar-item"><a href = "home.py">LISTE</a></div>
                <div class = "navbar-item"><a href = "new.py">AJOUT</a></div>
           </div>
           """)

def get_image(color):
    return "res/" + color + "_default.png"

def get_appelation(id):
    curseur.execute("SELECT * FROM appelations WHERE id = '" + str(id) + "'")
    for appelation in curseur:
        return appelation