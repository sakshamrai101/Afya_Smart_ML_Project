const ratingOptions = `
            <option value="1">1 (Poor)</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5 (Excellent)</option>
        `;

        // Get all the dropdown elements and populate them with the rating options
for (let i = 1; i <= 4; i++) {
    const criteriaDropdown = document.querySelector('#criteria' + i);
    if (criteriaDropdown) {
        criteriaDropdown.innerHTML = ratingOptions;
    }
}