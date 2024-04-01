// Define the URL for the operations page
const ClickButton = ButtonID; // Accessing the doneURL variable defined in the HTML
const Form_New = FormID;

document.getElementById(Form_New).addEventListener('submit', function(event) {
    // Determine which button was clicked
    const clickedButtonId = event.submitter ? event.submitter.id : null;

    // Handle button clicks based on their IDs
    switch (clickedButtonId) {
        case ClickButton:
            // If button2 was clicked, allow the form submission
            break;
        case 'goToDashboardButton':
            // If the "Go to Dashboard" button was clicked, redirect to the dashboard page
            window.location.href = '/home'; // Replace '/dashboard' with the actual URL of your dashboard page
            event.preventDefault(); // Prevent default form submission
            break; // Prevent further execution of the function
        default:
            // For other buttons, prevent the default form submission behavior
            event.preventDefault();
            alert('This button is disabled or not yet implemented.');
    }
});
