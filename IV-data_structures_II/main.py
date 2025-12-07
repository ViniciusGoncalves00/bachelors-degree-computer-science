from binary_tree import Person, BinaryTree

people = [
    Person("Ana", 18),
    Person("Maria", 19),
    Person("Marina", 20),
    Person("Mariana", 21),
    Person("Julia", 22),
    Person("Juliana", 23),
    Person("Elisa", 24),
    Person("Elisângela", 25),
    Person("Rosa", 26),
    Person("Rosângela", 27),
    Person("Lidia", 28),
    Person("Lidiane", 29),
    Person("Pedro", 21),
    Person("João", 22),
    Person("Tiago", 23),
    Person("André", 24),
    Person("Filipe", 25),
    Person("Bartolomeu", 26),
    Person("Mateus", 27),
    Person("Tomé", 28),
    Person("Tiago", 29),
    Person("Tadeu", 30),
    Person("Simão", 31),
    Person("Judas", 32),
    Person("Jesus", 33),
]

tree = BinaryTree()

for person in people:
    tree.insert(person)

print("")
print("In Order:")
tree.inorder()

print("")
print("Pre Order:")
tree.preorder()

print("")
print("Post Order:")
tree.postorder()

print("")
print("In Reverse Order:")
tree.inorder_reverse()

print("")
print("Width:")
tree.width()