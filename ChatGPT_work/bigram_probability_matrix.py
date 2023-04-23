import string
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

def preprocess_text(text):
    text = text.upper()
    allowed_chars = string.ascii_uppercase + ' '
    processed_text = ''.join(c for c in text if c in allowed_chars)
    return processed_text

def generate_bigrams(text):
    words = text.split()
    bigrams = defaultdict(int)
    for word in words:
        for i in range(len(word) - 1):
            bigram = word[i:i + 2]
            bigrams[bigram] += 1
    return bigrams

def calculate_frequencies(bigrams):
    total_bigrams = sum(bigrams.values())
    frequencies = {bigram: count / total_bigrams for bigram, count in bigrams.items()}
    return frequencies

def generate_all_possible_bigrams():
    all_bigrams = {}
    for c1 in string.ascii_uppercase:
        for c2 in string.ascii_uppercase:
            all_bigrams[f"{c1}{c2}"] = 0
    return all_bigrams

def create_matrix(frequencies):
    matrix = np.zeros((26, 26))
    for bigram, frequency in frequencies.items():
        row = ord(bigram[0]) - ord('A')
        col = ord(bigram[1]) - ord('A')
        matrix[row, col] = frequency
    return matrix

def plot_matrix(matrix):
    plt.imshow(matrix, cmap='viridis', interpolation='nearest')
    plt.xticks(range(26), string.ascii_uppercase)
    plt.yticks(range(26), string.ascii_uppercase)
    plt.xlabel('Second Letter')
    plt.ylabel('First Letter')
    plt.title('Bigram Probability Matrix')
    plt.colorbar(label='Probability')
    plt.show()

def main(file_path):
    text = read_text_file(file_path)
    processed_text = preprocess_text(text)
    bigrams = generate_bigrams(processed_text)
    frequencies = calculate_frequencies(bigrams)

    all_possible_bigrams = generate_all_possible_bigrams()
    all_possible_bigrams.update(frequencies)

    matrix = create_matrix(all_possible_bigrams)
    plot_matrix(matrix)

if __name__ == "__main__":
    file_path = "the_old_man_and_the_sea.txt"
    main(file_path)
