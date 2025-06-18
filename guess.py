from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'secret123'  # required for sessions

@app.route("/", methods=["GET", "POST"])
def index():
    if "number" not in session:
        session["number"] = random.randint(1, 100)
        session["attempts"] = 0

    message = ""
    won = False

    if request.method == "POST":
        try:
            guess = int(request.form["guess"])
            target = session["number"]

            if guess == target:
                won = True
                message = f"🎉 Congratulations! You guessed it in {session['attempts']} tries!"
                session.pop("number")
                session.pop("attempts")
            else:
                session["attempts"] += 1
                if guess < target:
                    message = "Too Low! 👎🏻"
                else:
                    message = "Too High! 👍🏻"
        except ValueError:
            message = "Please enter a valid number."

    return render_template("guess.html", message=message, won=won)

if __name__ == "__main__":
    app.run(debug=True,port=5004)
