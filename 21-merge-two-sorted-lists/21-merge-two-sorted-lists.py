# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        Arr1 = []
        var = 0
        while list1 is not None:
            var = list1.val
            list1 = list1.next
            Arr1.append(var)
        Arr2 = []
        var = 0
        while list2 is not None:
            var = list2.val
            list2 = list2.next
            Arr2.append(var)
        Arr1.extend(Arr2)
        Arr1.sort()
        
        n = 0
        node = ListNode(0)
        temp = node
        while(n<len(Arr1)):
            node2 = ListNode(Arr1[n])
            temp.next = node2
            temp = temp.next
            n+=1
        return node.next
            