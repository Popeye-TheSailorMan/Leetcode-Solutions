# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        Arr1 = []
        var = 0
        while l1 is not None:
            var = l1.val
            l1 = l1.next
            Arr1.append(var)
        Arr2 = []
        var = 0
        while l2 is not None:
            var = l2.val
            l2 = l2.next
            Arr2.append(var)
        
        num1 = 0
        for i in reversed(range(len(Arr1))):
            var = Arr1[i]*(10**(i))
            num1 += var
        num2 = 0
        for i in reversed(range(len(Arr2))):
            var = Arr2[i]*(10**(i))
            num2 += var
        
        num3  = num1+ num2
        res = [int(x) for x in str(num3)]
        res.reverse()
        
        n = 0
        node = ListNode(0)
        temp = node
        while(n<len(res)):
            node2 = ListNode(res[n])
            temp.next = node2
            temp = temp.next
            n += 1
        return node.next