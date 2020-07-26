class Queue():
    def __init__(self):
        self.items=[]
    def enqueue(self,item):
        #print(item)
        self.items.insert(0,item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        return len(self.items)==0
    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
    def __len__(self):
        return self.size()
    def size(self):
        return len(self.items)


class Stack():
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        self.items.pop()
    def is_empty(self):
        return len(self.items) ==0
    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
    def size(self):
        return len(self.items)
    def __len__(self):
        return self.size()



class Node():
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree(object):
    def __init__(self,root):
        self.root=Node(root)

    def print_tree(self,traversal_type):
        if(traversal_type == 'preorder'):
            return self.preorder_print(self.root,"")
        elif (traversal_type == 'postorder'):
            return self.postorder_print(self.root,"")
        elif (traversal_type == 'inorder'):
            return self.inorder_print(self.root,"")
        elif (traversal_type == 'levelorder'):
            return self.levelorder_print(self.root)
        elif(traversal_type == 'reverselevelorder'):
            return self.reverseLevelOrder_print(self.root)
        else:
            return "'un-supported operation"

    def preorder_print(self,start,traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal  = self.preorder_print(start.left,traversal)
            traversal  = self.preorder_print(start.right,traversal)
        return traversal
    
    def postorder_print(self,start,traversal):
        if start:
            traversal  = self.preorder_print(start.left,traversal)
            traversal  = self.preorder_print(start.right,traversal)
            traversal += (str(start.value) + "-")
        return traversal
    
    def inorder_print(self,start,traversal):
        if start:
            traversal  = self.preorder_print(start.left,traversal)
            traversal += (str(start.value) + "-")
            traversal  = self.preorder_print(start.right,traversal)
        return traversal

    
    def levelorder_print(self,start):
        if start is None:
            return
        queue=Queue()
        traversal=""
        queue.enqueue(start)
        while(len(queue)!=0):
            traversal+=str(queue.peek()) + "-"
            node=queue.dequeue()
            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
                queue.enqueue(node.right)
        return traversal

    def reverseLevelOrder_print(self,start):
        if start is None:
            return
        stack=Stack()
        queue=Queue()
        queue.enqueue(start)
        traversal=""
        while (len(queue)!=0):
            node=queue.dequeue()
            stack.push(node)
            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
                queue.enqueue(node.right)
        while (len(stack)!=0):
            traversal+=str(stack.peek()) + "-"
            stack.pop()
        return traversal

    
    def height(self,node):
        if node is None:
            return -1
        left_height=self.height(node.left)
        right_height=self.height(node.right)

        return 1+ max(left_height,right_height)


    #Size of binary tree is the total no of nodes in the tree
    #iterative Approach
    def size(self):
        if self.root is None:
            return 0
        size=0
        queue=Queue()
        queue.enqueue(self.root)
        while len(queue)>0:
            node=queue.dequeue()
            size+=1
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return size


    #Size of binary tree
    #Recursive approch
    def size_recursive(self,node):
        if node is None:
            return 0
        left=self.size_recursive(node.left)
        right=self.size_recursive(node.right)

        return 1+left+right
        

#root=int(input("enter the root element of thr tree="))
tree=BinaryTree(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)

print("Height of binary tree is-"+str(tree.height(tree.root)))
print("size of binary tree is-"+str(tree.size()))
print("size recursive approach of binary tree is-"+str(tree.size_recursive(tree.root)))
print(tree.print_tree("preorder"))
print(tree.print_tree("postorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("levelorder"))
print(tree.print_tree("reverselevelorder"))
