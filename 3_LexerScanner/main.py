import sys
from lexer import Lexer

def main():
    if len(sys.argv) < 2:
        print("ERROR: No input file provided.")
        exit(1)

    with open(sys.argv[1], "r") as f:
        lexer = Lexer(f.read(), sys.argv[1])

    tokens = lexer.lex()

    # Printing the tokens
    for token in tokens:
        print(f"{token.loc}:  {token.type.name} {token.value}")

if __name__ == "__main__":
    main()