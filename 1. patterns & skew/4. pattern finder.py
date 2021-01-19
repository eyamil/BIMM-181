import sys

# Given a pattern and text, find all indices in the text
# where pattern begins.
# run `python main.py filepath` where the file's first line is
# the pattern to find and the second line is the text to search.

def main():
    file = open(sys.argv[1], "r")
    pat = file.readline().strip()
    text = file.readline().strip()
    print(' '.join(map(str, find(text, pat))))

def find(text, pat):
    ind = []
    for i in range(len(text) - len(pat) + 1):
        if text[i : i + len(pat)] == pat:
            ind.append(i)
    return ind

if __name__ == "__main__":
    main()