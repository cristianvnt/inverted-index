import os
import sys

def main():
    filename = os.path.basename(os.environ.get('mapreduce_map_input_file', ''))
    stopwords = set(line.strip() for line in open("stopwords.txt"))

    for lineno, line in enumerate(sys.stdin, 1):
        for word in line.strip().split():
            lower_word = word.lower()
            if lower_word in stopwords or not word.isalpha():
                continue
            print(f'{lower_word}\t{filename}:{lineno}')

main()
