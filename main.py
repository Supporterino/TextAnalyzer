import os
from input_parser import load_sentences_from_file
from analyzer import Analyzer

FILE_TO_ANALYZE = os.getcwd() + "/samples/debug.txt"
WARNING_THRESHOLD = 20
WORD_GAP = 5
PREFIX = "Debug"


if __name__ == '__main__':
    print(":: Text Analyzer")
    sentences = load_sentences_from_file(FILE_TO_ANALYZE)
    analyzer = Analyzer(sentences, WARNING_THRESHOLD, PREFIX, WORD_GAP)
    analyzer.run_analyses()