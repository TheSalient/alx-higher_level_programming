#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    the = len(sys.argv)
    the1 = 0
    if the == 1:
        print(0)
        exit()
    for i in range(1, the):
        the1 += int(sys.argv[i])
    print("{:d}".format(the1))
