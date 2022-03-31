import sqlite3
from style.style import *
from functions import *
import cgi
from random import randint

connexion = sqlite3.connect('database/base_vin.db')
curseur = connexion.cursor()

formulaire = cgi.FieldStorage()
colorInput = formulaire.getvalue("color")
appelationInput = formulaire.getvalue("appelation")
nameInput = formulaire.getvalue("name")


def home():
    css()
    create_header('Acceuil')

    print("""
    <!DOCTYPE html>
        <html lang ="fr">
            <head>
                <meta charset="utf-8"/>
                <title>Page D'acceuil</title>
            </head>
            <body>
                <div id = "shop-filters-screen">
                <div id = "filters-screen">
                    <form action = "/home.py" id ="filters-form">
                        <select name = "color" selected = "all" class = "filter-form-input">
                            <option value = "all">Toutes</option>
                            <option value = "rouge">Rouge</option>
                            <option value = "blanc">Blanc</option>
                            <option value = "rosé">Rosé</option>
                        </select>

                        <select name = "appelation" selected = "all" class = "filter-form-input">
                            <option value = "all">Toutes</option>
                            """)

    for appelation in get_appelations(): print("<option value=" + str(appelation[0]) + ">", appelation[1], "</option>")

    print("""
                        </select>
                        <input type = "text" class = "filter-form-input" name = "name">
                        <input type = "submit" class = "filter-form-input" id = "filter-form-submit" name = "submit" value = "TRIER">

                    </form>

                </div>
                <div id = "shop-screen">
    """)

    # TRAITEMENT TRI
    request = "SELECT * FROM wines "

    if (colorInput != None):
        if (colorInput in ["rouge", "blanc", "rosé"]):
            if ("WHERE" in request):
                request += " AND color = '" + colorInput + "'"
            else:
                request += "WHERE color = '" + colorInput + "'"

    if (appelationInput != None):
        if (appelationInput != "all"):
            if ("WHERE" in request):
                request += " AND appelation = '" + str(appelationInput) + "'"
            else:
                request += "WHERE appelation = '" + str(appelationInput) + "'"

    if (nameInput != None):
        if ("WHERE" in request):
            request += "AND name LIKE '" + str(nameInput) + "%'"
        else:
            request += "WHERE name LIKE '" + str(nameInput) + "%'"

    # print("<p>" + str(request) + "</p><br>")

    wines = curseur.execute(request)
    for wine in wines:
        print("""
                    <div class = "shop-item">
                        <img class = "shop-item-image" src = '""" + str(get_image(wine[2])) + """'>
                        <p class = "shop-item-name">""" + wine[1].upper() + """</p>
                        <p class = "shop-item-appelation">""" + str(get_appelation(wine[3])[1]).upper() + """</p>
                        <div class = "shop-item-informations-button">INFORMATIONS</div>
                    </div>        
        """)
    #
    print("""
                </div>
                </div>
            </body>
        </html>""")

    connexion.close()


home()

