from . import symbolang
import sys

def main():
    try:
        symbolang.Symbolang(sys.argv[1], sys.argv[2])
    except IndexError:
        print('You have to specify a file to open!! and some arguments!!')
        quit()
    except ZeroDivisionError:
        print("lol don't divide by zero")
        quit()