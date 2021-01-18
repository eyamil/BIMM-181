import sys

# Count the number of times a pattern appears in text.
# run `python main.py filepath`, where the file's first
# line is the text to search and the second is the pattern
# to count.

def main():
	# Open file; first line corpus and second is pattern to match
    file = open(sys.argv[1], "r")
    text = file.readline().strip()
    pat = file.readline().strip()
    print(count(text, pat))

def count(text, pat):
    count = 0
    for i in range(len(text) - len(pat) + 1):
        if text[i : i + len(pat)] == pat:
            count = count + 1
    return count

if __name__ == "__main__":
    main()