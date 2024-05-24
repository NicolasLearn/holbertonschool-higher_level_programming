// Utilisation de fetch pour récupérer la valeur de "hello" depuis l'URL
fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then(response => {
    // Vérification de la réussite de la requête
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    // Extraction du texte de la réponse
    return response.text();
  })
  .then(data => {
    // Accès à la valeur de "hello" depuis la réponse
    const helloValue = data;
    // Sélection de l'élément HTML avec l'identifiant "hello"
    const helloElement = document.getElementById('hello');
    // Attribution de la valeur de "hello" comme contenu textuel de l'élément
    helloElement.textContent = helloValue;
  })
  .catch(error => {
    // Gestion des erreurs de la requête Fetch
    console.error('There was a problem with the fetch operation:', error);
  });
