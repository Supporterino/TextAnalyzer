import matplotlib.pyplot as plt
import os


class Grapher:
    def __init__(self, analyzer):
        self.analyzer = analyzer
        self.create_img_directory()

    def create_img_directory(self):
        if not os.path.exists(self.analyzer.output_path + "/img"):
            os.makedirs(self.analyzer.output_path + "/img")

    def demo_plot(self):
        fig, ax = plt.subplots()
        ax.plot(self.analyzer.words_per_sentence)
        ax.set(xlabel='sentence', ylabel='words', title='words per sentence')
        ax.grid()
        fig.savefig(self.analyzer.output_path + "/img/demo.png")
        plt.show()
