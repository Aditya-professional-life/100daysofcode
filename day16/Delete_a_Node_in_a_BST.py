def getsucessor(curr,data):
    while curr.left !=None:
        curr = curr.left
    return curr.data

def deleteNode(root, data):
    # code here.
    if root  ==None:
        return 
    if root.data >data:
        root.left = deleteNode(root.left,data)
    elif root.data < data:
        root.right  = deleteNode(root.right,data)
    else:
        if root.left == None:
            return root.right
        elif root.right ==None:
            return root.left
        else:
            succ = getsucessor(root.right,data)
            root.data = succ
            root.right = deleteNode(root.right,succ)
    return root