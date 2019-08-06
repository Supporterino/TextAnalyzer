import os
from lib.SentenceSplitter import SentenceSplitter


def load_text(path):
    print("\t::Loading raw text from file")
    with open(path, "r", encoding="utf-8") as input_file:
        text = input_file.read()
    return text


def split_into_sentences(data):
    print("\t::Splitting raw text into sentences")
    splitter = SentenceSplitter(language='de', non_breaking_prefix_file='lib/non_breaking_prefixes/de.txt')
    return splitter.split(data)


def load_sentences_from_file(path):
    print(":: Getting sentences from file: {}".format(path))
    raw_input = load_text(path)
    sentences = split_into_sentences(raw_input)
    return sentences


if __name__ == '__main__':
    print(split_into_sentences(load_text(os.getcwd() + "/samples/sample_sofea.txt")))
