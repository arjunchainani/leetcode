# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # SOMETHING TO TRY LATER ON:
        # a more time-optimal solution is to add the digits as soon as you grab them from the array
        # means you can do the whole thing in one while loop

        i = 0
        num1 = 0
        num2 = 0
        while l1 is not None or l2 is not None:
            if l1 is not None:
                num1 += l1.val * (10**i)
                l1 = l1.next
            if l2 is not None:
                num2 += l2.val * (10**i)
                l2 = l2.next
        
            i += 1

        answer = num1 + num2

        init_node = None
        prev_node = None

        if answer == 0:
            init_node = ListNode(val=0, next=None)

        while answer > 0:
            curr_digit = answer % 10
            answer = answer // 10
            digit_node = ListNode(val=curr_digit, next=None)

            if prev_node is not None:
                prev_node.next = digit_node
            else:
                init_node = digit_node
            
            prev_node = digit_node
        
        return init_node