class TreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


def reConstructBinaryTree(pre, tin):
    """输入前序序列及中序序列"""
    length = len(pre)
    if length == 0:
        return False
    elif length == 1:
        return TreeNode(pre[0])
    else:
        root = TreeNode(pre[0])
        root.lchild = reConstructBinaryTree(pre[1:tin.index(pre[0])+1], tin[:tin.index(pre[0])])
        root.rchild = reConstructBinaryTree(pre[tin.index(pre[0])+1:], tin[tin.index(pre[0])+1:])


if __name__ == '__main__':
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]
    reConstructBinaryTree(pre, tin)
