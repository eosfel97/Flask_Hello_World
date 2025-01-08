from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return "<h2>Bonjour tout le monde !</h2><p>Pour accéder à vos exerices cliquez <a href='./exercices/'>Ici</a></p>"

@app.route('/exercices/')
def exercices():
    return render_template('exercices.html')
                                                                                                               
@app.route("/contact/")
def MaPremiereAPI():
    return render_template("contact.html")

@app.route('/calcul_carre/<int:val_user>')
def carre(val_user):
    return "<h2>Le carré de votre valeur est : </h2>" + str(val_user * val_user)

    #exo 4 et 5

 #@app.route('/somme/<int:valeur1>/<int:valeur2>')
#def somme(valeur1, valeur2):
 #   result = valeur1 + valeur2
  #  if result % 2 == 0:
   #     parity = "pair"
    #else:
     #   parity = "impair"
    #return f"""
    #    <h2>La somme de vos valeurs est : {result}</h2>
    #    <p>La somme est un nombre <strong>{parity}</strong>.</p>
    #"""

@app.route('/somme/<values>')
def somme_total(values):
    try:
        valeurs = list(map(int, values.split(',')))
        result = sum(valeurs)
    except ValueError:
        return "<h2>Veuillez entrer uniquement des nombres entiers séparés par des virgules.</h2>"

    return f"""
        <h2>La somme de vos valeurs est : {result}</h2>
        <p>Les valeurs saisies sont : {', '.join(map(str, valeurs))}</p>
    """

@app.route('/max/<values>')
def max_value(values):
    try:
        valeurs = list(map(int, values.split(',')))
        max_val = max(valeurs) 
    except ValueError:
        return "<h2>Veuillez entrer uniquement des nombres entiers séparés par des virgules.</h2>"

    return f"""
        <h2>La valeur maximale saisie est : {max_val}</h2>
        <p>Les valeurs saisies sont : {', '.join(map(str, valeurs))}</p>
    """
@app.route('/cv')
def cv():
    return render_template('cv.html')

@app.route('/page1')
def page1():
    return render_template('page1.html')

@app.route('/actualite')
def actualite():
    return render_template('actualite.html')


@app.route('/outilsjs')
def outilsjs():
    return render_template('Outils_JS.html')


@app.route('/Biblo')
def outilsjs():
    return render_template('Biblo_Images.html')


if __name__ == "__main__":
  app.run(debug=True)