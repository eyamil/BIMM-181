import sys

# Given a string terminated by a special character, perform the burrows-wheeler transform.
# run `python main.py filepath` where the file's first line has the string, terminated by
# a special character ("$").

def main():
    file = open(sys.argv[1], "r")
    text = file.readline().strip()
    print(bwt(text))

def cyclic_perm(text, i):
    return(text[i :] + text[: i])

def bwt(text):
    arr = []
    for i in range(len(text)):
        arr.append(cyclic_perm(text, i))
    arr.sort()
    bwt_str = ""
    for i in range(len(text)):
        bwt_str += arr[i][-1]
    return(bwt_str)


if __name__ == "__main__":
    main()