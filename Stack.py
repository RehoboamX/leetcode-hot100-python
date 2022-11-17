# Q20: 有效的括号
def isValid(string):
    stack = []  # 定义一个栈
    for c in string:
        if c == '(' or c == '[' or c == '{':
            stack.append(c)  # 如果遍历到左括号则压栈
        else:
            if len(stack) == 0:
                return False
            else:
                temp = stack.pop()  # 弹出栈的顶层元素
                if temp == '(' and c != ')':
                    return False
                if temp == '[' and c != ']':
                    return False
                if temp == '{' and c != '}':
                    return False
    if len(stack) != 0:
        return False
    return True


# Q234: 回文链表(在LinkedList里面出现过)
class LinkedList:  # 定义链表的数据结构
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head):  # 使用栈
    stack = []
    temp = head
    while temp is not None:
        stack.append(temp.val)
        temp = temp.next
    while head is not None:
        if head.val != stack.pop():
            return False
        head = head.next
    return True


# Q94: 二叉树的中序遍历(在Tree里面出现过)
class TreeNode:  # 定义二叉树的数据结构
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root):
    stack = []  # 定义一个栈
    result = []
    while root is not None:
        if root.left:  # 如果左子树存在
            stack.append(root)
            root = root.left
        else:
            if stack and not root.right:  # 如果不存在右节点
                result.append(root.val)
                root = stack.pop()  # 从栈中弹出原节点
            result.append(root.val)
            root = root.right
    return result


if __name__ == "__main__":
    # Q20
    # a = isValid('[]()')
    # print(a)

    # Q234
    # e1 = LinkedList(1)
    # e2 = LinkedList(3)
    # e3 = LinkedList(2)
    #
    # e1.next = e2
    # e2.next = e3
    #
    # print(isPalindrome(e1))

    # Q94
    root = TreeNode(0)  # 根节点

    l = TreeNode(1)
    ll = TreeNode(2)
    lr = TreeNode(3)

    r = TreeNode(4)
    rl = TreeNode(5)
    rr = TreeNode(6)

    root.left = l
    root.right = r
    l.left = ll
    l.right = lr
    r.left = rl
    r.right = rr

    a = inorderTraversal(root)
    print(a)

