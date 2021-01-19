import sys
import math

# Given a string with a special terminal character, return the string's suffix array.
# run `python main.py filepath` where the first line of the file has the string, terminated
# by a special character ("$" works.)

def main():
    file = open(sys.argv[1], "r")
    text = file.readline().strip()
    print(", ".join([str(pos) for pos in make_suffix_array(text)]))

def make_suffix_array(text):
    arr = []
    for pos in range(len(text)):
        arr.append((text[pos :], pos))
    arr.sort(key = lambda x : x[0])
    return([entry[1] for entry in arr])

if __name__ == "__main__":
    main()