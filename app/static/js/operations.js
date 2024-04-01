// Create buttons
const button1 = document.createElement('button');
button1.textContent = 'text1';

const button2 = document.createElement('button');
button2.textContent = 'text2';

const button3 = document.createElement('button');
button3.textContent = 'text3';

// Apply styles to the buttons
const buttonStyles = `
    display: block;
    margin: 20px auto; /* Add margin to separate buttons */
    font-size: 24px;
    padding: 15px 30px;
    background-color: orange;
    color: white;
    border: none;
    border-radius: 10px;
    cursor: pointer;
`;

button1.style.cssText = buttonStyles;
button2.style.cssText = buttonStyles;
button3.style.cssText = buttonStyles;

// Append buttons to the document body or any other container element
document.body.appendChild(button1);
document.body.appendChild(button2);
document.body.appendChild(button3);
