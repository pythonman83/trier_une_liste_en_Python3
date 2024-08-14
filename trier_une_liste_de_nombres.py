print()

# Écrivez une fonction pour trier une liste de nombres.

from flask import Flask, render_template, request

app = Flask(__name__)

def trier_liste(liste):
    return sorted(liste)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultat = None
    if request.method == 'POST':
        liste_str = request.form['liste']
        # Nettoyer l'entrée pour enlever les espaces supplémentaires et séparer par des virgules
        liste_str = liste_str.replace(' ', ',').replace(',,', ',')
        try:
            liste = list(map(int, liste_str.split(',')))
            resultat = trier_liste(liste)
        except ValueError:
            resultat = "Erreur: Assurez-vous que tous les éléments de la liste sont des nombres entiers."
    return render_template('index.html', resultat=resultat)

if __name__ == '__main__':
    app.run(debug=True)


print()

# 