import sys

def parseLine(line):
    parts = line.strip().split('\t')
    word = parts[0]
    file_line = parts[1].rsplit(':', 1)
    filename = file_line[0]
    lineno = int(file_line[1])
    return word, filename, lineno

def printEntry(word, occur):
    parts = []
    for filename, lines in occur.items():
        parts.append(f'({filename}, {lines})')
    entry = ' '.join(parts)
    print(f'{word}: {entry}')

def main(): 
    current_word = None
    occurrences = {}

    for line in sys.stdin:
        word, filename, lineno = parseLine(line)
        if word == current_word:
            occurrences.setdefault(filename, []).append(lineno)
        else:
            if current_word is not None:
                printEntry(current_word, occurrences)
            current_word = word
            occurrences = {}
            occurrences.setdefault(filename, []).append(lineno)

    if current_word is not None:
        printEntry(current_word, occurrences)

main()
