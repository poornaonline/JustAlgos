from random import randrange

class Node:

    def __init__(self, internal_number_provided):
        self.internal_number = internal_number_provided
        self.left_node = None
        self.right_node = None

    def addNode(self, new_node):
        if self.internal_number > new_node.internal_number:
            print("New node " + str(new_node.internal_number) + " is smaller than internal number " + str(
                self.internal_number))
            if self.left_node is None:
                print("Left node is None and adding it to the left node")
                self.left_node = new_node
            else:
                print("Left node is NOT None --> Going inside the Left node")
                self.left_node.addNode(new_node)
        elif self.internal_number < new_node.internal_number:
            print("New node " + str(new_node.internal_number) + " is larger than internal number " + str(
                self.internal_number))
            if self.right_node is None:
                print("Right node is None and adding it to the Right node")
                self.right_node = new_node
            else:
                print("Right node is NOT None --> Going inside the Right node")
                self.right_node.addNode(new_node)
        else:
            print("Number is already exist in the graph cannot exist")

n1 = Node(10)
n2 = Node(20)
n3 = Node(5)
n4 = Node(30)
n5 = Node(15)
n6 = Node(22)

n1.addNode(n2)
n1.addNode(n3)
n1.addNode(n4)
n1.addNode(n5)
n1.addNode(n6)
n1.addNode(n3)

num = 0

while (num < 1000):
    random_number = randrange(10000)
    random_node = Node(random_number)
    n1.addNode(random_node)
    num = num + 1

print("End")