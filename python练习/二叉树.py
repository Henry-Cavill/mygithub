from _collections import deque


class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


a = BiTreeNode('A')
b = BiTreeNode('B')
c = BiTreeNode('C')
d = BiTreeNode('D')
e = BiTreeNode('E')
f = BiTreeNode('F')
g = BiTreeNode('G')

e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f

root = e

def pre_order(root):
    """前序遍历"""
    deque = []

    def helper(root):
        if not root:
            return
        deque.append(root.data)
        helper(root.lchild)
        helper(root.rchild)
    helper(root)
    return deque

if __name__ == '__main__':
    print(pre_order(root))
    # def in_order(root):
    #     """中序遍历"""
    #     if root:
    #         in_order(root.lchild)
    #         print(root.data, end='')
    #         in_order(root.rchild)
    #
    #
    # def post_order(root):
    #     """后续遍历"""
    #     if root:
    #         post_order(root.lchild)
    #         post_order(root.rchild)
    #         print(root.data, end='')
    #
    #
    # def level_order(root):
    #     q = deque()
    #     q.append(root)
    #     while len(q) > 0:
    #         x = q.popleft()
    #         print(x.data, end='')
    #         if x.lchild:
    #             q.append(x.lchild)
    #         if x.rchild:
    #             q.append(x.rchild)
    #
    #
    # pre_order(root)
    # print('\n')
    # in_order(root)
    # print('\n')
    # post_order(root)
