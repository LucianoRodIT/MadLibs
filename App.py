from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Get form data from request
        name = request.form.get("name")
        noun1 = request.form.get("noun1")
        noun2 = request.form.get("noun2")
        noun3 = request.form.get("noun3")
        plural_noun = request.form.get("pluralNoun")
        adjective1 = request.form.get("adjective1")
        adjective2 = request.form.get("adjective2")
        adjective3 = request.form.get("adjective3")
        adjective4 = request.form.get("adjective4")
        animal = request.form.get("animal")
        bird = request.form.get("bird")
        feeling1 = request.form.get("feeling1")
        feeling2 = request.form.get("feeling2")
        family_member = request.form.get("familyMember")

        # Generate Madlibs story using form data
        story = f"Title: The Adventure of {name}'s {noun1}\n\n"
        story += f"Once upon a time, {name} decided to go on an adventure. Armed with only a {adjective1} {noun2} and a sense of curiosity, {name} set out into the {adjective2} wilderness.\n\n"
        story += f"As {name} journeyed through the {adjective3} forest, they encountered a {adjective4} creature. It had the body of a {animal} but the wings of a {bird}. {name} was {feeling1} at first, but then realized the creature was friendly.\n\n"
        story += f"The creature led {name} to a hidden {noun3}, where they found a treasure chest filled with {plural_noun}. {name} couldn't believe their luck! They decided to share the treasure with their {family_member} back home.\n\n"
        story += f"With their newfound riches, {name} returned home feeling {feeling2}. They knew that no matter where their adventures took them, they would always cherish the memories of their journey."

        # Return JSON response with form data and generated story
        return jsonify({"form_data": request.form, "story": story})

    # Render the template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
