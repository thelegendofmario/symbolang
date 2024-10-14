from lex import Lexer

def main():
    source = 'Set x = 24'
    lexer = Lexer(source)

    while lexer.peek() != '\0':
        print(lexer.curChar)
        lexer.nextChar()

main()
