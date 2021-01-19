import sys

# Given a burrows-wheeler transformed string, build the last-to-first array.
# run `python main.py filepath` where the file's first line has the string and the
# second line has an integer to run through the last-to-first mapping.

def main():
    file = open(sys.argv[1], "r")
    bwt = file.readline().strip()
    pos = int(file.readline().strip())
    print(last_to_first(bwt).index(pos))

def last_to_first(bwt):
    numbered_bwt = []
    for i in range(len(bwt)):
        numbered_bwt.append((bwt[i], i))
    numbered_bwt.sort(key = lambda x : x[0])
    permutation = [x[1] for x in numbered_bwt]
    return(permutation)

if __name__ == "__main__":
    main()