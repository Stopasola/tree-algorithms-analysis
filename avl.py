import time


class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.bf = 0


class AVLTree:

    def __init__(self):
        self.root = None
        self.insertComp = 0
        self.searchComp = 0

    def search_tree_helper(self, node, key):

        self.searchComp = self.searchComp + 1
        if node is None or key == node.data:
            return node

        self.searchComp = self.searchComp + 1
        if key < node.data:
            return self.search_tree_helper(node.left, key)
        return self.search_tree_helper(node.right, key)

    def search_tree(self, k):
        return self.search_tree_helper(self.root, k)

    # update the balance factor the node
    def __update_balance(self, node):

        if node.bf < -1 or node.bf > 1:
            self.__rebalance(node)
            return

        if node.parent is not None:

            if node == node.parent.left:
                node.parent.bf -= 1

            if node == node.parent.right:
                node.parent.bf += 1

            if node.parent.bf != 0:
                self.__update_balance(node.parent)

    # rebalance the tree
    def __rebalance(self, node):

        if node.bf > 0:
            if node.right.bf < 0:
                self.right_rotate(node.right)
                self.__left_rotate(node)
            else:
                self.__left_rotate(node)
        elif node.bf < 0:
            if node.left.bf > 0:
                self.__left_rotate(node.left)
                self.right_rotate(node)
            else:
                self.right_rotate(node)

    # rotate left at node x
    def __left_rotate(self, x):

        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            self.insertComp = self.insertComp + 1
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

        # update the balance factor
        x.bf = x.bf - 1 - max(0, y.bf)
        y.bf = y.bf - 1 + min(0, x.bf)

    # rotate right at node x
    def right_rotate(self, x):
        y = x.left
        x.left = y.right

        if y.right is not None:
            y.right.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

        # update the balance factor
        x.bf = x.bf + 1 - min(0, y.bf)
        y.bf = y.bf + 1 + max(0, x.bf)

    def insert(self, key):
        node = Node(key)
        y = None
        x = self.root

        while x is not None:
            y = x
            self.insertComp = self.insertComp + 1
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        self.insertComp = self.insertComp + 1
        if y is None:
            self.root = node
        elif node.data < y.data:
            self.insertComp = self.insertComp + 1
            y.left = node
        else:
            y.right = node

        self.__update_balance(node)


def initialize_avl(creation_data, search_data):
    bst = AVLTree()
    creation_start_time = time.time()
    for i in creation_data:
        bst.insert(int(i))
    creation_elapsed_time = round(time.time() - creation_start_time, 5)

    search_start_time = time.time()
    for i in search_data:
        bst.search_tree(int(i))
    search_elapsed_time = round(time.time() - search_start_time, 5)

    return {"inset_comp": bst.insertComp, "inset_time": creation_elapsed_time,
            "search_comp": bst.searchComp, "search_time": search_elapsed_time}

