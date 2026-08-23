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
    
class SetExpression:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"Set({self.name}, {self.value})"


class PrintExpression:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Print({self.value})"

class BeginExpression:
    def __init__(self, expressions):
        self.expressions = expressions

    def __repr__(self):
        return f"Begin({self.expressions})"

class IfExpression:
    def __init__(self, condition, then_branch, else_branch):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch

    def __repr__(self):
        return (
            f"If("
            f"condition={self.condition}, "
            f"then={self.then_branch}, "
            f"else={self.else_branch}"
            f")"
        )

class WhileExpression:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def __repr__(self):
        return (
            f"While("
            f"condition={self.condition}, "
            f"body={self.body}"
            f")"
        )