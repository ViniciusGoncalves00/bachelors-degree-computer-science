from lexer import Lexer
from parser import Parser
from semantic import SemanticAnalyzer
from codegen import MEPA
from utils.report import Report

from tests.test_lexer import *
from tests.test_parser import *
from tests.test_semantic import *


def main():
    test_lexer()
    test_lexer_negative()

    test_parser()
    test_parser_negative()

    test_semantic()
    test_semantic_negative()


if __name__ == "__main__":
    main()


source = """
(begin

    (set contador 1)

    (while (<= contador 5)

        (begin

            (if (>= contador 3)
                (print (* contador 10))
                (print contador)
            )

            (set contador (+ contador 1))

        )
    )
)
"""

lexer = Lexer(source)

tokens = lexer.tokenize()

parser = Parser(tokens)

expressions = parser.parse()

semantic_analyzer = SemanticAnalyzer()

semantic_analyzer.analyze(
    expressions
)

generator = MEPA(
    semantic_analyzer.symbol_table
)

code = generator.generate(
    expressions
)

Report.print_tokens(tokens)

Report.print_symbols(
    semantic_analyzer.symbol_table
)

Report.print_code(code)