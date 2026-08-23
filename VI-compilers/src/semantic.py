from utils.expressions import *

class Symbol:

    def __init__(
        self,
        name,
        type,
        address,
        scope
    ):
        self.name = name
        self.type = type
        self.address = address
        self.scope = scope

    def __repr__(self):

        return (
            f"Symbol("
            f"name={self.name}, "
            f"type={self.type}, "
            f"address={self.address}, "
            f"scope={self.scope}"
            f")"
        )


class SymbolTable:

    def __init__(self):

        self.symbols = {}

        self.next_address = 0

    def define(self, name, type, scope="global"):

        if name in self.symbols:

            symbol = self.symbols[name]

            symbol.type = type

            return symbol

        symbol = Symbol(
            name,
            type,
            self.next_address,
            scope
        )

        self.symbols[name] = symbol

        self.next_address += 1

        return symbol

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

        if isinstance(expression, BinaryExpression):
            return self.analyze_binary(expression)

        if isinstance(expression, SetExpression):
            return self.analyze_set(expression)

        if isinstance(expression, PrintExpression):
            return self.analyze_print(expression)

        if isinstance(expression, BeginExpression):
            return self.analyze_begin(expression)

        if isinstance(expression, IfExpression):
            return self.analyze_if(expression)

        if isinstance(expression, WhileExpression):
            return self.analyze_while(expression)

        raise Exception(
            f"Expressão desconhecida: {expression}"
        )

    def analyze_identifier(self, expression):

        symbol = self.symbol_table.lookup(
            expression.name
        )

        if symbol is None:
            raise Exception(
                f"Erro semântico: "
                f"variável '{expression.name}' "
                f"não declarada."
            )

        return symbol.type

    def analyze_binary(self, expression):

        left_type = self.analyze_expression(
            expression.left
        )

        right_type = self.analyze_expression(
            expression.right
        )

        operator = expression.operator

        if operator in (
            "+",
            "-",
            "*",
            "/"
        ):

            if left_type != "number":
                raise Exception(
                    f"Erro semântico: "
                    f"operador '{operator}' "
                    f"espera um número à esquerda."
                )

            if right_type != "number":
                raise Exception(
                    f"Erro semântico: "
                    f"operador '{operator}' "
                    f"espera um número à direita."
                )

            return "number"

        if operator in (
            ">",
            ">=",
            "<",
            "<="
        ):

            if left_type != "number":
                raise Exception(
                    f"Erro semântico: "
                    f"operador '{operator}' "
                    f"espera um número à esquerda."
                )

            if right_type != "number":
                raise Exception(
                    f"Erro semântico: "
                    f"operador '{operator}' "
                    f"espera um número à direita."
                )

            return "boolean"

        raise Exception(
            f"Erro semântico: "
            f"operador '{operator}' desconhecido."
        )

    def analyze_set(self, expression):
        value_type = self.analyze_expression(
            expression.value
        )
    
        self.symbol_table.define(
            expression.name,
            value_type,
            "global"
        )
    
        return value_type

    def analyze_print(self, expression):

        self.analyze_expression(
            expression.value
        )

        return "void"

    def analyze_begin(self, expression):

        for statement in expression.expressions:

            self.analyze_expression(
                statement
            )

        return "void"

    def analyze_if(self, expression):

        condition_type = self.analyze_expression(
            expression.condition
        )

        if condition_type != "boolean":
            raise Exception(
                "Erro semântico: "
                "a condição do 'if' "
                "deve ser booleana."
            )

        self.analyze_expression(
            expression.then_branch
        )

        self.analyze_expression(
            expression.else_branch
        )

        return "void"

    def analyze_while(self, expression):

        condition_type = self.analyze_expression(
            expression.condition
        )

        if condition_type != "boolean":
            raise Exception(
                "Erro semântico: "
                "a condição do 'while' "
                "deve ser booleana."
            )

        self.analyze_expression(
            expression.body
        )

        return "void"