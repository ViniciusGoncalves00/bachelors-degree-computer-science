class NumberExpression:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Number({self.value})"

    def dump(self, indent=0):
        return " " * indent + f"Number({self.value})"


class IdentifierExpression:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Identifier({self.name})"

    def dump(self, indent=0):
        return " " * indent + f"Identifier({self.name})"


class BinaryExpression:
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Binary({self.operator}, {self.left}, {self.right})"

    def dump(self, indent=0):
        result = " " * indent + f"Binary({self.operator})\n"

        result += self.left.dump(indent + 2)
        result += "\n"
        result += self.right.dump(indent + 2)

        return result


class SetExpression:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"Set({self.name}, {self.value})"

    def dump(self, indent=0):
        result = " " * indent + f"Set({self.name})\n"
        result += self.value.dump(indent + 2)

        return result


class PrintExpression:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Print({self.value})"

    def dump(self, indent=0):
        result = " " * indent + "Print\n"
        result += self.value.dump(indent + 2)

        return result


class BeginExpression:
    def __init__(self, expressions):
        self.expressions = expressions

    def __repr__(self):
        return f"Begin({self.expressions})"

    def dump(self, indent=0):
        result = " " * indent + "Begin\n"

        for expression in self.expressions:
            result += expression.dump(indent + 2)
            result += "\n"

        return result.rstrip()


class IfExpression:
    def __init__(
        self,
        condition,
        then_branch,
        else_branch
    ):
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

    def dump(self, indent=0):
        result = " " * indent + "If\n"

        result += " " * (indent + 2) + "Condition\n"
        result += self.condition.dump(indent + 4)
        result += "\n"

        result += " " * (indent + 2) + "Then\n"
        result += self.then_branch.dump(indent + 4)
        result += "\n"

        result += " " * (indent + 2) + "Else\n"
        result += self.else_branch.dump(indent + 4)

        return result


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

    def dump(self, indent=0):
        result = " " * indent + "While\n"

        result += " " * (indent + 2) + "Condition\n"
        result += self.condition.dump(indent + 4)
        result += "\n"

        result += " " * (indent + 2) + "Body\n"
        result += self.body.dump(indent + 4)

        return result