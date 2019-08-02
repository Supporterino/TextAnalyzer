from helper_functions import write_file, clean_up
import os


class Analyzer:
    def __init__(self, data):
        self.data = data
        clean_up()

    def get_number_of_sentences(self):
        fileoutput = "Number of sentences in text\n\n"
        amount = len(self.data)
        fileoutput += "{0}\n".format(amount)
        write_file(os.getcwd() + "/reports/NumberOfSentences.txt", fileoutput)
