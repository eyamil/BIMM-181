import sys

# Given a DNA string, find its reverse complement.
# run `python main.py filepath` where file's first
# is the string to reverse complement.

def main():
    file = open(sys.argv[1], "r")
    text = file.readline().strip()
    print(reverse(complement(text)))

def reverse(text):
    rev = ""
    for i in range(len(text)):
        rev = rev + text[i]
    return rev

def complement(text):
    base_list = ['A', 'C', 'G', 'T']
    comp = ""
    for i in range(len(text)):
        complement_ind = len(base_list) - (base_list.index(text[i]) + 1)
        comp = base_list[complement_ind] + comp
    return comp

if __name__ == "__main__":
    main()