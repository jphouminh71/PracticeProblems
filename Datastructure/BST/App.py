
class Leaf: 
    def __init__(self, value = None, leftChild = None, rightChild = None):
        self.value = value 
        self.leftChild = leftChild
        self.rightChild = rightChild


class BST: 
    def __init__(self):
        self.root = None

    # return the minimum value in the tree, should be on the left side 
    def __findMinHelper(self, parent):
        if parent.leftChild: 
            return self.__findMinHelper(parent.leftChild)
        return parent.value

    def __findMaxHelper(self, parent):
        if parent.rightChild: 
            return self.__findMaxHelper(parent.rightChild)
        return parent.value 
         

    def findMin(self): 
        if self.root is None: 
            print("no minimum of empty tree")
        min = self.__findMinHelper(self.root)
        print("MINIMUM: ",min)

    def findMax(self): 
        if self.root is None: 
            print("no maximum of empty tree")
        min = self.__findMaxHelper(self.root)
        print("MAXIMUM: ",min)

    def __addHelper(self, leafToAdd: Leaf, parent: Leaf): 
        pValue = parent.value 
        nValue = leafToAdd.value 
        isLessE = (nValue <= pValue)
        
        # traverse down 
        if parent.leftChild and parent.rightChild:
            if isLessE:
                self.__addHelper(leafToAdd, parent.leftChild)
            else: 
                self.__addHelper(leafToAdd, parent.rightChild)
        
        # if left but no right
        elif parent.leftChild and not parent.rightChild:
            if isLessE:
                self.__addHelper(leafToAdd, parent.leftChild)
            else: 
                parent.rightChild = leafToAdd
        
        # if right but no left 
        elif parent.rightChild and not parent.leftChild:
            if isLessE:
                parent.leftChild = leafToAdd
            else: 
                self.__addHelper(leafToAdd, parent.rightChild) 
        
        # no child
        elif not parent.leftChild and not parent.rightChild: 
            if isLessE: 
                parent.leftChild = leafToAdd
            else: 
                parent.rightChild = leafToAdd
        
    def addLeaf(self, leaf): 
        if self.root == None: 
            self.root = leaf 
        else: 
            self.__addHelper(leaf, self.root)

    def __removeHelper(self, value, parent, prev=None): 
        if parent is None: 
            print(value, " does not exist in this tree.")
            return

        # look down left subtree / rightsubtree 
        if parent.leftChild and parent.rightChild: 
            if parent.value > value: 
                self.__removeHelper(value, parent.leftChild, parent)
            else: 
                self.__removeHelper(value, parent.rightChild, parent)

        elif parent.value == value:                     
            # Case 1: No children
            if parent.leftChild is None and parent.rightChild is None: 
                if prev.leftChild.value == value: 
                    prev.leftChild = None
                else: 
                    prev.rightChild = None
                
            # Case 2: 1 Child
            elif (parent.leftChild and not parent.rightChild) or (parent.rightChild and not parent.leftChild): 
                if parent.leftChild: 
                    parent.value = parent.leftChild.value
                    parent.leftChild = None 
                elif parent.rightChild: 
                    parent.value = parent.rightChild.value
                    parent.rightChild = None 

            # Case 3: 2 Children
            else: 
                pass

    def removeLeaf(self, value):
        if self.root is None: 
            print("No tree exists.")
        else: 
            self.__removeHelper(value, self.root)

    # pass the root in intially 
    def traverse(self, leaf): 
        if leaf is None:
            return
        print(leaf.value)
        self.traverse(leaf.leftChild)
        self.traverse(leaf.rightChild)        

        

def main():
    bst = BST()

    nineteen = Leaf(19)
    twentyThree = Leaf(23)
    thirtyOne = Leaf(31)
    four = Leaf(4) 
    eleven = Leaf(11) 
    six = Leaf(6) 
    seven = Leaf(7) 
    one = Leaf(1)

    '''
              19 
         4          23 
      1     11          31 
         6
            7
    '''

    seeds = [nineteen,twentyThree, thirtyOne, four, eleven, six, seven, one]
    for seed in seeds: 
        bst.addLeaf(seed)

    toDelete = 1
    bst.traverse(nineteen)
    print("Deleting: ", toDelete)
    bst.removeLeaf(toDelete)
    
    #bst.findMin()
    #bst.findMax()
    
    print("-----Traversing-----")
    bst.traverse(nineteen)

main()
