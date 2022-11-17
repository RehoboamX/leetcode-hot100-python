# 定义树的数据结构
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Q94: 二叉树的中序遍历
def inorderTraversal(root):  # 递归法
    if not root:  # 如果树节点为空，则返回空列表
        return []
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)


# Q101: 对称二叉树
def isSymmetric(root):  # 递归法
    if not root:
        return True

    def dfs(left, right):
        # 1.两节点都为空时循环结束
        # 2.一个节点为空或两节点值不等时返回False
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        elif left.val != right.val:
            return False
        return dfs(left.left, right.right) and dfs(left.right, right.left)

    return dfs(root.left, root.right)


# Q104: 二叉树的最大深度
def maxDepth(root):  # 递归法
    if not root:
        return 0
    leftHeight = maxDepth(root.left)
    rightHeight = maxDepth(root.right)
    return max(leftHeight, rightHeight) + 1


# Q226: 翻转二叉树
def invertTree(root):
    if not root:  # 递归函数的终止条件
        return None
    root.left, root.right = root.right, root.left  # 交换左右节点
    invertTree(root.left)
    invertTree(root.right)
    return root


# Q543: 二叉树的直径
def diameterOfBinaryTree(root):
    def getDiamDepth(node):
        if not node:
            return 0, 0  # 返回的两个值分别为直径和深度
        leftDiam, leftDepth = getDiamDepth(node.left)
        rightDiam, rightDepth = getDiamDepth(node.right)
        depth = 1 + max(leftDepth, rightDepth)  # 得到二叉树的深度
        diam = max(leftDiam, rightDiam, leftDepth+rightDepth+1)
        return diam, depth
    dia, dep = getDiamDepth(root)
    return dia


# Q617: 合并二叉树
def mergeTrees(root1, root2):
    def dfs(n1, n2):
        if not (n1 and n2):  # 如果n1或n2有不存在的
            return n1 if n1 else n2
        n1.val += n2.val
        n1.left = dfs(n1.left, n2.left)
        n1.right = dfs(n1.right, n2.right)
        return n1
    return dfs(root1, root2)


if __name__ == "__main__":
    # 定义二叉树
    root = TreeNode(0)  # 根节点

    l = TreeNode(1)
    ll = TreeNode(2)
    lr = TreeNode(3)

    r = TreeNode(1)
    rl = TreeNode(3)
    rr = TreeNode(2)

    root.left = l
    root.right = r
    l.left = ll
    l.right = lr
    r.left = rl
    r.right = rr

    # Q94
    # a = inorderTraversal(root)
    # print(a)

    # Q101
    # a = isSymmetric(root)
    # print(a)

    # Q104
    # a = maxDepth(root)
    # print(a)

    # Q543
    a = diameterOfBinaryTree(root)
    print(a)
