// Define the URL for the operations page
const operationsURL = doneURL; // Accessing the doneURL variable defined in the HTML

// Add event listener to the "Done" button
document.getElementById('doneButton').addEventListener('click', function() {
    // Redirect to the operations page using the variable
    window.location.href = operationsURL;
    event.preventDefault(); // Prevent default form submission
    return; // Exit the function early
});
