

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class MergeTwoSortedLists:
    def merge(self, l1, l2):
        if l1 is None and l2 is not None:
            return l2
        if l2 is None and l1 is not None:
            return l1
        if l1.value < l2.value:
            l1.next = self.merge(l1.next, l2)
            return l1
        else:
            l2.next = self.merge(l1, l2.next)
            return l2

if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(3)
    l1.next.next = ListNode(5)

    l2 = ListNode(2)
    l2.next = ListNode(6)
    l2.next.next = ListNode(8)

    mts = MergeTwoSortedLists()
    mts.merge(l1, l2)

    print(l1)