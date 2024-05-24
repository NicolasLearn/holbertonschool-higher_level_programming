// Fetch the character name from the API
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => {
    // Check if the request was successful
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    // Parse the JSON response
    return response.json();
  })
  .then(data => {
    // Access the character name from the response data
    const characterName = data.name;
    // Select the HTML element with id "character"
    const characterElement = document.getElementById('character');
    // Set the character name as the inner text of the selected element
    characterElement.innerText = characterName;
  })
  .catch(error => {
    // Handle any errors that occurred during the fetch operation
    console.error('There was a problem with the fetch operation:', error);
});
