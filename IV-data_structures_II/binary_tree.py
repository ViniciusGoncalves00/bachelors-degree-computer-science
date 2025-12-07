class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name} ({self.age})"


class Node:
    def __init__(self, person: Person):
        self.person = person
        self.parent = None
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root: Node | None = None

    def insert(self, person: Person):
        new_node = Node(person)

        if self.root is None:
            self.root = new_node
            return

        self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, current: Node, new_node: Node):
        p1 = new_node.person
        p2 = current.person

        if p1.age < p2.age:
            if current.left is None:
                current.left = new_node
                new_node.parent = current
            else:
                self._insert_recursive(current.left, new_node)

        elif p1.age > p2.age:
            if current.right is None:
                current.right = new_node
                new_node.parent = current
            else:
                self._insert_recursive(current.right, new_node)

        else:
            if p1.name < p2.name:
                if current.left is None:
                    current.left = new_node
                    new_node.parent = current
                else:
                    self._insert_recursive(current.left, new_node)
            else:
                if current.right is None:
                    current.right = new_node
                    new_node.parent = current
                else:
                    self._insert_recursive(current.right, new_node)

    def inorder(self, node: Node | None = None):
        if node is None:
            node = self.root

        if node is not None:
            if node.left:
                self.inorder(node.left)

            print(f"Age: {node.person.age} Name: {node.person.name}")

            if node.right:
                self.inorder(node.right)

    def preorder(self, node: Node | None = None):
        if node is None:
            node = self.root

        if node is not None:
            print(f"Age: {node.person.age} Name: {node.person.name}")

            if node.left:
                self.preorder(node.left)

            if node.right:
                self.preorder(node.right)

    def postorder(self, node: Node | None = None):
        if node is None:
            node = self.root

        if node is not None:
            if node.left:
                self.postorder(node.left)

            if node.right:
                self.postorder(node.right)

            print(f"Age: {node.person.age} Name: {node.person.name}")
            
    def print_horizontal(self, node: Node | None = None, prefix: str = "", is_left: bool = True):
        if node is None:
            node = self.root

        if node is not None:
            if node.right:
                self.print_horizontal(node.right, prefix + ("│   " if is_left else "    "), False)

            print(prefix + ("└── " if is_left else "┌── ") + str(node.person))

            if node.left:
                self.print_horizontal(node.left, prefix + ("    " if is_left else "│   "), True)
                
    def print_vertical(self):
        if self.root is None:
            print("Empty tree.")
            return

        from collections import deque

        queue = deque([(self.root, 0)])
        levels: list[list[str]] = []

        while queue:
            node, level = queue.popleft()

            if len(levels) <= level:
                levels.append([])

            levels[level].append(str(node.person))

            if node.left:
                queue.append((node.left, level + 1))

            if node.right:
                queue.append((node.right, level + 1))

        height = len(levels)
        max_width = 2 ** height

        for i, level in enumerate(levels):
            spacing = max_width // (2 ** (i + 1))
            line = (" " * spacing).join(level)
            print(" " * spacing + line)
            
    def inorder_reverse(self, node: Node | None = None):
        if node is None:
            node = self.root

        if node is not None:
            if node.right:
                self.inorder_reverse(node.right)

            print(node.person)

            if node.left:
                self.inorder_reverse(node.left)
                
    def width(self):
        if self.root is None:
            print("Empty tree.")
            return

        from collections import deque

        queue = deque([self.root])

        while queue:
            node = queue.popleft()
            print(node.person)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)