import pickle

model = pickle.load(open("emotion_model.pkl","rb"))
vectorizer = pickle.load(open("vectorizer.pkl","rb"))

while True:
    text = input("Enter text: ")
    vec = vectorizer.transform([text])
    prediction = model.predict(vec)

    print("Predicted Emotion:", prediction[0])

    