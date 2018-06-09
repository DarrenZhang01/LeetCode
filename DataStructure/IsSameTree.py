def isSameTree(self, p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if (p == None and q == None):
        return True
    if (p == None and q != None) or (p != None and q == None):
        return False
    if (p.val != q.val):
        return False
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
