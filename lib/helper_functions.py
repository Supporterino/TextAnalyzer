import os


def write_file(filepath, data):
    with open(filepath, "w+", encoding="utf-8") as output:
        output.writelines(data)
    print(":: Written File {}".format(filepath))


def clean_up(path):
    print(":: Removing old files")
    files = [
        path + "/NumberOfSentences.txt",
        path + "/WordsPerSentence.txt",
        path + "/AverageWordsPerSentence.txt",
        path + "/WarningTooLongSentences.txt",
        path + "/UsageOfWords.txt",
        path + "/Duplicates.txt",
    ]

    for file in files:
        if os.path.exists(file):
            os.remove(file)
