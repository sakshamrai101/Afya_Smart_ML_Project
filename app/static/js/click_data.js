// JavaScript for bone fracture form submission
document.getElementById('boneFractureForm').addEventListener('submit', function(event) {
    // Prevent the default form submission behavior
    event.preventDefault();

    // Log to console to check if event listener is triggered
    console.log('Bone fracture form submitted');

    // Submit the form
    this.submit();
});

// JavaScript for oral surgery form submission
document.getElementById('oralSurgeryForm').addEventListener('submit', function(event) {
    // Prevent the default form submission behavior
    event.preventDefault();

    // Log to console to check if event listener is triggered
    console.log('Oral surgery form submitted');

    // Submit the form
    this.submit();
});
