from functions import *
from style.style import css
connexion = sqlite3.connect('base_vin.db')
curseur = connexion.cursor()

def affich_formulaire():
    css()
    create_header('Ajout')
    print("""
               <form action = "/new_wine.py" method = "post">
                   <fieldset>
                       <legend>Vins</legend>
                       <p>
                           <label for = "name">Nom</label>
                           <input type = "text" id = "name" name = "name">
                           <label for = "color">Auteur</label>
                           <input type = "text" id = "color" name = "color">
                           <label for = "number">Nombre</label>
                           <input type = "number" id = "number" name = "number">
                           <select name="appelation" id="appelation">
                                <option value="default">Choisissez une appelation</option>
                                """)

    for appelation in get_appelations(): print("<option value=" + str(appelation[0]) + ">", appelation[1], "</option>")
    print("""
                           </select>
                       </p>
                       <p>


                           <button type="submit">Compléter la base</button>
                   </fieldset>
               </form>
               
               <form action = "/new_appelation.py" method = "post">
                   <fieldset>
                       <legend>Appelations</legend>
                       <p>
                           <label for = "name">Nom</label>
                           <input type = "text" id = "name" name = "name">
                           <label for = "country">Pays</label>
                           <input type = "text" id = "country" name = "country">
                           <label for = "region">Région</label>
                           <input type = "text" id = "region" name = "region">
                       </p>
                       <p>
                           <button type="submit">Compléter la base</button>
                   </fieldset>
               </form>
               
           </body>
       </html>""")

affich_formulaire()
