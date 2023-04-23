import string
from collections import defaultdict

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

def main(file_path):
    text = read_text_file(file_path)
    processed_text = preprocess_text(text)
    bigrams = generate_bigrams(processed_text)
    frequencies = calculate_frequencies(bigrams)

    all_possible_bigrams = generate_all_possible_bigrams()
    all_possible_bigrams.update(frequencies)

    for bigram, frequency in all_possible_bigrams.items():
        print(f"{bigram}: {frequency:.4f}")

if __name__ == "__main__":
    file_path = "the_old_man_and_the_sea.txt"
    main(file_path)
