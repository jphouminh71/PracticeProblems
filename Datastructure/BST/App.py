
class Leaf: 
    def __init__(self, value = None, leftChild = None, rightChild = None):
        self.value = value 
        self.leftChild = leftChild
        self.rightChild = rightChild


class BST: 
    def __init__(self):
        self.root = None

    def addHelper(self, leafToAdd: Leaf, parent: Leaf): 
        pValue = parent.value 
        nValue = leafToAdd.value 
        isLessE = (nValue <= pValue)
        
        # traverse down 
        if parent.leftChild and parent.rightChild:
            if isLessE:
                self.addHelper(leafToAdd, parent.leftChild)
            else: 
                self.addHelper(leafToAdd, parent.rightChild)
        
        # if left but no right
        elif parent.leftChild and not parent.rightChild:
            if isLessE:
                self.addHelper(leafToAdd, parent.leftChild)
            else: 
                parent.rightChild = leafToAdd
        
        # if right but no left 
        elif parent.rightChild and not parent.leftChild:
            if isLessE:
                parent.leftChild = leafToAdd
            else: 
                self.addHelper(leafToAdd, parent.rightChild) 
        
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
            self.addHelper(leaf, self.root)

    # find the spot then replace with one of its child accordingly 
    def removeLeaf(self, value):
        pass

    # pass the root in intially 
    def traverse(self, leaf): 
        if leaf is None:
            return
        print(leaf.value)
        self.traverse(leaf.leftChild)
        self.traverse(leaf.rightChild)        

    # return the minimum value in the tree, should be on the left side 
    def findMinHelper(self, parent):
        if parent.leftChild: 
            return self.findMinHelper(parent.leftChild)
        return parent.value

    def findMaxHelper(self, parent):
        if parent.rightChild: 
            return self.findMaxHelper(parent.rightChild)
        return parent.value 
         

    def findMin(self): 
        if self.root is None: 
            print("no minimum of empty tree")
        min = self.findMinHelper(self.root)
        print("MINIMUM: ",min)

    def findMax(self): 
        if self.root is None: 
            print("no maximum of empty tree")
        min = self.findMaxHelper(self.root)
        print("MAXIMUM: ",min)
        

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
    bst.findMin()
    bst.findMax()
    
    #print("-----Traversing-----")
    #bst.traverse(nineteen)

main()
