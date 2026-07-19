# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # # using arry
        # arr = []
        # curr = head

        # while curr:
        #     arr.append(curr.val)
        #     curr = curr.next

        # left = 0
        # right = len(arr) -1

        # while left < right:
        #     if arr[left] != arr[right]:
        #         return False
        #     left +=1
        #     right -=1

        # return True 
        

        # Input: head = [1,2,3,2,1]
        # A linked list only lets you walk forward. 
        # That's the core obstacle: to check a palindrome you naturally want to compare node 1 with node n, node 2 with node n-1

        # if we find the mid point, 
         # [1, 2, 3, 2, 1]
         # mid point = 3
         # [2, 2, 2, 2]
         # mid point = 2

        fast = head
        slow = head

        # find middle (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        #  # [1, 2, 3, 2, 1]

        # slow/mid: 3
        # second half: 2->1 -> None
        # reverse 1->2->None
        # reverse second hal

        prev = None
        curr = slow
        while curr:
            nxt = curr.next  # 1. save next
            curr.next = prev  # 2. flip pointer
            prev = curr  # 3. move prev
            curr = nxt # 4. move curr


        # compare first half with reversed second half
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True



        

