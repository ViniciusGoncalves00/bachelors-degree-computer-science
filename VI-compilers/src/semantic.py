from parser import *

class Symbol:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def __repr__(self):
        return f"Symbol({self.name}, {self.type})"


class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def define(self, name, symbol):
        self.symbols[name] = symbol

    def lookup(self, name):
        return self.symbols.get(name)

    def contains(self, name):
        return name in self.symbols


class SemanticAnalyzer:

    def __init__(self):
        self.symbol_table = SymbolTable()

    def analyze(self, expressions):

        for expression in expressions:
            self.analyze_expression(expression)

    def analyze_expression(self, expression):
        if isinstance(expression, NumberExpression):
            return "number"

        if isinstance(expression, IdentifierExpression):
            return self.analyze_identifier(expression)

        if isinstance(expression, ListExpression):
            return self.analyze_list(expression)
        
        if isinstance(expression, BinaryExpression):
            return self.analyze_binary(expression)

        raise Exception(
            f"Expressão desconhecida: {expression}"
        )

    def analyze_identifier(self, expression):

        name = expression.name

        if name in ("+", "-", "*", "/"):
            return "operator"

        symbol = self.symbol_table.lookup(name)

        if symbol is None:
            raise Exception(
                f"Erro semântico: "
                f"variável '{name}' não declarada."
            )

        return symbol.type

    def analyze_list(self, expression):

        elements = expression.elements

        if len(elements) == 0:
            raise Exception(
                "Erro semântico: lista vazia."
            )

        first = elements[0]

        if not isinstance(first, IdentifierExpression):
            raise Exception(
                "Erro semântico: "
                "o primeiro elemento da lista "
                "deve ser um operador."
            )

        operator = first.name

        if operator == "define":
            return self.analyze_define(expression)

        if operator in ("+", "-", "*", "/"):
            return self.analyze_binary_operation(
                expression
            )

        raise Exception(
            f"Erro semântico: "
            f"operação '{operator}' desconhecida."
        )
        
    def analyze_binary(self, expression):
        left_type = self.analyze_expression(
            expression.left
        )

        right_type = self.analyze_expression(
            expression.right
        )

        if left_type != "number":
            raise Exception(
                "Erro semântico: "
                "operando esquerdo deve ser numérico."
            )

        if right_type != "number":
            raise Exception(
                "Erro semântico: "
                "operando direito deve ser numérico."
            )

        return "number"

    def analyze_define(self, expression):

        elements = expression.elements

        if len(elements) != 3:
            raise Exception(
                "Erro semântico: "
                "define espera 2 argumentos."
            )

        name = elements[1]
        value = elements[2]

        if not isinstance(
            name,
            IdentifierExpression
        ):
            raise Exception(
                "Erro semântico: "
                "o nome da variável deve "
                "ser um identificador."
            )

        value_type = self.analyze_expression(
            value
        )

        self.symbol_table.define(
            name.name,
            Symbol(
                name.name,
                value_type
            )
        )

        return value_type

    def analyze_binary_operation(
        self,
        expression
    ):

        elements = expression.elements

        if len(elements) != 3:
            raise Exception(
                "Erro semântico: "
                "operação aritmética espera "
                "2 operandos."
            )

        left = elements[1]
        right = elements[2]

        left_type = self.analyze_expression(left)
        right_type = self.analyze_expression(right)

        if left_type != "number":
            raise Exception(
                "Erro semântico: "
                "primeiro operando deve ser numérico."
            )

        if right_type != "number":
            raise Exception(
                "Erro semântico: "
                "segundo operando deve ser numérico."
            )

        return "number"