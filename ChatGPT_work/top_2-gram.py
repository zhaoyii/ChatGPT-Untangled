import re
from collections import Counter
from itertools import tee

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]+', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text

def get_ngrams(text, n=2):
    words = text.split()
    ngrams = zip(*(words[i:] for i in range(n)))
    return [' '.join(ngram) for ngram in ngrams]

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def ngram_probability(text, n=3):
    ngrams = get_ngrams(text, n)
    total_ngrams = len(ngrams)
    counter = Counter(ngrams)
    return {ngram: count / total_ngrams for ngram, count in counter.items()}

def main():
    text = read_file('the_old_man_and_the_sea.txt')
    preprocessed_text = preprocess_text(text)
    ngram_probabilities = ngram_probability(preprocessed_text)

    sorted_ngram_probabilities = sorted(ngram_probabilities.items(), key=lambda x: x[1], reverse=True)

    # 输出Markdown表格标题和分隔符
    print('| 2-gram | Probability |')
    print('|--------|-------------|')

    for ngram, probability in sorted_ngram_probabilities[:10]:
        print(f'| {ngram} | {probability:.6f} |')  # 更改为Markdown表格行格式

if __name__ == "__main__":
    main()
