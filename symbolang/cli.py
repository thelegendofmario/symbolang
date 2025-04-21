from . import symbolang
import sys, argparse

parser = argparse.ArgumentParser(
    prog="symbolang",
    description="a simple 2d programming language.",
    epilog="filler text"
)

parser.add_argument("filename")
parser.add_argument("-d", "--debug", action='store_true')

args = parser.parse_args()

def main():
    symbolang.run(args)