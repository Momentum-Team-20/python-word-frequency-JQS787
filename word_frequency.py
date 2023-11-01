import string
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

 # def print_word_freq(file):
    # """Read in `file` and print out the frequency of words in that file."""
    



with open ("the-hill-we-climb.txt","r") as f:
    text = f.read()
    words = text.split()
    # print (words)
    table = str.maketrans("", "", string.punctuation)
    stripped = [word.translate(table) for word in words]
    # print (stripped)
    lowercase = [word.lower() for word in stripped]
    
    nonstop = []
    for word in lowercase:
        if word not in STOP_WORDS:
            nonstop.append(word)
    
    word_count = {}
    for word in nonstop:
        word_count[word] = word_count.get(word, 0) + 1
    print(word_count)
    for word, count in word_count.items():
        print(word, count)



   











if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
