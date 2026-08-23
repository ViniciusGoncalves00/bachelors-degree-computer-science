from enum import Enum, auto


class TokenType(Enum):
    LPAREN = auto()
    RPAREN = auto()

    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()

    GREATER_EQUAL = auto()
    GREATER_THAN = auto()
    LESS_EQUAL = auto()
    LESS_THAN = auto()

    NUMBER = auto()
    IDENTIFIER = auto()

    EOF = auto()
    
class Token:
    def __init__(self, type, lexeme, line, column):
        self.type = type
        self.lexeme = lexeme
        self.line = line
        self.column = column

    def __repr__(self):
        return f"Token({self.type.name}, {self.lexeme!r})"
    
class Lexer:
    def __init__(self, source):
        self.source = source

        self.start = 0
        self.current = 0

        self.line = 1
        self.column = 1

        self.tokens = []

    def tokenize(self):
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        self.tokens.append(
            Token(TokenType.EOF, "", self.line, self.column)
        )

        return self.tokens
    
    def scan_token(self):
        c = self.advance()

        if c == '(':
            self.add_token(TokenType.LPAREN)

        elif c == ')':
            self.add_token(TokenType.RPAREN)

        elif c == '+':
            self.add_token(TokenType.PLUS)

        elif c == '-':
            self.add_token(TokenType.MINUS)

        elif c == '*':
            self.add_token(TokenType.MULTIPLY)

        elif c == '/':
            self.add_token(TokenType.DIVIDE)

        elif c.isspace():
            pass

        elif c.isdigit():
            self.number()

        elif c.isalpha():
            self.identifier()
            
        elif c == '>':
            if self.peek() == '=':
                self.advance()
                self.add_token(TokenType.GREATER_EQUAL)
            else:
                self.add_token(TokenType.GREATER_THAN)

        elif c == '<':
            if self.peek() == '=':
                self.advance()
                self.add_token(TokenType.LESS_EQUAL)
            else:
                self.add_token(TokenType.LESS_THAN)

        else:
            raise Exception(
                f"Caractere inesperado '{c}' "
                f"na linha {self.line}, coluna {self.column}"
            )
            
    def advance(self):
        c = self.source[self.current]
        self.current += 1

        if c == '\n':
            self.line += 1
            self.column = 1
        else:
            self.column += 1

        return c
    
    def peek(self):
        if self.is_at_end():
            return '\0'

        return self.source[self.current]
    
    def number(self):
        while self.peek().isdigit():
            self.advance()

        self.add_token(TokenType.NUMBER)
        
    def identifier(self):
        while self.peek().isalnum() or self.peek() == '_':
            self.advance()

        self.add_token(TokenType.IDENTIFIER)
        
    def add_token(self, type):
        lexeme = self.source[self.start:self.current]

        self.tokens.append(
            Token(
                type,
                lexeme,
                self.line,
                self.column
            )
        )
        
    def is_at_end(self):
        return self.current >= len(self.source)