from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    data = request.json
    user_choice = data['choice']
    computer_choice = random.choice(["rock", "paper", "scissors"])
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result = "You win!"
    else:
        result = "You lose!"
    return jsonify({'result': result, 'computer_choice': computer_choice})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

