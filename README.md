# 90_North_assg
# Frontend Development Project -- Assignment 1
This is a frontend development project showcasing a responsive web page with a navigation bar, left menu, main content area, and a right panel. The layout adjusts based on the screen size to ensure a good user experience on both desktop and mobile devices. 
## Files: 
  -`index.html`: The main HTML file for the web page. 
  - `style.css`: The CSS file for styling the web page.
  - `script.js`: The JavaScript file for adding interactive functionality.
 ## Features: 
 - Responsive Design: The layout adjusts based on the screen size.
- Navigation Bar: Links to different sections of the page. - Collapsible Left Menu: The left menu can be toggled on and off.
- Main Content Area: The main content of the page.
- Right Panel: Additional information or links can be placed here. -Footer: A simple footer with reserved rights notice. 
## How to Use 
1. Clone the repository: ```bash git clone https://github.com/Fatima-Munshi/90_North_assg.git
2. Open the project: Navigate to the project directory and open the `index.html` file in your browser to view the web page.
## Code Overview 
HTML: The structure of the web page is defined in the `index.html` file.
CSS: The styling is handled by the `style.css` file, which includes responsive design techniques.
JavaScript: The `script.js` file contains functions to toggle the left menu and adjust the page scale based on the screen size.

# DJANGO -- Assignment 2: Chat App
# ChatApp

## Introduction
ChatApp is a real-time messaging application built with Django and WebSockets. It allows users to create accounts, log in, and communicate with each other through text messages.

## Features
- User registration and authentication
- Real-time messaging using WebSockets
- User profile management
- Chat rooms for group conversations

## Installation
Follow these steps to get the ChatApp up and running on your local machine.

### Prerequisites
- Python 3.x
- Django
- Django Channels
- Redis (for WebSocket support)

### Steps
1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/chatapp.git
    cd chatapp
    ```

2. **Create and activate a virtual environment**:
    - On Windows:
      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```
    - On Mac/Linux:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    ```bash
    python manage.py migrate
    ```

5. **Run the Redis server**:
    ```bash
    redis-server
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

7. **Access the application**:
    Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage
1. **Register**: Create a new user account.
2. **Log in**: Log in with your credentials.
3. **Join a chat room**: Join an existing chat room or create a new one.
4. **Start chatting**: Send and receive messages in real-time.

## Acknowledgements
- Django Documentation
- Django Channels Documentation

# AWS -- Assignment 3
This repository contains two AWS Lambda functions: one to add two numbers and another to store a document or PDF file in an S3 bucket.
## AddNumbersLambda
This Lambda function takes two numbers as input and returns their sum.
Usage: To invoke this function, you need to pass a JSON object with the keys number1 and number2. The function will return a JSON object with the key result.
## StoreDocumentLambda
This Lambda function takes a document or PDF file as input and stores it in an S3 bucket.
Usage: To invoke this function, you need to pass a JSON object with the key fileContent, which should be the content of the file you want to upload. The function will return a success or failure message.
