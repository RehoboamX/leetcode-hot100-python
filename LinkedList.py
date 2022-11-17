# 定义链表的数据结构
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Q206: 反转链表
def reverseList(head):
    pre = None
    cur = head
    while cur is not None:
        temp = cur.next  # 先把原来cur.next位置存起来
        cur.next = pre
        pre = cur
        cur = temp
    return pre


# Q234: 回文链表
def isPalindrome1(head):  # 反转链表法
    fast = slow = head
    while fast.next and fast.next.next:  # 快慢指针找到链表中点
        slow = slow.next
        fast = fast.next.next
    pre = None
    cur = slow.next
    slow.next = None
    while cur is not None:  # 反转后半部分的链表
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
    while pre is not None:  # 比较前半链表和反转的后半链表
        if pre.val != head.val:
            return False
        pre = pre.next
        head = head.next
    return True


def isPalindrome2(head):  # 使用栈
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


# Q141 环形链表
def hasCycle1(head):
    fast, slow = head, head  # 快慢指针
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False


def hasCycle2(head):
    hashmap = {}  # 哈希表记录链表节点
    while head is not None:
        hashmap[head] = 1
        head = head.next
        if head in hashmap:
            return True
    return False


# Q160: 相交链表
def getIntersectionNode(headA, headB):
    counter = set()
    while headA is not None:
        counter.add(headA)
        headA = headA.next
    while headB is not None:
        if headB in counter:
            return headB
        headB = headB.next
    return None


# Q21: 合并两个有序链表
def mergeTwoLists(head1, head2):
    dummy = ListNode(0)  # 虚拟头节点
    temp = dummy
    while head1 is not None and head2 is not None:
        if head1.val > head2.val:
            temp.next = head2
            head2 = head2.next
        else:
            temp.next = head1
            head1 = head1.next
        temp = temp.next
    if head1 is not None:
        temp.next = head1
    if head2 is not None:
        temp.next = head2
    return dummy.next


# Q2: 两数相加
def addTwoNums(headA, headB):
    dummy = ListNode(0)
    temp = dummy
    carry = 0  # 进位
    while headA and headB:  # 两个链表节点均不为None
        temp.next = ListNode((headA.val + headB.val + carry) % 10)
        carry = (headA.val + headB.val + carry) // 10
        headA = headA.next
        headB = headB.next
        temp = temp.next
    if headA is not None:
        while headA:
            temp.next = ListNode((headA.val + carry) % 10)
            carry = (headA.val + carry) // 10
            headA = headA.next
            temp = temp.next
        while headB:
            temp.next = ListNode((headB.val + carry) % 10)
            carry = (headA.val + carry) // 10
            headB = headB.next
            temp = temp.next
    if carry == 1:
        temp.next = ListNode(1)
    return dummy.next


# Q19: 删除链表的倒数第N个节点
def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    fast, slow = head, head  # 双指针
    while n != 0:
        fast = fast.next
        n -= 1
    while fast.next is not None:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next


if __name__ == "__main__":
    # 定义链表
    e1 = ListNode(2)
    e2 = ListNode(4)
    e3 = ListNode(3)
    e4 = ListNode(6)
    e5 = ListNode(7)

    e1.next = e2
    e2.next = e3
    e3.next = e4
    e4.next = e5
    # e5.next = e3

    # c1 = ListNode(5)
    # c2 = ListNode(6)
    # c3 = ListNode(4)
    #
    # c1.next = c2
    # c2.next = c3

    # Q206
    # a = reverseList(e1)
    # while a is not None:
    #     print(a.val)
    #     a = a.next

    # Q234
    # a = isPalindrome2(e1)
    # print(a)

    # Q141
    # a = hasCycle2(e1)
    # print(a)

    # Q160
    # a = getIntersectionNode(e1, c1)
    # print(a.val)

    # Q21
    # a = mergeTwoLists(e1, c1)
    # while a:
    #     print(a.val)
    #     a = a.

    # Q2
    # a = addTwoNums(c1, e1)
    # while a:
    #     print(a.val)
    #     a = a.next

    # Q19
    a = removeNthFromEnd(e1, 3)
    while a:
        print(a.val)
        a = a.next
