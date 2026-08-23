from lexer import Lexer
from parser import Parser
from semantic import SemanticAnalyzer

source = """
(begin
 (set a 10)
 (set b 20)
 (print (+ a b)))
"""

lexer = Lexer(source)
tokens = lexer.tokenize()

parser = Parser(tokens)
expressions = parser.parse()

semantic_analyzer = SemanticAnalyzer()

semantic_analyzer.analyze(expressions)

print("Tabela de símbolos:")

for name, symbol in semantic_analyzer.symbol_table.symbols.items():
    print(name, "->", symbol.type)