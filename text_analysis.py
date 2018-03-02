import matplotlib.pyplot as plt
import sys
import operator
import argparse
import string
from operator import itemgetter


"""

    Listing some statistics like frequency and rank of words of a given text: 
    
    
    The scope of this program is  to
    * Output the top n words with its rank and frequency.
    * Creating data visualisation using a pie chart 
        * pie chart: with the frequency of top n words
                     distribution.
    
    
    
    Version: python 3.6
    Dependency packages: String, Matplotlib, numpy and itemgetter
    Usage:Python3 text_analysis.py <num>, <filename>

    num: type:int >0
    help="Enter the number of words to be searched for in the text file."
    
    filename: "the path to the text file to be searched through"
"""    


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'num', type=int, 
        help="Enter the number(positive integer) of words to be searched for in the text file."
    )
    parser.add_argument(
        "filename",
        help="the path to the text file to be searched through"
    )

    args = parser.parse_args()

    try:
        open(args.filename)
    except FileNotFoundError:

        # Custom error print
        sys.stderr.write("Error: " + args.filename + " does not exist!")
        sys.exit(1)

    text_analysis(args.num, args.filename)


def text_analysis(num, filename):
    
    words = {}
    # Removing the punctuations in the text
    translator = str.maketrans('', '', string.punctuation)

    words_gen = (word.translate(translator).lower()
                 for line in open(filename)
                 for word in line.split())
    for word in words_gen:
        words[word] = words.get(word, 0) + 1
    #  creating a list of words sorted in descending order
    number =int(num)
    top_words = sorted(words.items(), key=itemgetter(1), reverse=True)[:number]

    # Variable initialisation
    rank = 1

    t_word = []
    t_freq = []

    print("%4s %10s %10s" % ("Rank ", "Word ",  "Frequency "))
    for word, frequency in top_words:
        print("%4d %10s %10d" % (rank, word, frequency))
        rank += 1  # making a  word ranking
        t_word.append(word)  # adding the n words to t_word
        t_freq.append(frequency)  # adding the frequency of words
    """     
        Pie chart, where the slices will be ordered and plotted counter-clockwise:
    """

    fig1, ax1 = plt.subplots()

    fig1 = ax1.pie(t_freq, labels=t_word, autopct='%1.0f%%', startangle=90)
    # Set aspect ratio to be equal so that pie is drawn as a circle.

    ax1.axis('equal')
    plt.title("Top frequency words")
    plt.show()


if __name__ == "__main__":
    main()
