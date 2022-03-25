# Tree Algorithms Analysis

![image](https://img.shields.io/github/languages/top/stopasola/minimum-cost-graph)

## Introduction

In this work, the chronological performance spent in the construction of a Binary Search Tree and an AVL Tree was analyzed, in addition to the time calculation, the number of comparisons performed to build each of the structures was also calculated. After the construction of the structures, the chronological time spent in consulting a certain set of elements present in a file was analyzed. 

## Hardware Methods and Configurations

It was used python 3.7 programming language and a computer with the following specs:

- Operating System: Windows 10 Professional, 64-bit
- Processor: Intel Core i5-4200U CPU @ 1.60GHz
- RAM memory: 8.00GB
- SSD: 230 GB

The analyzed datasets consist of 25 files containing respectively the trees of different sizes.
The  dimensions consist of `50, 100, 200, 300, 500, 750, 1000, 1500, 2000, 3000, 5000, 7500, 10000, 12500, 15000, 20000, 25000, 30000, 40000, 50000, 75000, 100000, 125000, 150000, 175000, 200000, 225000 and 250000`. 

## Implementation

##### Construction Binary Search Tree

To structure the binary search tree we create a class called BSTNode with the following attributes.

```
class BSTNode(object):
    def __init__(self, key, value=None, left=None, right=None, comp_add=0, comp_get=0):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.comp_add = comp_add
        self.comp_get = comp_get
```

The left and right values hold the left and right children of each node respectively. To add values to the binary tree, we use the **add** function as shown below.

```
def add(self, key):
    arvore.comp_add = arvore.comp_add + 2
    side = 'left' if key < self.key else 'right'
    node = getattr(self, side)

    if node is None:
        setattr(self, side, BSTNode(key))
    else:
        node.add(key)
```

The add function in turn checks the key of the requested node to know if the tree should grow to the left or to the right, then compares if any of the left or right nodes is null (to perform the insertion). If yes, a new node is created either to the left or to the right, if not, the add function is called again for a left or right child of the previous node and so on recursively until finding a node with the desired child (left or right) null .

#### AVL Tree Construction

To create the tree, a node structure was created with the following attributes:
```
class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.bf = 0
```

A tree structure was also created, composed of several nodes, according to the work specification, the search and insertion functions of elements were implemented.
To create the popular structure, an insert function was implemented iteratively, performing checks of where the new node of the key sent by parameter, will be allocated in the tree structure. We also implemented the necessary balancing functions for avl.

```
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
```     
        
## Query Binary Tree Search

Querying the binary tree is performed as follows. Firstly, the current key is verified, if it is equal to the key of the analyzed node in question, we return the object containing the information of that node, if not, we verify if the desired key is greater or less than the analyzed current key, to identify for which side should we follow with search. The figure below shows the code of the search function (get).

```
def get(self, key):
    arvore.comp_get = arvore.comp_get + 1
    if self.key == key:
        return self

    arvore.comp_get = arvore.comp_get + 2
    node = self.left if key < self.key else self.right
    if node is not None:
        return node.get(key)
 ```     
                
## AVL Tree Query

The search function was implemented recursively, as can be seen in the figure below.

```
def search_tree_helper(self, node, key):

    self.searchComp = self.searchComp + 1
    if node is None or key == node.data:
        return node

    self.searchComp = self.searchComp + 1
    if key < node.data:
        return self.search_tree_helper(node.left, key)
    return self.search_tree_helper(node.right, key)
 ```     
 
As you can see, the search_tree_helper function performs basic comparisons to check if the key element is equal, greater or less than the analyzed node. In the image we can also check the search_comp attribute, responsible for counting the comparisons.

## Results and discussion

After executing all the build and search files, for the AVL and for the Search Binary Tree, we arrive at the results presented in the graphs below:
 
- Number of comparisons - Creation of structures:

  As can be seen in the graph, the AVL tree in general needed a smaller number of comparisons to   populate its structure, this is due to its balancing mechanism responsible for filling the tree   better, keeping the nodes closer to the root. Without the existing balancing mechanism of the     AVL tree, the binary search tree ends up becoming degenerate, and consequently needs to go down   more levels (perform more comparisons) to insert a certain element.
  
  <p align="center", style="width: 300px height: 150px">
    <img src="https://user-images.githubusercontent.com/17886190/160035084-3303e408-6860-4bc4-9901-384d263655e6.png"/>
  </p>
 

 - Chronological time spent building the structures:

   Overall AVL showed better results as described above, this is due to the balance present in      the    structure. However, there is a computational cost for carrying out the balancing          operations,      which explains why the time difference between the two structures is not as      large as the result seen in the X graph. Another analysis that points to the computational        cost of the balancing operation balancing, is that for the first analyzed files, the binary      tree showed better results, showing that for small data entries the balancing cost ends up        being higher than the insertion cost in an unbalanced tree.
   
    <p align="center", style="width: 300px height: 150px">
      <img src="https://user-images.githubusercontent.com/17886190/160035220-ff339779-f728-4466-b7fd-561ba0cc4b89.png"/>
    </p>

 - Number of comparisons - Query in structures:
 
   As can be seen in graphs 3 and 4, the AVL tree is better for searching elements in an already    populated tree, this is because as the AVL tree has fewer levels from the root to the leaves,    thus the number of comparisons ends up being smaller. Such statement is corroborated because      the AVL implementation is almost identical to the ABB implementation, for the element search.

   <p align="center", style="width: 300px height: 150px">
       <img src="https://user-images.githubusercontent.com/17886190/160035294-2d92eba6-1747-4d50-ba4f-f2706ab1c7c0.png"/>
   </p>
    
    <p align="center", style="width: 300px height: 150px">
      <img src="https://user-images.githubusercontent.com/17886190/160035328-c5c0a1cc-db3e-4bbf-85e8-9877b8bef59d.png"/>
    </p> 


## Conclusion

  After the implementation and analysis of the results, we concluded that the AVL tree is better for both the creation and the search of elements, this is due to the balancing factor present in the AVL, allowing the elements to be better grouped, thus reducing the amount of levels in the tree. However, the binary search tree works satisfactorily for small datasets, as it does not have the computational expense attributed to balancing operations, however, for large datasets this approach ends up becoming unfeasible, as the structure becomes degenerate and ends up having a behavior similar to a sequential search.


## References

[1] [Binary Search Tree in Python](https://pythonhelp.wordpress.com/2015/01/19/arvore-binaria-de-busca-em-python/)

[2] [Python](https://www.python.org/)

[3] [AVL Tree Implementation](https://runestone.academy/runestone/books/published/pythonds/Trees/AVLTreeImplementation.html)
