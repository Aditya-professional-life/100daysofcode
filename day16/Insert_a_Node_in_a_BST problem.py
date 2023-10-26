class Solution:
    #Function to insert a node in a BST. 
    def insert(self,root, Key):
        # code here
        parent = None
        curr = root 
        while curr != None:
            parent = curr
            if curr.data == Key:
                return root
            elif curr.data > Key:
                curr = curr.left
            else:
                curr = curr.right
        if parent == None:
            return Node(Key)
        if parent.data > Key:
            parent.left = Node(Key)
        else:
            parent.right = Node(Key)
            
        return root