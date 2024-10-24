class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self,value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_node(self.root,value)
            
    def insert_node(self, node1 , value):
        if value < node1.value:
            if node1.left is None:
                node1.left = Node(value)
            else:
                self.insert_node(node1.left, value)
        elif value > node1.value:
            if node1.right is None:
                node1.right = Node(value)
            else:
                self.insert_node(node1.right, value)
                
    def delete(self, value):
        self.root = self.delete_node(self.root,value)
        
    def delete_node(self,node,value):
        if node is None:
            return node
        if value < node.value:
            node.left = self.delete_node(node.left,value)
        elif value > node.value:
            node.right = self.delete_node(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
        return node
    
    def preorder(self,node1):
        if node1:
            print(node1.value, end=" ")
            self.preorder(node1.left)
            self.preorder(node1.right)
    
    def postorder(self, node1):
        if node1:
            self.postorder(node1.left)
            self.postorder(node1.right)
            print(node1.value, end= " ")
            
    def inorder(self,node1):
        if node1:
            self.inorder(node1.left)
            print(node1.value, end= " ")
            self.inorder(node1.right)
            
            
tree =BinaryTree()
tree_ = [10,20,80,78,90,30,45,40,100,50]
for n in tree_:
    tree.insert(n)

print("PreOrder Traversal: ")
tree.preorder(tree.root)
print("\nInorder Traversal: ")
tree.inorder(tree.root)
print("\nPostOrder Traversal: ")
tree.postorder(tree.root)

tree.delete(78)
print("\nPreorder Traversal after deleting node 78: ")
tree.preorder(tree.root)