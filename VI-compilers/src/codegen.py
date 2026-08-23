from expressions import *


class MEPA:
    def __init__(self, symbol_table):

        self.symbol_table = symbol_table

        self.code = []
        self.label_count = 0

    # ========================================================
    # EMIT
    # ========================================================

    def emit(self, instruction):
        self.code.append(instruction)

    # ========================================================
    # LABELS
    # ========================================================

    def new_label(self):
        label = f"L{self.label_count}"
        self.label_count += 1

        return label

    def emit_label(self, label):
        self.emit(f"{label}:")

    # ========================================================
    # GENERATE
    # ========================================================

    def generate(self, expressions):

        for expression in expressions:
            self.generate_expression(expression)

        return self.code

    # ========================================================
    # EXPRESSIONS
    # ========================================================

    def generate_expression(self, expression):

        if isinstance(expression, NumberExpression):
            return self.generate_number(expression)

        if isinstance(expression, IdentifierExpression):
            return self.generate_identifier(expression)

        if isinstance(expression, BinaryExpression):
            return self.generate_binary(expression)

        if isinstance(expression, SetExpression):
            return self.generate_set(expression)

        if isinstance(expression, PrintExpression):
            return self.generate_print(expression)

        if isinstance(expression, BeginExpression):
            return self.generate_begin(expression)

        if isinstance(expression, IfExpression):
            return self.generate_if(expression)

        if isinstance(expression, WhileExpression):
            return self.generate_while(expression)

        raise Exception(
            f"Expressão desconhecida: {expression}"
        )

    # ========================================================
    # NUMBER
    # ========================================================

    def generate_number(self, expression):

        self.emit(
            f"CRCT {expression.value}"
        )

    # ========================================================
    # IDENTIFIER
    # ========================================================

    def generate_identifier(self, expression):

        self.emit(
            f"CRVL {expression.name}"
        )

    # ========================================================
    # BINARY
    # ========================================================

    def generate_binary(self, expression):

        # Gera primeiro o lado esquerdo
        self.generate_expression(
            expression.left
        )

        # Depois o lado direito
        self.generate_expression(
            expression.right
        )

        operator = expression.operator

        if operator == "+":
            self.emit("SOMA")

        elif operator == "-":
            self.emit("SUBT")

        elif operator == "*":
            self.emit("MULT")

        elif operator == "/":
            self.emit("DIVI")

        elif operator == ">":
            self.emit("CMMA")

        elif operator == ">=":
            self.emit("CMAG")

        elif operator == "<":
            self.emit("CMME")

        elif operator == "<=":
            self.emit("CMEG")

        else:
            raise Exception(
                f"Operador desconhecido: {operator}"
            )

    # ========================================================
    # SET
    # ========================================================

    def generate_set(self, expression):

        self.generate_expression(
            expression.value
        )

        self.emit(
            f"ARMZ {expression.name}"
        )

    # ========================================================
    # PRINT
    # ========================================================

    def generate_print(self, expression):

        self.generate_expression(
            expression.value
        )

        self.emit("IMPR")

    # ========================================================
    # BEGIN
    # ========================================================

    def generate_begin(self, expression):

        for statement in expression.expressions:

            self.generate_expression(
                statement
            )

    # ========================================================
    # IF
    # ========================================================

    def generate_if(self, expression):

        else_label = self.new_label()
        end_label = self.new_label()

        # Calcula condição
        self.generate_expression(
            expression.condition
        )

        # Se falso, vai para ELSE
        self.emit(
            f"DSVF {else_label}"
        )

        # THEN
        self.generate_expression(
            expression.then_branch
        )

        # Pula o ELSE
        self.emit(
            f"DSVS {end_label}"
        )

        # ELSE
        self.emit_label(
            else_label
        )

        self.generate_expression(
            expression.else_branch
        )

        # Fim
        self.emit_label(
            end_label
        )

    # ========================================================
    # WHILE
    # ========================================================

    def generate_while(self, expression):

        start_label = self.new_label()
        end_label = self.new_label()

        # Início do loop
        self.emit_label(
            start_label
        )

        # Calcula condição
        self.generate_expression(
            expression.condition
        )

        # Se falso, termina
        self.emit(
            f"DSVF {end_label}"
        )

        # Corpo
        self.generate_expression(
            expression.body
        )

        # Volta para o início
        self.emit(
            f"DSVS {start_label}"
        )

        # Fim
        self.emit_label(
            end_label
        )