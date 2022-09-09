#Given the head of a singly linked list, reverse the list, and return the reversed list.
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n=head
        prev=None
        while n is not None:
            nxt=n.next
            n.next=prev
            prev=n
            n=nxt
        return prev
     