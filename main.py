import os
from input_parser import load_sentences_from_file
from analyzer import Analyzer

FILE_TO_ANALYZE = os.getcwd() + "/samples/sample_sofea.txt"


if __name__ == '__main__':
    print(":: Text Analyzer")
    sentences = load_sentences_from_file(FILE_TO_ANALYZE)
    analyzer = Analyzer(sentences)
    analyzer.get_number_of_sentences()
    analyzer.get_number_of_words_per_sentence()
    analyzer.get_average_words_per_sentence()
