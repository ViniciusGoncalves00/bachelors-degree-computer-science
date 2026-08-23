from lexer import Lexer
from parser import Parser


def test_parser():

    source = """
    (begin
        (set a 10)
        (set b 20)

        (print (+ a b))

        (if (>= a b)
            (print a)
            (print b)
        )

        (while (< a 100)
            (set a (+ a 1))
        )
    )
    """

    lexer = Lexer(source)

    tokens = lexer.tokenize()

    parser = Parser(tokens)

    expressions = parser.parse()

    print()
    print("===== TESTE DO PARSER =====")

    for expression in expressions:
        print(expression.dump())

    print("===========================")