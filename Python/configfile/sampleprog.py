#!/usr/bin/env python
# Template for best practices python program
# Shows use of a .cfg file for configuration
# in addition to using command line args
import argparse
import ConfigParser

# Input Args
cfgfile = []
verbose = []



def parse_args():
    global cfgfile, verbose
    parser = argparse.ArgumentParser(description="Show a demo program with arguments")
    parser.add_argument("config",
                        help="the name of the configuration file to use",
                        type=str,
                        default="default.cfg")
    parser.add_argument("-v", "--verbose",
                        help="Turn on verbose mode.",
                        action="store_true")
    args = parser.parse_args()
    cfgfile = args.config
    verbose = args.verbose



def main():
    parse_args()
    do_stuff()


def do_stuff():
    print cfgfile


if __name__ == "__main__":
    main()