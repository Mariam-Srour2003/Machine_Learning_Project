from flask import Flask, render_template, request, jsonify
import joblib
import re
import nltk
from nltk.corpus import stopwords
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)

# loading the trained model and  vectorizer
vectorizer, classifier = joblib.load('text_classifier_model.joblib')

# loading the data from the csv file
data = pd.read_csv('cmd_commands.csv')

# intailize label column
label_column = 'name'  

# download the stopwatch words
nltk.download('stopwords')

additional_stop_words = ['a', 'an', 'and', 'for', 'in', 'is', 'it', 'of', 'on', 'or', 'the', 'to', 'with',
                          'seamless', 'comprehensive', 'facilitating', 'enhance', 'empower', 'efficient', 'streamlined']

stop_words = set(stopwords.words('english'))
stop_words.update(additional_stop_words)

def preprocess_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
    text = ' '.join(word for word in text.split() if word not in stop_words)
    return text


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    user_input = request.form['user_input']
    user_input_preprocessed = preprocess_text(user_input)
    user_input_vectorized = vectorizer.transform([user_input_preprocessed])

    # predict the first 5 labls and the propa of the given desc
    top_predictions = classifier.predict_proba(user_input_vectorized)
    top_indices = top_predictions.argsort()[:, ::-1][:, :5]

    predictions = []
    for i in range(5):
        predicted_label = classifier.classes_[top_indices[0][i]]
        probability = top_predictions[0][top_indices[0][i]]

        # find all occurrence of the predicted label in the db
        label_indices = data[data[label_column] == predicted_label].index

        # get the descriptions of all occurrences
        descriptions = [data.iloc[description_index]['description1'] for description_index in label_indices]

        # append the predictions to the list
        predictions.append({"label": predicted_label, "probability": probability, "description": descriptions})

    return jsonify(predictions)

if __name__ == '__main__':
    app.run(debug=True)
