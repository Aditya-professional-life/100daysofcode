class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev = dummy
        curr = head

        while curr and curr.next:
            nxtPair = curr.next.next
            secondNode = curr.next

            secondNode.next = curr
            curr.next = nxtPair
            prev.next = secondNode

            prev = curr
            curr = nxtPair

        return dummy.next
        