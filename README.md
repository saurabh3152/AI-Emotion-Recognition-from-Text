# AI Emotion Recognition from Text

An AI-powered Natural Language Processing (NLP) project that analyzes textual input and predicts human emotions such as **Joy, Sadness, Anger, and Fear** using Machine Learning techniques.

---

## Author

**Saurabh Mishra**
MCA Student – Galgotias University

GitHub: https://github.com/saurabh3152

---

## Overview

Understanding emotions from text is an important task in Natural Language Processing (NLP). This project aims to automatically identify emotions expressed in user-provided text using machine learning techniques.

The system processes textual data, converts it into numerical features using TF-IDF Vectorization, and classifies emotions using a Multinomial Naive Bayes model.

---

## Features

* Emotion detection from text
* NLP-based text processing
* TF-IDF feature extraction
* Machine Learning classification
* Real-time emotion prediction from user input

### Supported Emotions

* Joy
* Sadness
* Anger
* Fear

---

## Dataset

The model is trained using an emotion-labeled text dataset containing thousands of sentences.

### Example Dataset Samples

```text
I feel very happy today ; joy
I am feeling sad and lonely ; sadness
This situation makes me angry ; anger
I am scared of this situation ; fear
```

Dataset Files:

```text
train.txt
test.txt
val.txt
```

---

## Project Workflow

```text
Text Input
    ↓
Text Preprocessing
    ↓
TF-IDF Vectorization
    ↓
Multinomial Naive Bayes Classifier
    ↓
Emotion Prediction
```

---

## Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-learn

### NLP Techniques

* Text Classification
* TF-IDF Vectorization

### Machine Learning

* Multinomial Naive Bayes

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Shanvi587/AI-Emotion-Recognition-from-Text.git
```

Navigate to the project directory:

```bash
cd AI-Emotion-Recognition-from-Text
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

### Train the Model

```bash
python train_model.py
```

### Run Emotion Prediction

```bash
python emotion_model.py
```

Example:

```text
Enter text: I feel amazing today
Predicted Emotion: joy
```

---

## Sample Predictions

| Input Text                    | Predicted Emotion |
| ----------------------------- | ----------------- |
| I feel very happy today       | Joy               |
| I am feeling sad and lonely   | Sadness           |
| This situation makes me angry | Anger             |
| I am scared of the future     | Fear              |

---

## Skills Demonstrated

* Natural Language Processing (NLP)
* Text Classification
* Machine Learning
* Feature Engineering
* Model Training & Evaluation
* Python Programming
* Data Preprocessing

---

## Project Structure

```text
AI-Emotion-Recognition-from-Text
│
├── train_model.py
├── emotion_model.py
├── train.txt
├── test.txt
├── val.txt
├── requirements.txt
├── emotion_model.pkl
├── vectorizer.pkl
└── README.md
```

---

## Future Improvements

* Implement Deep Learning models (LSTM, GRU)
* Integrate BERT-based emotion classification
* Develop a Flask web application
* Deploy as a REST API
* Support additional emotion categories

---

## References

* Scikit-learn Documentation: https://scikit-learn.org
* NLTK Documentation: https://www.nltk.org
* Emotion Dataset for NLP: https://www.kaggle.com/datasets/praveengovi/emotions-dataset-for-nlp
* TF-IDF Overview: https://en.wikipedia.org/wiki/Tf%E2%80%93idf

---

## License

This project is intended for educational and learning purposes.
