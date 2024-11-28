from flask import Flask, redirect, render_template, request, session, url_for
from function import (
    random_card,
    random_card_name,
    card_description,
    card_meaning,
    get_card_image,
)

app = Flask(__name__, template_folder="templates")

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        question = request.form["question"]
        number = int(request.form["number"])

        result = random_card(number)
        cards = random_card_name(result)
        images = get_card_image(cards)
        description = card_description(result, cards)
        meaning = card_meaning(result, cards)

        session["cards"] = cards
        session["images"] = images
        session["description"] = description
        session["meaning"] = meaning
        session["name"] = name
        session["question"] = question
        return redirect(url_for("pickcards"))
    return render_template("index.html")


@app.route("/pickcards", methods=["GET", "POST"])
def pickcards():

    cards = session.get("cards")
    images = session.get("images")
    description = session.get("description")
    meaning = session.get("meaning")

    name = session.get("name")
    question = session.get("question")

    return render_template(
        "pickcards.html",
        cards=cards,
        descriptions=description,
        meanings=meaning,
        images=images,
        name=name,
        question=question,
    )


if __name__ == "__main__":
    app.run(debug=True)
