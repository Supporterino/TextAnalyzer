from helper_functions import write_file, clean_up
import os
import collections


class Analyzer:
    def __init__(self, data, threshold, prefix):
        self.amount_of_sentences = 0
        self.words_per_sentence = []
        self.avg_words_per_sentence = 0
        self.usage_of_words = {}
        self.data = data
        self.threshold = threshold
        self.output_path = self.create_reports_directory(prefix)
        clean_up(self.output_path)

    def run_analyses(self):
        self.get_number_of_sentences()
        self.get_number_of_words_per_sentence()
        self.get_average_words_per_sentence()
        self.gen_warning_for_too_long_sentences()
        self.get_word_usage()

    @staticmethod
    def create_reports_directory(prefix):
        if not os.path.exists(os.getcwd() + "/reports/" + prefix):
            os.makedirs(os.getcwd() + "/reports/" + prefix)
        return os.getcwd() + "/reports/" + prefix

    def get_number_of_sentences(self):
        fileoutput = "Number of sentences in text\n\n"
        self.amount_of_sentences = len(self.data)
        fileoutput += "{0}\n".format(self.amount_of_sentences)
        write_file(self.output_path + "/NumberOfSentences.txt", fileoutput)

    def get_number_of_words_per_sentence(self):
        fileoutput = "Number of words per sentence\n\n"
        for sentence in self.data:
            self.words_per_sentence.append(len(sentence.split(" ")))
        for x in range(len(self.words_per_sentence)):
            fileoutput += "{0}\t{1}\n".format(x, self.words_per_sentence[x])
        write_file(self.output_path + "/WordsPerSentence.txt", fileoutput)

    def get_average_words_per_sentence(self):
        fileoutput = "Average number of words per sentence\n\n"
        self.avg_words_per_sentence = round(sum(self.words_per_sentence) / len(self.words_per_sentence), 2)
        fileoutput += "{0}\n".format(self.avg_words_per_sentence)
        write_file(self.output_path + "/AverageWordsPerSentence.txt", fileoutput)

    def gen_warning_for_too_long_sentences(self):
        fileoutput = "Following sentences hit the limit of {} words\n\n".format(self.threshold)
        for sentence in self.data:
            if len(sentence.split(" ")) > self.threshold:
                fileoutput += "Sentence number {0} too long:\n\t{1}\n".format(self.data.index(sentence), sentence)
        write_file(self.output_path + "/WarningTooLongSentences.txt", fileoutput)

    def get_word_usage(self):
        fileoutput = "Usages of each word sorted by usage amount\n\n"
        for entry in self.create_word_map():
            if entry in self.usage_of_words:
                self.usage_of_words[entry] += 1
            else:
                self.usage_of_words[entry] = 1
        self.usage_of_words = collections.OrderedDict(sorted(self.usage_of_words.items(), key=lambda kv: kv[1], reverse=True))
        for x in self.usage_of_words:
            fileoutput += "{0}\t{1}\n".format(x, self.usage_of_words[x])
        write_file(self.output_path + "/UsageOfWords.txt", fileoutput)

    def create_word_map(self):
        words = []
        for sentence in self.data:
            for word in sentence.split(" "):
                words.append(word.strip().lower().replace(',', '').replace('.', ''))
        return words
