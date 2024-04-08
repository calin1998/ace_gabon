from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_mysqldb import MySQL
import random
import string

app = Flask(__name__)

# Configuration de la base de données MySQL
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'calin0280'
app.config['MYSQL_DB'] = 'personnel_ace'  # Correction
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'  # Utilisation d'un curseur dict
mysql = MySQL(app)

# Clé secrète pour la gestion de session
app.secret_key = 'votre_clé_secrète'

# Page d'accueil
@app.route('/')
def index():
    return render_template('index.html')

# Page d'inscription
@app.route('/inscription', methods=['GET', 'POST'])
def inscription():
    if request.method == 'POST':
        # Récupération des données du formulaire d'inscription
        nom = request.form['nom']
        telephone = request.form['telephone']
        email = request.form['email']
        mot_de_passe = request.form['mot_de_passe']
        
        # Inscription dans la base de données
        cur = mysql.connection.cursor()
        try:
            cur.execute("INSERT INTO utilisateurs (nom, telephone, email, mot_de_passe) VALUES (%s, %s, %s, %s)", (nom, telephone, email, mot_de_passe))
            mysql.connection.commit()
            flash('Inscription réussie. Vous pouvez vous connecter maintenant.', 'success')
            return redirect(url_for('connexion'))
        except Exception as e:
            flash('Une erreur s\'est produite lors de l\'inscription. Veuillez réessayer.', 'danger')
            return redirect(url_for('inscription'))
        finally:
            cur.close()
    else:
        return render_template('inscription.html')

# Page de connexion
@app.route('/connexion', methods=['GET', 'POST'])
def connexion():
    if request.method == 'POST':
        # Récupération des données du formulaire de connexion
        email = request.form['email']
        mot_de_passe = request.form['mot_de_passe']
        
        # Vérification des informations d'identification dans la base de données
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM utilisateurs WHERE email = %s AND mot_de_passe = %s", (email, mot_de_passe))
        utilisateur = cur.fetchone()
        cur.close()
        
        if utilisateur:
            # Utilisateur trouvé, définir la session et rediriger vers la page d'accueil
            session['logged_in'] = True
            session['username'] = utilisateur['nom']  # Vous pouvez utiliser le nom d'utilisateur ou l'e-mail ici
            flash('Vous êtes connecté avec succès.', 'success')
            return redirect(url_for('accueil'))
        else:
            # Utilisateur non trouvé, afficher un message d'erreur
            flash('Adresse email ou mot de passe incorrect. Veuillez réessayer.', 'danger')
            return redirect(url_for('connexion'))
    else:
        return render_template('connexion.html')

# Page de réinitialisation du mot de passe
@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        email = request.form['email']
        # Vérifiez si l'email existe dans la base de données
        # Si oui, générez un jeton de réinitialisation
        token = ''.join(random.choices(string.ascii_letters + string.digits, k=30))
        # Enregistrez le jeton dans la base de données avec l'email
        # Envoyez l'email contenant le lien de réinitialisation
        # Redirigez l'utilisateur vers une page de confirmation
        flash('Un email de réinitialisation de mot de passe a été envoyé à votre adresse email.', 'info')
        return redirect(url_for('password_reset_confirmation'))
    return render_template('reset_password.html')

# Page de confirmation de réinitialisation du mot de passe
@app.route('/reset_password_confirmation', methods=['GET', 'POST'])
def password_reset_confirmation():
    # Implémentez cette fonctionnalité si nécessaire
    return render_template('password_reset_confirmation.html')

# Page d'accueil après connexion
@app.route('/accueil')
def accueil():
    return render_template('accueil.html')

# Page d'enregistrement du personnel
@app.route('/enregistrement')
def enregistrement():
    # Logique pour la page d'enregistrement du personnel
    return render_template('enregistrement.html')

# Page du personnel
@app.route('/personnel')
def personnel():
    return render_template('personnel.html')

# Page de recherche
@app.route('/recherche')
def recherche():
    return render_template('recherche.html')

# Route pour afficher les résultats de recherche
@app.route('/votre_route_de_recherche', methods=['POST'])
def votre_route_de_recherche():
    # Traitez ici la recherche et récupérez les résultats de la base de données
    # Redirigez l'utilisateur vers la page de résultats de recherche avec les résultats obtenus
    return redirect(url_for('resultats_recherche'))

# Page de résultats de recherche
@app.route('/resultats_recherche', methods=['GET', 'POST'])
def resultats_recherche():
    if request.method == 'POST':
        # Récupérer les valeurs des champs d'entrée du formulaire
        lieu_naissance_value = request.form.get('lieuNaissanceValue')
        sexe_value = request.form.get('sexeValue')
        departement_value = request.form.get('departementValue')
        fonction_value = request.form.get('fonctionValue')
        niveau_etude_value = request.form.get('niveauEtudeValue')
        diplome_value = request.form.get('diplomeValue')
        numero_telephone_value = request.form.get('numeroTelephoneValue')
        adresse_mail_value = request.form.get('adresseMailValue')
        statut_matrimonial_value = request.form.get('statutMatrimonialValue')
        date_embauche_value = request.form.get('dateEmbaucheValue')
        # Récupérer les autres valeurs de recherche de la même manière
        
        # Utiliser les valeurs récupérées pour construire la requête SQL et rechercher dans la base de données
        
        return render_template('resultats_recherche.html')
    else:
        # Logique pour gérer la méthode GET
        # Vous pouvez ajouter du code ici si nécessaire
        return render_template('resultats_recherche.html')


if __name__ == '__main__':
    app.run(debug=True)
