import matplotlib.pyplot as plt
import numpy as np
import os
import shutil


class Grapher:
    def __init__(self, analyzer):
        self.analyzer = analyzer
        self.create_img_directory()

    def create_img_directory(self):
        if os.path.exists(self.analyzer.output_path + "/img"):
            shutil.rmtree(self.analyzer.output_path + "/img")
        if not os.path.exists(self.analyzer.output_path + "/img"):
            os.makedirs(self.analyzer.output_path + "/img")

    def run_all(self):
        self.gen_graph_for_words_per_sentence()
        self.gen_graph_for_usage_of_words()
        self.gen_graph_how_hard_do_i_suck()

    def gen_graph_for_words_per_sentence(self):
        fig, ax = plt.subplots()
        ax.plot(self.analyzer.words_per_sentence)
        ax.set(xlabel='sentence', ylabel='words', title='words per sentence')
        ax.grid()
        fig.savefig(self.analyzer.output_path + "/img/words_per_sentence.png")
        plt.show()

    def gen_graph_for_usage_of_words(self):
        xvals = []
        yvals = []
        counter = 0
        for key in self.analyzer.usage_of_words:
            if counter > 10:
                break
            xvals.append(key)
            yvals.append(self.analyzer.usage_of_words[key])
            counter += 1

        fig, ax = plt.subplots()
        ax.bar(xvals, yvals, align='center', alpha=0.5)
        ax.set(title='Usage per word (top 10)', ylabel='Usage (n times)')
        fig.savefig(self.analyzer.output_path + "/img/usage_of_words.png")
        plt.show()

    def gen_graph_how_hard_do_i_suck(self):
        with plt.xkcd():
            fig = plt.figure()
            ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
            ax.spines['right'].set_color('none')
            ax.spines['top'].set_color('none')
            ax.set_xticks([])
            ax.set_yticks([])
            ax.set_ylim([-30, 10])

            data = np.ones(100)
            data[70:] -= np.arange(30)

            ax.annotate('THE MOMENT THE\n SCRIPT REALISES YOU\n HAVE {0} DUPLICATES\n IN YOUR TEXT.'.format(self.analyzer.duplicates), xy=(70, 1), arrowprops=dict(arrowstyle='->'), xytext=(15, -10))

            ax.plot(data)

            ax.set_xlabel('TIME')
            ax.set_ylabel('QUALITY OF YOUR TEXT')
            fig.text(0.5, 0.05, '"Text Quality"', ha="center")
            fig.savefig(self.analyzer.output_path + "/img/suck.png")
            fig.set_tight_layout(False)

        plt.show()
