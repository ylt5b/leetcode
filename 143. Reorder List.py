class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        def _split(head):
            
            slow = fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            head1 = slow.next
            slow.next = None
            return head, head1
        
        def _reverse(head):
        
            last = None
            curr = head
            while curr:
                temp = curr.next
                curr.next = last
                last = curr
                curr = temp
            return last
        
        def _merge(a, b):
           
            while b:
                next1, next2 = a.next, b.next
                a.next = b
                b.next = next1
                a, b = next1, next2
                
        if not head or not head.next:
            return
        a, b = _split(head)
        b = _reverse(b)
        _merge(a, b)
