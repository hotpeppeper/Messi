
'''
给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class AddNumber:
    def add_number(self, n1, n2):
        if not n1:
            return n2
        if not n2:
            return n1

        if n1.value + n2.value < 10:
            n3 = Node(n1.value + n2.value)
            n3.next = self.add_number(n1.next, n2.next)
        else:
            n3 = Node(n1.value + n2.value - 10)
            tmp = Node(1)
            n3.next = self.add_number(n1.next, self.add_number(n2.next, tmp))
        return n3


if __name__ == "__main__":
    la = Node(2)
    la.next = Node(4)
    la.next.next = Node(3)

    lb = Node(5)
    lb.next = Node(6)
    lb.next.next = Node(7)

    aa = AddNumber()
    lc = aa.add_number(la, lb)