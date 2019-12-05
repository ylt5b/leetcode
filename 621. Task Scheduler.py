class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 1. heap, O(nlogn)
        count = collections.Counter(tasks)
        heap = []
        n += 1
        for key in count.keys():
            heapq.heappush(heap, -count[key])
        ans = 0
        while heap:
            stack = []
            count = 0
            for _ in range(n):
                if heap:
                    c = heapq.heappop(heap)
                    count += 1
                    if c < -1:
                        stack.append(c+1)
            for i in stack:
                heapq.heappush(heap, i)
            if heap:
                ans += n
            else:
                ans += count
        return ans
