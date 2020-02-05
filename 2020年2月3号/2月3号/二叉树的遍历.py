class TreeNode():
    def __init__(self, node):
        self.node = node
        self.left = None
        self.right = None


one_node = TreeNode('A')
two_node = TreeNode('B')
three_node = TreeNode('C')
four_node = TreeNode('D')
five_node = TreeNode('E')
six_node = TreeNode('F')
seven_node = TreeNode('G')

one_node.left = two_node
one_node.right = three_node
two_node.left = four_node
two_node.right = five_node
three_node.left = six_node
three_node.right = seven_node

root = one_node



def preorder(root):
    deque = []
    def helper(root):
        if not root:
            return
        deque.append(root.node)
        helper(root.left)
        helper(root.right)
    helper(root)
    return deque

print(preorder(root))