from helper_functions import write_file, clean_up
import os


class Analyzer:
    def __init__(self, data):
        self.amount_of_sentences = 0
        self.words_per_sentence = []
        self.avg_words_per_sentence = 0
        self.data = data
        clean_up()

    def get_number_of_sentences(self):
        fileoutput = "Number of sentences in text\n\n"
        self.amount_of_sentences = len(self.data)
        fileoutput += "{0}\n".format(self.amount_of_sentences)
        write_file(os.getcwd() + "/reports/NumberOfSentences.txt", fileoutput)

    def get_number_of_words_per_sentence(self):
        fileoutput = "Number of words per sentence\n\n"
        for sentence in self.data:
            self.words_per_sentence.append(len(sentence.split(" ")))
        for x in range(len(self.words_per_sentence)):
            fileoutput += "{0}\t{1}\n".format(x, self.words_per_sentence[x])
        write_file(os.getcwd() + "/reports/WordsPerSentence.txt", fileoutput)

    def get_average_words_per_sentence(self):
        fileoutput = "Average number of words per sentence\n\n"
        self.avg_words_per_sentence = round(sum(self.words_per_sentence) / len(self.words_per_sentence), 2)
        fileoutput += "{0}\n".format(self.avg_words_per_sentence)
        write_file(os.getcwd() + "/reports/AverageWordsPerSentence.txt", fileoutput)
