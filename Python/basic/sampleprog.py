#!/usr/bin/env python
# Template for best practices python program
import argparse

# Input Args
infile = []
verbose = []


def parse_args():
    global infile, verbose
    parser = argparse.ArgumentParser(description="Show a demo program with arguments")
    parser.add_argument("input",
                        help="the name of the input file to use",
                        type=str,
                        default="a.in")
    parser.add_argument("-v", "--verbose",
                        help="Turn on verbose mode.",
                        action="store_true")
    args = parser.parse_args()
    infile = args.input
    verbose = args.verbose


def main():
    parse_args()
    do_stuff()


def do_stuff():
    print infile


if __name__ == "__main__":
    main()