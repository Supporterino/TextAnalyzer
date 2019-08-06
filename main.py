import os
from lib.input_parser import load_sentences_from_file
from lib.analyzer import Analyzer
from lib.printer import Grapher

FILE_TO_ANALYZE = os.getcwd() + "/samples/debug.txt"
WARNING_THRESHOLD = 20
WORD_GAP = 5
PREFIX = "Debug"


if __name__ == '__main__':
    print(":: Text Analyzer")
    sentences = load_sentences_from_file(FILE_TO_ANALYZE)
    analyzer = Analyzer(sentences, WARNING_THRESHOLD, PREFIX, WORD_GAP)
    analyzer.run_analyses()
    grapher = Grapher(analyzer)
    grapher.demo_plot()
