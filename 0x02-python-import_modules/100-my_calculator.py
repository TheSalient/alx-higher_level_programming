#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    if len(argv) == 4:
        a = int(argv[1])
        b = int(argv[3])
        c = argv[2]
        hi = {"+": add, "-": sub, "*": mul, "/": div}
        for i in hi:
            if c == i:
                print("{} {} {} = {}".format(a, c, b, hi[i](a, b)))
                exit(0)
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
