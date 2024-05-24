// Select the element with id "toggleHeader" using document.querySelector
const toggleHeader = document.querySelector('#toggle_header');

// Add a click event listener to the element
toggleHeader.addEventListener('click', function() {
  // Select the element header
  const header = document.querySelector('header');

  // Use the toggle() function to switch between "red" and "green" classes
  header.classList.toggle('red');
  header.classList.toggle('green');
});

