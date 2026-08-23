from lexer import Lexer
from parser import Parser
from semantic import SemanticAnalyzer

source = "(+ 10 (* x 2))"

lexer = Lexer(source)
tokens = lexer.tokenize()

parser = Parser(tokens)
expressions = parser.parse()

semantic_analyzer = SemanticAnalyzer()

semantic_analyzer.analyze(expressions)

print("Tabela de símbolos:")

for name, symbol in semantic_analyzer.symbol_table.symbols.items():
    print(name, "->", symbol.type)