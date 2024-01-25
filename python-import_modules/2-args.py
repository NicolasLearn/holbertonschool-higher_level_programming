#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    len_argv = len(argv) - 1
    if len_argv == 0:
        print("0 arguments.")
    elif len_argv == 1:
        print("{} argument:".format(len_argv))
        print("{}: {}".format(len_argv, argv[len_argv]))
    else:
        print("{} arguments:".format(len_argv))
        for arg in range(1, len_argv + 1):
            print("{}: {}".format(arg, argv[arg]))
