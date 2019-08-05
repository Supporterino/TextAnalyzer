# TextAnalyzer

This is a text analyzer to get statistics from your text.


## config

```python
...

FILE_TO_ANALYZE = os.getcwd() + "/input/text.txt"
WARNING_THRESHOLD = 20
WORD_GAP = 5
PREFIX = "Debug"

...
```
This is an extract of the main.py, where you have to adjust some variables to configure the analyzer for your needs. This configuration will be moved to an external file at some point.

You can configure the following options:
+ `FILE_TO_ANALYZE` takes the path to your txt file with your text in it. Expected is a file named text.txt inside the `input` directory
+ `WARNING_THRESHOLD` is the lenght of sentences before they get recognized by the too long feature
+ `WORD_GAP` is the threshold in which words should be searched for duplicates
+ `PREFIX` is the name of the directory inside to `


## Features

The analyzer supports the following functionalities at version 0.1.

### Average words per sentence

This report gives you a number which represents the average words used per sentence. This number is rounded by 2 digits behind the decimal point.

### Duplicates

This report gives you the words which appear to frequently [see config](). The information given is the position of the words first occurrence and the distance from its first position to the reappearance.

### Number of sentences

This reports gives you a number of the total sentences in your text.

### Usage of words

Gives a list with all words sorted by their usage. All words are lower case and punctuation is removed.

### Warning for too long sentences

Gives a list of sentences which passed the threshold [see config]().
