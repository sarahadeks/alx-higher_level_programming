#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    addition = 0

    for arg in sys.argv:
        if arg != sys.argv[0]:
            addition += int(arg)
    print("{}".format(addition))
