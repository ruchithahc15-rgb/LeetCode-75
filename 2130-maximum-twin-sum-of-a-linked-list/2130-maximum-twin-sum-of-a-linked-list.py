# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Step 1: Find the middle of the linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 'slow' is now at the beginning of the second half
        
        # Step 2: Reverse the second half of the list
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        # 'prev' is now the head of the reversed second half
        
        # Step 3: Find the maximum twin sum
        max_sum = 0
        first_half = head
        second_half = prev
        
        while second_half: # Only need to loop through half the list
            current_twin_sum = first_half.val + second_half.val
            max_sum = max(max_sum, current_twin_sum)
            
            # Move both pointers forward
            first_half = first_half.next
            second_half = second_half.next
            
        return max_sum

        