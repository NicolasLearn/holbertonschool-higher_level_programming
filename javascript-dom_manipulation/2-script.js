// Select the element with id "red_header" using document.querySelector
const redHeader = document.querySelector('#red_header');

// Add a click event listener to the element
redHeader.addEventListener('click', function() {
  // Select the header element using document.querySelector
  // Add the class "red" to the header element
  document.querySelector('header').classList.add('red');
});
