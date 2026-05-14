from flask import Flask, render_template, request
import pickle
import os
import csv

app = Flask(__name__)

# Load model & vectorizer
MODEL_PATH = "model.pkl"
VECT_PATH = "vectorizer.pkl"

if not os.path.exists(MODEL_PATH) or not os.path.exists(VECT_PATH):
    raise FileNotFoundError("model.pkl or vectorizer.pkl not found. Run train_model.py first.")

model = pickle.load(open(MODEL_PATH, "rb"))
vectorizer = pickle.load(open(VECT_PATH, "rb"))


# Function to read prediction history
def get_history():
    history = []

    if os.path.exists("history.csv"):
        with open("history.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)

            for row in reader:
                history.append(row)

    return history[::-1]


@app.route("/", methods=["GET"])
def home():
    return render_template(
        "index.html",
        prediction=None,
        user_text="",
        history=get_history()
    )


@app.route("/predict", methods=["POST"])
def predict():
    text = request.form.get("news", "")

    # If empty input
    if text.strip() == "":
        return render_template(
            "index.html",
            prediction=None,
            user_text="",
            history=get_history()
        )

    # Prediction
    vector = vectorizer.transform([text])
    pred = model.predict(vector)[0]

    result = "FAKE NEWS ❌" if pred == 1 else "REAL NEWS ✔"

    # Save history into CSV
    with open("history.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([text, result])

    return render_template(
        "index.html",
        prediction=result,
        user_text=text,
        history=get_history()
    )


if __name__ == "__main__":
    app.run(debug=True)