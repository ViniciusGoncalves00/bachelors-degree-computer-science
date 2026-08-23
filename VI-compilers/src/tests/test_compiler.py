from lexer import Lexer
from parser import Parser
from semantic import SemanticAnalyzer
from codegen import MEPA
from report import Report


def test_compiler(source):

    print()
    print("=" * 70)
    print("TESTE DE INTEGRAÇÃO")
    print("=" * 70)

    print()
    print("CÓDIGO FONTE")
    print("-" * 70)
    print(source)

    # ========================================================
    # 1. ANÁLISE LÉXICA
    # ========================================================

    lexer = Lexer(source)

    tokens = lexer.tokenize()

    print()
    Report.print_tokens(tokens)

    # ========================================================
    # 2. ANÁLISE SINTÁTICA
    # ========================================================

    parser = Parser(tokens)

    expressions = parser.parse()

    print()
    print("=" * 70)
    print("ÁRVORE SINTÁTICA ABSTRATA")
    print("=" * 70)

    for expression in expressions:
        print(expression.dump())

    # ========================================================
    # 3. ANÁLISE SEMÂNTICA
    # ========================================================

    semantic_analyzer = SemanticAnalyzer()

    semantic_analyzer.analyze(
        expressions
    )

    Report.print_symbols(
        semantic_analyzer.symbol_table
    )

    # ========================================================
    # 4. GERAÇÃO DE CÓDIGO
    # ========================================================

    generator = MEPA(
        semantic_analyzer.symbol_table
    )

    code = generator.generate(
        expressions
    )

    Report.print_code(code)

    print()
    print("=" * 70)
    print("COMPILAÇÃO CONCLUÍDA COM SUCESSO")
    print("=" * 70)