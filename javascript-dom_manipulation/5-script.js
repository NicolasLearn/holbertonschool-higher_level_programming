// Select the element with id "update_header"
const updateHeader = document.querySelector('#update_header');

// Add a click event listener to the element
updateHeader.addEventListener('click', function() {
  // Select the header element
  const header = document.querySelector('header');

  // Modify the text of the header
  header.textContent = "New Header!!!"
});