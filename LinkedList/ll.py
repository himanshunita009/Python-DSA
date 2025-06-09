# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: ListNode) -> ListNode:
        tCount = 1
        count = 1
        headCopy = head
        prev = None
        while head:

            if tCount%2 != 0:
                prev = head
                if count > 0:
                    count -= 1
                    head = head.next
                if count == 0:
                    tCount += 1
                    count = tCount
            else:
                start = end = head
                head = head.next
                count -= 1
                while head and count > 0:
                    temp = head.next
                    head.next = start
                    start = head
                    head = temp
                    count -= 1
                prev.next = start 
                end.next = head
                tCount += 1
                count = tCount
        return headCopy
        
obj = Solution()
head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6,ListNode(7,ListNode(8,ListNode(9,ListNode(10,None))))))))))
obj.reverseEvenLengthGroups(head)