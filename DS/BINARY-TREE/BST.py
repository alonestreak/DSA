class Node():
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None


class BST():
    def __init__(self):
        self.root=None

    def insert(self,data):
        if self.root is None:
            self.root=Node(data)
        else:
            self.insert_(data,self.root)

    def insert_(self,data,cur_node):
        if data< cur_node.data:
            if cur_node.left is None:
                cur_node.left=Node(data)
            else:
                self.insert_(data,cur_node.left)

        elif data> cur_node.data:
            if cur_node.right is None:
                cur_node.right=Node(data)
            else:
                self.insert_(data,cur_node.right)
        else:
            print("Value already present in the tree")

    def find(self,data):
        if self.root:
            is_found=self._find(data,self.root)
            if is_found:
                print("given data was present in the tree")
            else:
                print("data was not preset in the tree")
        else:
            print("tree is empty")
    def _find(self,data,cur_node):
        is_found=False
        if data > cur_node.data and cur_node.right:
            is_found=self._find(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:
            is_found=self._find(data, cur_node.left)
        if data== cur_node.data:
            return True
        return is_found
            
bst=BST()
bst.insert(5)
bst.insert(6)
bst.insert(4)
bst.insert(8)
bst.find(87)
            

            
