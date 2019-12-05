class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    
    # 1. heap
        if not lists: return None
        heap = []
        count = 0
        for i, item in enumerate(lists):
            if item: 
                count += 1
                heapq.heappush(heap, (item.val, count, item))
        head = head_temp = ListNode(0)
        while len(heap) > 0:
            value, _, node = heapq.heappop(heap)
            head_temp.next = node
            head_temp = head_temp.next
            node = node.next
            if node:
                count += 1
                heapq.heappush(heap, (node.val, count, node))
        return head.next
        
    # merge
    
        def merge_two(l1, l2):
            head = curr = ListNode(0)
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                    curr = curr.next
                else:
                    curr.next = l2
                    l2 = l2.next
                    curr = curr.next
            if not l1:
                curr.next = l2
            if not l2: 
                curr.next = l1
            return head.next
        n = len(lists)
        if n == 0: return None
        interval = 1
        while interval < n:
            for i in range(0, n - interval, interval * 2):
                lists[i] = merge_two(lists[i], lists[i+interval])
            interval *= 2
        return lists[0] 
