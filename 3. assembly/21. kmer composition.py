import sys

# Given an integer k and a genome string, break up the genome string
# into all its k-mers.
# run `python main.py filepath` where the file's first line is the
# parameter k and the second line is the genome string.

def main():
    file = open(sys.argv[1], "r")
    k = int(file.readline().strip())
    text = file.readline().strip()
    print('\n'.join(composition(k, text)))

def composition(k, text):
    composition = []
    for i in range(len(text) - k + 1):
        composition.append(text[i : i + k])
    return composition

if __name__ == "__main__":
    main()