from helper_functions import write_file, clean_up
import os
import collections
import re


class Analyzer:
    def __init__(self, data, threshold, prefix, word_gap):
        self.amount_of_sentences = 0
        self.words_per_sentence = []
        self.avg_words_per_sentence = 0
        self.usage_of_words = {}
        self.data = data
        self.threshold = threshold
        self.word_gap = word_gap
        self.output_path = self.create_reports_directory(prefix)
        self.ignore_list = self.init_ignore_list()
        clean_up(self.output_path)

    def run_analyses(self):
        self.get_number_of_sentences()
        self.get_number_of_words_per_sentence()
        self.get_average_words_per_sentence()
        self.gen_warning_for_too_long_sentences()
        self.get_word_usage()
        self.get_double_words()

    @staticmethod
    def init_ignore_list():
        with open(os.getcwd() + "/config/ignoreList.txt", "r") as input:
            ignore_list = input.readlines()
        for i in range(len(ignore_list)):
            ignore_list[i] = ignore_list[i].replace('\n', '').strip()
        return ignore_list

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
                words.append(re.sub("\.(?!\d)", '', word.strip().lower().replace(',', '').replace('"', '').replace('„', '').replace('“', '')))
        return words

    def get_double_words(self):
        doubles = []
        fileoutput = "Duplicate words with distance of {0}\n\n".format(self.word_gap)
        words = self.create_word_map()
        for x in range(len(words)):
            if not words[x] in self.ignore_list:
                for i in range(1, self.word_gap):
                    if i + x < len(words):
                        if words[x + i] == words[x]:
                            doubles.append("Duplicate at word({0}): '{1}' with distance of {2}\n".format(str(x), words[x], str(i)))
                    else:
                        break
        for j in doubles:
            fileoutput += j
        write_file(self.output_path + "/Duplicates.txt", fileoutput)

