// section_buddy/report_generator/static/js/custom.js

// Set the top position value
const inputFieldWidth = '180px'
const topHeading = '50px'
const leftMargin = '50px'
const inputFieldDistance = '100px'

// Set styles using JavaScript
document.addEventListener('DOMContentLoaded', function () {
    const heading = document.querySelector('h1.main-title');
    const heightInput = document.getElementById('heightInput');
    const widthInput = document.getElementById('widthInput');
    const generateBtn = document.getElementById('generateBtn');

    heading.style.position = 'absolute';
    heading.style.top = topHeading;
    heading.style.left = leftMargin;
    heading.style.fontSize = '32px';
    heading.style.fontWeight = 'bold';
    heading.style.color = '#333';

    heightInput.style.position = 'absolute';
    heightInput.style.top = `calc(${topPosition} + ${someVerticalDistance})`;
    heightInput.style.left = leftMargin;
    heightInput.style.width = inputFieldWidth;

    widthInput.style.position = 'absolute';
    widthInput.style.top = `calc(${topPosition} + ${someVerticalDistance})`;
    widthInput.style.left = `calc(${leftMargin} + ${inputFieldWidth})`;
    widthInput.style.width = inputFieldWidth;

    generateBtn.style.position = 'absolute';
    generateBtn.style.top = `calc(${topPosition} + (${someVerticalDistance} * 1.5))`;
    generateBtn.style.left = topPosition;
    generateBtn.style.width = inputFieldWidth;
});
