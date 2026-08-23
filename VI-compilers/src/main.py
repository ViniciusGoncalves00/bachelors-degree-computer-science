from lexer import Lexer

source = "(+ 10 (* x 2))"

lexer = Lexer(source)
tokens = lexer.tokenize()

for token in tokens:
    print(token)