// Select the element with id "red_header" using document.querySelector
const redHeader = document.querySelector('#red_header');

// Add a click event listener to the element
redHeader.addEventListener('click', function() {
  // Select the header element using document.querySelector
  // Update the text color of the header element to red
  document.querySelector('header').style.color = '#FF0000';
});
