import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

news = input("Enter news text: ")

vector = vectorizer.transform([news])
prediction = model.predict(vector)[0]

if prediction == 1:
    print("FAKE NEWS ❌")
else:
    print("REAL NEWS ✔")
