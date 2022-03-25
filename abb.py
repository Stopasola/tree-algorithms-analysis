import time


def initialize_abb(creation_data, search_data):
    class BSTNode(object):
        def __init__(self, key, value=None, left=None, right=None, comp_add=0, comp_get=0):
            self.key = key
            self.value = value
            self.left = left
            self.right = right
            self.comp_add = comp_add
            self.comp_get = comp_get

        def get(self, key):
            arvore.comp_get = arvore.comp_get + 1
            if self.key == key:
                return self

            arvore.comp_get = arvore.comp_get + 2
            node = self.left if key < self.key else self.right
            if node is not None:
                return node.get(key)

        def add(self, key):
            arvore.comp_add = arvore.comp_add + 2
            side = 'left' if key < self.key else 'right'
            node = getattr(self, side)

            if node is None:
                setattr(self, side, BSTNode(key))
            else:
                node.add(key)

    creation_start_time = time.time()

    arvore = BSTNode(creation_data[0])
    for x in range(1, len(creation_data)):
        y = creation_data[x]
        arvore.add(y)

    creation_elapsed_time = round(time.time() - creation_start_time, 5)

    search_start_time = time.time()

    for i in search_data:
        arvore.get(i)

    search_elapsed_time = round(time.time() - search_start_time, 5)

    return {"inset_comp": arvore.comp_add, "inset_time": creation_elapsed_time,
            "search_comp": arvore.comp_get, "search_time": search_elapsed_time}

