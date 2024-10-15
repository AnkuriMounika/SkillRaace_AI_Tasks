
import re
from collections import defaultdict

# Load dataset from a text file
with open('dataset_book.txt', 'r') as file:  # Replace 'dataset.txt' with your actual file name
    texts = file.readlines()

# Function to preprocess the dataset
def preprocess(sentence):
    sentence = sentence.lower()  # Convert to lowercase
    sentence = re.sub(r'[^a-zA-Z\s]', '', sentence)  # Remove non-alphabetic characters
    return sentence

# Preprocess all sentences
processed_dataset = [preprocess(sentence).split() for sentence in texts]

# Build a word frequency dictionary
word_freq = defaultdict(lambda: defaultdict(int))
for sentence in processed_dataset:
    for i in range(len(sentence) - 1):
        word_freq[sentence[i]][sentence[i + 1]] += 1

# Function to predict the next word
def predict_next_word(word):
    if word in word_freq:
        next_word = max(word_freq[word], key=word_freq[word].get)
        return next_word
    else:
        return "No prediction available"

# Example usage
user_input = input()
last_word = user_input.split()[-1]
predicted_word = predict_next_word(last_word)
print(f"Predicted next word: {predicted_word}")
