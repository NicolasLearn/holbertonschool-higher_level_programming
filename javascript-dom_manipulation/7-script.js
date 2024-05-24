// Fetch the movie titles from the API
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => {
    // Check if the request was successful
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    // Parse the JSON response
    return response.json();
  })
  .then(data => {
    // Access the list of movies from the response data
    const movies = data.results;
    // Select the HTML element ul with id "list_movies"
    const listElement = document.getElementById('list_movies');
    // Loop through each movie and add its title to the list
    movies.forEach(movie => {
      // Create a new li element
      const listItem = document.createElement('li');
      // Set the text content of the li element to the movie title
      listItem.textContent = movie.title;
      // Append the li element to the ul element
      listElement.appendChild(listItem);
    });
  })
  .catch(error => {
    // Handle any errors that occurred during the fetch operation
    console.error('There was a problem with the fetch operation:', error);
  });
