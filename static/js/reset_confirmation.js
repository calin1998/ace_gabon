document.getElementById('resetConfirmationForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var newPassword = document.getElementById('newPassword').value;
    var confirmPassword = document.getElementById('confirmPassword').value;
    // Valider les mots de passe
    if (newPassword !== confirmPassword) {
        alert("Les mots de passe ne correspondent pas.");
        return;
    }
    // Envoyer le nouveau mot de passe au serveur pour mise à jour
    // Afficher un message de confirmation ou rediriger l'utilisateur vers la page de connexion
});
