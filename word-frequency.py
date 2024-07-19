import re
from collections import Counter
import os

class WordFrequencyCounter:
    def __init__(self, filepath):
        self.filepath = filepath
        self.text = ""
        self.word_frequencies = Counter()
        self.word_list = []
        self.total_words = 0
        self.unique_words = 0

    def read_file(self):
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"The file {self.filepath} does not exist.")
        with open(self.filepath, 'r', encoding='utf-8') as file:
            self.text = file.read()

    def preprocess_text(self):
        self.text = self.text.lower()
        self.text = re.sub(r'[^a-z\s]', '', self.text)
        self.word_list = self.text.split()
        self.total_words = len(self.word_list)
        self.unique_words = len(set(self.word_list))

    def count_words(self):
        self.word_frequencies = Counter(self.word_list)

    def display_word_frequencies(self):
        print(f"Total Words: {self.total_words}")
        print(f"Unique Words: {self.unique_words}")
        print("Word Frequencies:")
        for word, freq in self.word_frequencies.most_common():
            print(f"{word}: {freq}")

    def save_frequencies_to_file(self, output_filepath):
        with open(output_filepath, 'w', encoding='utf-8') as file:
            file.write(f"Total Words: {self.total_words}\n")
            file.write(f"Unique Words: {self.unique_words}\n")
            file.write("Word Frequencies:\n")
            for word, freq in self.word_frequencies.most_common():
                file.write(f"{word}: {freq}\n")

    def display_top_n_words(self, n):
        print(f"Top {n} Words:")
        for word, freq in self.word_frequencies.most_common(n):
            print(f"{word}: {freq}")

    def save_top_n_words_to_file(self, output_filepath, n):
        with open(output_filepath, 'w', encoding='utf-8') as file:
            file.write(f"Top {n} Words:\n")
            for word, freq in self.word_frequencies.most_common(n):
                file.write(f"{word}: {freq}\n")

    def analyze_word_lengths(self):
        lengths = [len(word) for word in self.word_list]
        length_frequencies = Counter(lengths)
        return length_frequencies

    def display_word_lengths(self):
        length_frequencies = self.analyze_word_lengths()
        print("Word Length Frequencies:")
        for length, freq in length_frequencies.items():
            print(f"Length {length}: {freq}")

    def save_word_lengths_to_file(self, output_filepath):
        length_frequencies = self.analyze_word_lengths()
        with open(output_filepath, 'w', encoding='utf-8') as file:
            file.write("Word Length Frequencies:\n")
            for length, freq in length_frequencies.items():
                file.write(f"Length {length}: {freq}\n")

    def process(self, output_filepath, top_n=10):
        self.read_file()
        self.preprocess_text()
        self.count_words()
        self.display_word_frequencies()
        self.save_frequencies_to_file(output_filepath)
        self.display_top_n_words(top_n)
        self.save_top_n_words_to_file(output_filepath, top_n)
        self.display_word_lengths()
        self.save_word_lengths_to_file(output_filepath)

def main():
    input_filepath = 'textfile.txt'
    output_filepath = 'word_frequencies.txt'
    top_n = 10

    counter = WordFrequencyCounter(input_filepath)
    
    try:
        counter.process(output_filepath, top_n)
        print(f"Word frequencies and additional analyses have been saved to {output_filepath}.")
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
