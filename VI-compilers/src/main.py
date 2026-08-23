from lexer import Lexer
from parser import Parser
from semantic import SemanticAnalyzer
from codegen import MEPA
from report import Report

from tests.test_lexer import test_lexer
from tests.test_parser import test_parser
from tests.test_semantic import test_semantic


def main():
    test_lexer()
    test_parser()
    test_semantic()


if __name__ == "__main__":
    main()


source = """
(begin

    (set a 10)
    (set b 20)

    (print (+ a b))

)
"""


# ============================================================
# LEXER
# ============================================================

lexer = Lexer(source)

tokens = lexer.tokenize()


# ============================================================
# PARSER
# ============================================================

parser = Parser(tokens)

expressions = parser.parse()


# ============================================================
# SEMANTIC ANALYZER
# ============================================================

semantic_analyzer = SemanticAnalyzer()

semantic_analyzer.analyze(
    expressions
)


# ============================================================
# CODE GENERATOR
# ============================================================

generator = MEPA(
    semantic_analyzer.symbol_table
)

code = generator.generate(
    expressions
)


# ============================================================
# REPORTS
# ============================================================

Report.print_tokens(tokens)

Report.print_symbols(
    semantic_analyzer.symbol_table
)

Report.print_code(code)