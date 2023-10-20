import os
import json
import random
import pickle
import nltk
import numpy as np
from typing import Union
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

class BasicAssistant:

    def __init__(self, intents_data: Union[str, os.PathLike, dict], method_mappings: dict = {}, model_name: str = "basic_model") -> None:
        nltk.download('punkt', quiet=True)
        nltk.download('wordnet', quiet=True)

        if isinstance(intents_data, dict):
            self.intents_data = intents_data
        else:
            if os.path.exists(intents_data):
                with open(intents_data, "r") as f:
                    self.intents_data = json.load(f)
            else:
                raise FileNotFoundError

        self.method_mappings = method_mappings
        self.model_name = model_name

        self.vectorizer = CountVectorizer(tokenizer=nltk.word_tokenize)
        self.classifier = MultinomialNB()

        self.intents = []

    def _prepare_intents_data(self, ignore_letters: tuple = ("!", "?", ",", ".")):
        documents = []
        labels = []

        for intent in self.intents_data["intents"]:
            if intent["tag"] not in self.intents:
                self.intents.append(intent["tag"])

            for pattern in intent["patterns"]:
                pattern_words = nltk.word_tokenize(pattern)
                pattern_words = [w.lower() for w in pattern_words if w not in ignore_letters]
                documents.append(" ".join(pattern_words))
                labels.append(intent["tag"])

        return documents, labels

    def fit_model(self):
        documents, labels = self._prepare_intents_data()
        
        X = self.vectorizer.fit_transform(documents)
        y = np.array(labels)

        self.classifier.fit(X, y)

    def save_model(self):
        with open(f'{self.model_name}_vectorizer.pkl', 'wb') as vectorizer_file:
            pickle.dump(self.vectorizer, vectorizer_file)
        with open(f'{self.model_name}_classifier.pkl', 'wb') as classifier_file:
            pickle.dump(self.classifier, classifier_file)

    def load_model(self):
        with open(f'{self.model_name}_vectorizer.pkl', 'rb') as vectorizer_file:
            self.vectorizer = pickle.load(vectorizer_file)
        with open(f'{self.model_name}_classifier.pkl', 'rb') as classifier_file:
            self.classifier = pickle.load(classifier_file)

    def _predict_intent(self, input_text: str):
        input_text = " ".join([w.lower() for w in nltk.word_tokenize(input_text)])
        input_vector = self.vectorizer.transform([input_text])
        predicted_intent = self.classifier.predict(input_vector)[0]

        return predicted_intent

    def process_input(self, input_text: str):
        predicted_intent = self._predict_intent(input_text)

        try:
            if predicted_intent in self.method_mappings:
                self.method_mappings[predicted_intent]()

            for intent in self.intents_data["intents"]:
                if intent["tag"] == predicted_intent:
                    return random.choice(intent["responses"])
        except IndexError:
            return "I don't understand. Please try again."

# Example usage:
if __name__ == "__main__":
    # Define your intents data as a dictionary or provide a JSON file path.
    intents_data = {
        "intents": [
            {
                "tag": "greeting",
                "patterns": ["Hello", "Hi", "Hey"],
                "responses": ["Hello!", "Hi there!", "Hey! How can I assist you?"]
            },
            {
                "tag": "goodbye",
                "patterns": ["Goodbye", "See you later", "Bye"],
                "responses": ["Goodbye!", "See you later!", "Bye! Have a great day!"]
            }
        ]
    }

    # Initialize the assistant and train the model.
    assistant = BasicAssistant(intents_data)
    assistant.fit_model()

    # Process user input and get responses.
    user_input = "Hello"
    response = assistant.process_input(user_input)
    print(response)
