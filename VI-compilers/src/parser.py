from utils.expressions import *
from lexer import Lexer, TokenType

class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def parse(self):
        expressions = []

        while not self.is_at_end():
            expressions.append(
                self.expression()
            )

        return expressions

    def expression(self):
        token = self.peek()

        if token.type == TokenType.NUMBER:
            return self.number()

        if token.type == TokenType.IDENTIFIER:
            return self.identifier()

        if token.type == TokenType.LPAREN:
            return self.list()

        raise Exception(
            f"Token inesperado: {token}"
        )

    def number(self):
        token = self.advance()

        return NumberExpression(
            int(token.lexeme)
        )

    def identifier(self):
        token = self.advance()

        return IdentifierExpression(
            token.lexeme
        )

    def list(self):

        self.consume(
            TokenType.LPAREN,
            "Esperado '('."
        )

        if self.check(TokenType.RPAREN):
            raise Exception(
                "Lista vazia não é permitida."
            )

        operator = self.advance()

        if operator.type in (
            TokenType.PLUS,
            TokenType.MINUS,
            TokenType.MULTIPLY,
            TokenType.DIVIDE,
        ):
            return self.binary_expression(
                operator
            )

        if operator.type in (
            TokenType.GREATER_EQUAL,
            TokenType.GREATER_THAN,
            TokenType.LESS_EQUAL,
            TokenType.LESS_THAN,
        ):
            return self.binary_expression(
                operator
            )

        if operator.type == TokenType.IDENTIFIER:

            if operator.lexeme == "print":
                return self.print_expression()

            if operator.lexeme == "set":
                return self.set_expression()

            if operator.lexeme == "begin":
                return self.begin_expression()

            if operator.lexeme == "if":
                return self.if_expression()

            if operator.lexeme == "while":
                return self.while_expression()

        raise Exception(
            f"Operador ou forma especial desconhecida: "
            f"{operator.lexeme}"
        )

    def binary_expression(self, operator):

        left = self.expression()

        right = self.expression()

        self.consume(
            TokenType.RPAREN,
            "Esperado ')'."
        )

        return BinaryExpression(
            operator.lexeme,
            left,
            right
        )

    def print_expression(self):

        value = self.expression()

        self.consume(
            TokenType.RPAREN,
            "Esperado ')'."
        )

        return PrintExpression(
            value
        )

    def set_expression(self):

        name = self.consume(
            TokenType.IDENTIFIER,
            "Esperado identificador após 'set'."
        )

        value = self.expression()

        self.consume(
            TokenType.RPAREN,
            "Esperado ')'."
        )

        return SetExpression(
            name.lexeme,
            value
        )

    def begin_expression(self):

        expressions = []

        while (
            not self.check(TokenType.RPAREN)
            and not self.is_at_end()
        ):
            expressions.append(
                self.expression()
            )

        self.consume(
            TokenType.RPAREN,
            "Esperado ')'."
        )

        return BeginExpression(
            expressions
        )

    def if_expression(self):

        condition = self.expression()

        then_branch = self.expression()

        else_branch = self.expression()

        self.consume(
            TokenType.RPAREN,
            "Esperado ')'."
        )

        return IfExpression(
            condition,
            then_branch,
            else_branch
        )

    def while_expression(self):

        condition = self.expression()

        body = self.expression()

        self.consume(
            TokenType.RPAREN,
            "Esperado ')'."
        )

        return WhileExpression(
            condition,
            body
        )

    def peek(self):
        return self.tokens[self.current]

    def advance(self):

        token = self.tokens[self.current]

        if not self.is_at_end():
            self.current += 1

        return token

    def check(self, token_type):

        if self.is_at_end():
            return False

        return self.peek().type == token_type

    def consume(self, token_type, message):

        if self.check(token_type):
            return self.advance()

        raise Exception(
            message
        )

    def is_at_end(self):

        return self.peek().type == TokenType.EOF