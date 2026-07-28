# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # 2 pointers, one for each list
        # compare list1.val to list 2.val
        # pick the smallest and append to the list
        # advance the pointer until it reches end of list
        
        dummy = ListNode(0)
        tail = dummy
        
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next
        
        if list1 is not None:
            tail.next = list1
        else:
            tail.next = list2
        
        return dummy.next

    # space complexity: 
    # time complexity: O(n + m) n and m being length of the lists



    

            
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       










       
       
       
       
       
       

























       
        # # Edge cases:
        # # one list is empty, we return the other list



        # merged_list = ListNode() # dummy node
        # dummy = merged_list

        # while list1 and list2:
        #     if list1.val < list2.val:
        #         merged_list.next = list1
        #         list1 = list1.next
        #     else:
        #         merged_list.next = list2
        #         list2 =  list2.next
        #     merged_list = merged_list.next

        # merged_list.next = list1 or list2 

        # return dummy.next 
        