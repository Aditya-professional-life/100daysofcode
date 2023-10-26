def bstDelete(root, data):

    parent = None
    curr = root

    # Search for the node to be deleted
    while curr and curr.data != data:
        parent = curr
        if curr.data > data:
            curr = curr.left
        else:
            curr = curr.right

    if curr is None:
        return root  # Data not found, no changes needed

    # Node with the data found, handle different cases
    if curr.left is None and curr.right is None:
        # Case 1: Node has no children
        if parent is None:
            return None
        if parent.left == curr:
            parent.left = None
        else:
            parent.right = None

    elif curr.left is None or curr.right is None:
        # Case 2: Node has one child
        child = curr.left if curr.left is not None else curr.right
        if parent is None:
            return child
        if parent.left == curr:
            parent.left = child
        else:
            parent.right = child

    else:
        # Case 3: Node has two children
        successor = curr.right
        successor_parent = curr
        while successor.left:
            successor_parent = successor
            successor = successor.left
        curr.data = successor.data
        if successor_parent.left == successor:
            successor_parent.left = successor.right
        else:
            successor_parent.right = successor.right

    return root
