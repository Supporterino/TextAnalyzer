import os


def write_file(filepath, data):
    with open(filepath, "w+") as output:
        output.writelines(data)
    print(":: Written File {}".format(filepath))


def clean_up():
    print(":: Removing old files")
    files = [
        os.getcwd() + "/reports/NumberOfSentences.txt",
    ]

    for file in files:
        if os.path.exists(file):
            os.remove(file)
