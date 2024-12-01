from flask import Flask, flash, redirect, render_template, request, session, url_for
from function import (
    random_card,
    random_card_name,
    card_description,
    card_meaning,
    get_card_image,
)

app = Flask(__name__, template_folder="templates")

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

ERROR_MESSAGES = {
    "invalid_number": "Please choose a number between 1 and 6.",
    "fetch_error": "Failed to fetch card data. Please try again.",
    "session_expired": "Session expired. Please start again from the homepage.",
}


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        question = request.form.get("question")
        number = request.form.get("number")

        try:
            number = int(number)
            if number < 1 or number > 6:
                raise ValueError("Invalid number of cards.")
        except ValueError:
            flash(ERROR_MESSAGES["invalid_number"], "error")
            return redirect(url_for("index"))

        try:
            result = random_card(number)
            cards = random_card_name(result)
            images = get_card_image(cards)
            description = card_description(result, cards)
            meaning = card_meaning(result, cards)
        except Exception as e:
            flash(ERROR_MESSAGES["fetch_error"], "error")
            return redirect(url_for("index"))

        session["cards"] = cards
        session["images"] = images
        session["description"] = description
        session["meaning"] = meaning
        session["name"] = name
        session["question"] = question
        return redirect(url_for("pickcards"))


@app.route("/pickcards", methods=["GET", "POST"])
def pickcards():

    if not session.get("cards"):
        flash(ERROR_MESSAGES["session_expired"], "error")
        return redirect(url_for("index"))

    data = {
        "cards": session.get("cards"),
        "images": session.get("images"),
        "description": session.get("description"),
        "meaning": session.get("meaning"),
        "name": session.get("name"),
        "question": session.get("question"),
    }

    return render_template("pickcards.html", **data)


if __name__ == "__main__":
    app.run(debug=True)
