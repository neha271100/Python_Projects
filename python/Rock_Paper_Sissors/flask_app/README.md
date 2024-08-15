# Rock, Paper, Scissors Web App

This is a simple Rock, Paper, Scissors game implemented as a web application using Flask. The game allows the user to choose between Rock, Paper, or Scissors, and plays against the computer, which randomly selects one of the three options. The result of the game is displayed on the screen.

## How It Works

- The user selects Rock, Paper, or Scissors by clicking the corresponding button on the web page.
- The server receives the user's choice and randomly selects Rock, Paper, or Scissors for the computer.
- The server compares the user's choice and the computer's choice to determine the result (win, lose, or tie).
- The result, along with the computer's choice, is returned to the client and displayed on the web page.

## Technologies Used

- **Flask:** A micro web framework for Python that is used to create the backend of the application.
- **HTML/CSS:** The front-end is built using HTML for the structure and inline CSS for basic styling.
- **JavaScript:** Handles the interaction between the user and the server, making asynchronous requests using `fetch`.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/neha271100/rock-paper-scissors-flask.git
   cd rock-paper-scissors-flask

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate

3. **Install the required dependencies:**
   ```bash
      pip install Flask

4. **Run the application:**
   ```bash
        python app.py

5. **Open your web browser and go to:**
  http://127.0.0.1:8080
## Screenshots
Screenshots of the web app can be found in the screenshots folder. [Flask app Project](https://github.com/neha271100/Python_Projects/tree/main/python/Rock_Paper_Sissors/flask_app/screenshots)
