#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    the = len(sys.argv)
    if the == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(the - 1))
        for i in range(1, the):
            print("{}: {}".format(i, sys.argv[i]))
