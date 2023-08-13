#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argslen = len(sys.argv)

    if argslen == 1:
        print("arguements.".format(argslen - 1))
    elif argslen == 2:
        print("arguement.".format(argslen - 1))
    else:
        print("{}arguments:".format(argslen - 1))
    for i in range(1, argslen):
        print("{}: {}".format(i, sys.argv[i]))
