import os
from basefilter import BaseFilter
import trainingcorpus
import corpus
import utils
import math
from collections import defaultdict


class MyFilter(BaseFilter):
    def __init__(self):
        super().__init__()
        # Initialize word count dictionaries and total counters for SPAM and OK categories
        self.spam_word_counts = defaultdict(int)
        self.ok_word_counts = defaultdict(int)
        self.spam_total_count = 0
        self.ok_total_count = 0
        self.total_spam = 0
        self.total_ok = 0

    def train(self, training_data):
        # Retrieve texts and labels from the training data
        texts, labels = trainingcorpus.TrainingCorpus.get_data(training_data)
        for text, label in zip(texts, labels):
            if label == "SPAM":
                self.total_spam += 1
                for word in text.split():
                    self.spam_word_counts[word] += 1
                    self.spam_total_count += 1
            else:
                self.total_ok += 1
                for word in text.split():
                    self.ok_word_counts[word] += 1
                    self.ok_total_count += 1

        # Prevent division by zero during scoring by ensuring non-zero totals
        if self.total_spam == 0:
            self.total_spam = 1
        if self.total_ok == 0:
            self.total_ok = 1

    def predict(self, test_data):
        # Generate predictions for each email in the test data
        predictions = []
        for text in test_data.values():
            spam_score = self._compute_score(text, "SPAM")
            ok_score = self._compute_score(text, "OK")
            predictions.append("SPAM" if spam_score > ok_score else "OK")
        return predictions

    def _compute_score(self, text, label):
        # Compute the log-probability score for a given text under the specified label
        if self.total_spam == 0 or self.total_ok == 0:
            return float('-inf') if label == "SPAM" else float('inf')

        words = text.split()
        score = math.log(self.total_spam if label == "SPAM" else self.total_ok) - math.log(
            self.total_spam + self.total_ok)

        word_counts = self.spam_word_counts if label == "SPAM" else self.ok_word_counts
        total_count = self.spam_total_count if label == "SPAM" else self.ok_total_count

        vocab_size = len(self.spam_word_counts) + len(self.ok_word_counts)
        smoothing = 1  # Laplace smoothing to handle unseen words

        for word in words:
            word_probability = (word_counts[word] + smoothing) / (total_count + smoothing * vocab_size)
            score += math.log(word_probability)

        return score

    def test(self, test_data_path):
        # Load test data and generate predictions
        test_data = corpus.Corpus.get_data(test_data_path)
        predictions = self.predict(test_data)

        # Write predictions to !prediction.txt file in the test data directory
        prediction_file = os.path.join(test_data_path, "!prediction.txt")
        with open(prediction_file, "w", encoding="utf-8") as f:
            for filename, text in test_data.items():
                prediction = predictions[list(test_data.keys()).index(filename)]
                f.write(f"{filename} {prediction}\n")

    def evaluate(self, test_data, true_labels):
        # Evaluate the filter's performance by comparing predictions to true labels
        predicted_labels = self.predict(test_data)
        tp = tn = fp = fn = 0

        for truth, prediction in zip(true_labels, predicted_labels):
            if truth == "SPAM" and prediction == "SPAM":
                tp += 1
            elif truth == "OK" and prediction == "OK":
                tn += 1
            elif truth == "OK" and prediction == "SPAM":
                fp += 1
            elif truth == "SPAM" and prediction == "OK":
                fn += 1

        return {"tp": tp, "tn": tn, "fp": fp, "fn": fn}

    def save_model(self, path):
        # Save the current filter state to a file
        utils.save_object(self, path + '_filter.pkl')

    def load_model(self, path):
        # Load the filter state from a file
        loaded_filter = utils.load_object(path + '_filter.pkl')
        self.__dict__.update(loaded_filter.__dict__)

    def mark_email(self, email_text):
        # Classify a single email as SPAM or OK
        spam_score = self._compute_score(email_text, "SPAM")
        ok_score = self._compute_score(email_text, "OK")
        return "SPAM" if spam_score > ok_score else "OK"
