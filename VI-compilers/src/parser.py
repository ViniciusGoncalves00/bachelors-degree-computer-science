from lexer import Lexer, TokenType

class NumberExpression:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Number({self.value})"
    
class IdentifierExpression:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Identifier({self.name})"
    
class ListExpression:
    def __init__(self, elements):
        self.elements = elements

    def __repr__(self):
        return f"List({self.elements})"
    
class BinaryExpression:
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Binary({self.operator}, {self.left}, {self.right})"
    
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
            "Esperado '('"
        )
    
        operator = self.advance()
    
        if operator.type not in (
            TokenType.PLUS,
            TokenType.MINUS,
            TokenType.MULTIPLY,
            TokenType.DIVIDE
        ):
            raise Exception(
                f"Operador inesperado: {operator}"
            )
    
        left = self.expression()
        right = self.expression()
    
        self.consume(
            TokenType.RPAREN,
            "Esperado ')'"
        )
    
        return BinaryExpression(
            operator.type,
            left,
            right
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

        raise Exception(message)

    def is_at_end(self):
        return self.peek().type == TokenType.EOF