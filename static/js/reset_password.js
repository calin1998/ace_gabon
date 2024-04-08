document.getElementById('resetPasswordForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var email = document.getElementById('email').value;
    // Envoyer l'email de réinitialisation du mot de passe à l'adresse email spécifiée
    // Rediriger l'utilisateur vers la page de confirmation de réinitialisation du mot de passe
    window.location.href = "/reset_password_confirmation?email=" + email;
});
