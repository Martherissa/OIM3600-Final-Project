from flask import Flask, redirect, render_template, request, session, url_for
import os
from flask_session import Session
import json

from function import (
    random_card,
    random_card_name,
    card_description,
    card_meaning,
    get_card_image,
)

# Specify the folder where the templates are stored
app = Flask(__name__, template_folder="templates")

# Set app secret key to make the session secure
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Data storage setup for the session
# The session data will be stored in the user_data folder
# The session data will be stored in a file called session.json
# The session is permanent, meaning that all past data will be stored even after the browser is closed
# The session data will be signed (encrypted) for security
# The session key prefix is session: (not necessary but added for clarity)
app.config["SESSION_TYPE"] = "filesystem"
session_dir = os.path.join(app.root_path, "user_data")
if not os.path.exists(session_dir):
    os.makedirs(session_dir)
app.config["SESSION_FILE_DIR"] = session_dir
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_USE_SIGNER"] = True
app.config["SESSION_KEY_PREFIX"] = "session:"


# Store the session data in a json file (the code is generated with help of the Flask documentation and ChatGPT)
@app.after_request
def store_session(response):
    session_data = {key: session[key] for key in session.keys()}
    with open(os.path.join(app.config["SESSION_FILE_DIR"], "session.json"), "w") as f:
        json.dump(session_data, f, indent=4)
    return response


# Initialize the session so that the session data is stored in the json file
Session(app)


# The main page of the app
# The user can input their name, question, and the number of cards they want to draw
# The user can also ask another question or logout (meaning they can choose another username)
@app.route("/", methods=["GET", "POST"])
def index():
    # Request method of POST means that the user has filled out the form and submitted it
    if request.method == "POST":
        # If the user has already input their name, the name will be stored in the session
        # Else they are asked to input their name
        if "name" in session:
            name = session.get("name")
        else:
            name = request.form["name"]

        # Get the question and the number of cards the user wants to draw
        # Number is converted to an integer
        question = request.form["question"]
        number = int(request.form["number"])

        # Get the random cards, their names, images, description, and meaning from predefined functions
        result = random_card(number)
        cards = random_card_name(result)
        images = get_card_image(cards)
        description = card_description(result, cards)
        meaning = card_meaning(result, cards)

        # Store the data in the session
        session["name"] = name
        session["question"] = question
        session["number"] = number
        session["cards"] = cards
        session["images"] = images
        session["description"] = description
        session["meaning"] = meaning

        # Redirect to the pick_cards page to display results
        return redirect(url_for("pick_cards"))
    # render index page first
    return render_template("index.html")


# This is the page where cards and results are displayed
@app.route("/pickcards", methods=["GET", "POST"])
def pick_cards():
    # Get the data from the stored session
    cards = session.get("cards")
    images = session.get("images")
    description = session.get("description")
    meaning = session.get("meaning")
    name = session.get("name")
    question = session.get("question")

    # Store past data in the dataset as past questions (easier to identify when managing database)
    past_questions = session.get("past_questions", [])
    past_questions.append(
        {
            "name": session.get("name"),
            "question": session.get("question"),
            "number": session.get("number"),
            "cards": session.get("cards"),
            "images": session.get("images"),
            "description": session.get("description"),
            "meaning": session.get("meaning"),
        }
    )
    session["past_questions"] = past_questions

    # Render the pickcards page with the data
    return render_template(
        "pickcards.html",
        cards=cards,
        descriptions=description,
        meanings=meaning,
        images=images,
        name=name,
        question=question,
    )


# This page allow the user to ask another question
@app.route("/ask_another", methods=["GET"])
def ask_another():

    # Store past data in the dataset
    past_questions = session.get("past_questions", [])
    past_questions.append(
        {
            "name": session.get("name"),
            "question": session.get("question"),
            "number": session.get("number"),
            "cards": session.get("cards"),
            "images": session.get("images"),
            "description": session.get("description"),
            "meaning": session.get("meaning"),
        }
    )
    session["past_questions"] = past_questions

    # Redirect to the index page to ask another question
    return redirect(url_for("index"))


# This page allow the user to logout (change username)
@app.route("/logout", methods=["GET"])
def logout():
    # Store past data in the dataset
    past_questions = session.get("past_questions", [])

    # Clear the current session data
    session.clear()

    # Store the past data in the session so the record is not lost
    session["past_questions"] = past_questions

    # Redirect to the index page to ask another question
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
