document.addEventListener("DOMContentLoaded", function () {
    var form = document.getElementById("rechercheForm");
    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Empêche l'envoi du formulaire

        // Simulation de données récupérées du formulaire (remplacez cela par votre logique de récupération de données côté serveur)
        var data = {
            // Exemple de données récupérées du formulaire
            nom: "Doe",
            prenom: "John",
            date_naissance: "01/01/1990",
            lieu_naissance: "Paris",
            sexe: "Masculin",
            departement: "RH",
            fonction: "Manager",
            niveau_etude: "Bac+5",
            diplome: "Master",
            numero_telephone: "0123456789",
            adresse_mail: "john.doe@example.com",
            statut_matrimonial: "Célibataire",
            date_embauche: "01/01/2010",
            nombre_enfants: 0,
            contrat: ["CDI", "CDD"]
        };

        afficherResultats(data); // Appel de la fonction pour afficher les résultats
    });
});

function afficherResultats(data) {
    var resultatsDiv = document.getElementById("resultats");
    resultatsDiv.innerHTML = ""; // Efface les résultats précédents

    // Création du tableau HTML pour afficher les données
    var table = document.createElement("table");
    var tbody = document.createElement("tbody");

    for (var key in data) {
        var tr = document.createElement("tr");
        var th = document.createElement("th");
        var td = document.createElement("td");

        th.textContent = key.toUpperCase(); // Affiche le nom du champ en majuscule
        td.textContent = data[key]; // Affiche la valeur correspondante

        tr.appendChild(th);
        tr.appendChild(td);
        tbody.appendChild(tr);
    }

    table.appendChild(tbody);
    resultatsDiv.appendChild(table);
}
