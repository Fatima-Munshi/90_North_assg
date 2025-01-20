# 90_North_assg
# Frontend Development Project -- Assignment 1
This is a frontend development project showcasing a responsive web page with a navigation bar, left menu, main content area, and a right panel. The layout adjusts based on the screen size to ensure a good user experience on both desktop and mobile devices. 
## Files: 
  `index.html`: The main HTML file for the web page. 
  - `style.css`: The CSS file for styling the web page.
  - `script.js`: The JavaScript file for adding interactive functionality.
 ## Features: 
 Responsive Design: The layout adjusts based on the screen size.
Navigation Bar: Links to different sections of the page. - Collapsible Left Menu: The left menu can be toggled on and off.
Main Content Area: The main content of the page.
Right Panel: Additional information or links can be placed here. -Footer: A simple footer with reserved rights notice. 
## How to Use 
1. Clone the repository: ```bash git clone https://github.com/Fatima-Munshi/90_NORTH_assg.git
2. Open the project: Navigate to the project directory and open the `index.html` file in your browser to view the web page.
## Code Overview 
HTML: The structure of the web page is defined in the `index.html` file.
CSS: The styling is handled by the `style.css` file, which includes responsive design techniques.
JavaScript: The `script.js` file contains functions to toggle the left menu and adjust the page scale based on the screen size.

# DJANGO -- Assignment 2: Chat App


# AWS -- Assignment 3
This repository contains two AWS Lambda functions: one to add two numbers and another to store a document or PDF file in an S3 bucket.
## AddNumbersLambda
This Lambda function takes two numbers as input and returns their sum.
Usage: To invoke this function, you need to pass a JSON object with the keys number1 and number2. The function will return a JSON object with the key result.
## StoreDocumentLambda
This Lambda function takes a document or PDF file as input and stores it in an S3 bucket.
Usage: To invoke this function, you need to pass a JSON object with the key fileContent, which should be the content of the file you want to upload. The function will return a success or failure message.
