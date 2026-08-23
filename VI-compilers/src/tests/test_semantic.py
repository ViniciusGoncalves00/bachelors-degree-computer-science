from lexer import Lexer
from parser import Parser
from semantic import SemanticAnalyzer


def test_semantic():

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
            (begin
                (print a)
                (set a (+ a 1))
            )
        )

    )
    """

    # Lexer
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    # Parser
    parser = Parser(tokens)
    expressions = parser.parse()

    # Semantic Analyzer
    semantic_analyzer = SemanticAnalyzer()

    semantic_analyzer.analyze(
        expressions
    )

    print()
    print("===== TESTE DO SEMÂNTICO =====")

    print("Análise semântica concluída!")

    print()
    print("Tabela de símbolos:")

    for symbol in semantic_analyzer.symbol_table.symbols.values():

        print(
            f"{symbol.name:<15}"
            f"{symbol.address:<10}"
            f"{symbol.type:<15}"
            f"{symbol.scope}"
        )

    print("==============================")
    
def test_semantic_negative():

    source = """
    (print x)
    """

    lexer = Lexer(source)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    expressions = parser.parse()

    semantic_analyzer = SemanticAnalyzer()

    print()
    print("===== TESTE NEGATIVO DO SEMÂNTICO =====")

    try:

        semantic_analyzer.analyze(
            expressions
        )

        print(
            "ERRO: o Semântico deveria "
            "rejeitar a variável 'x'."
        )

    except Exception as e:

        print("Erro detectado corretamente:")
        print(e)