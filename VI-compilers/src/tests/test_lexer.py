from lexer import Lexer


def test_lexer():

    source = """
    (begin
        (set idade 20)
        (set contador 1)

        (if (>= idade 18)
            (print 1)
            (print 0)
        )

        (while (< contador 10)
            (begin
                (print contador)
                (set contador (+ contador 1))
            )
        )
    )
    """

    lexer = Lexer(source)

    tokens = lexer.tokenize()

    print()
    print("===== TESTE DO LEXER =====")

    for num, token in enumerate(tokens, start=1):
        print(
            f"{num:<4} "
            f"{token.type.name:<20} "
            f"{token.lexeme}"
        )

    print("==========================")