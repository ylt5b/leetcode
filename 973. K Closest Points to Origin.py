import heapq
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        
        # 2. min heap O(nlog(k))
        heap = []
        
        for (x, y) in points:
            dist = -(x **2 + y **2)
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        return [(x, y) for (dist, x, y) in heap]

        # 3. quick select O(n)
         def dist(p):
            return p[0]**2 + p[1]**2
        def quickSelect(lo, hi, K):
            # while lo < hi:
            pivot = dist(points[lo])
            i, j = lo+1, hi

            while i <= j:
                while i <= hi and dist(points[i]) <= pivot:
                    i += 1
                while j > lo and dist(points[j]) >= pivot:
                    j -= 1
                if i < j:
                    points[i], points[j] = points[j], points[i]
            points[lo], points[j] = points[j], points[lo]

            if K-1 == j:
                return
            elif j > K-1:
                quickSelect(lo, j - 1, K)
            else:
                quickSelect(j+1, hi, K)
            
        quickSelect(0, len(points)-1, K)
        return points[:K]
