class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda x: x[0])
        merge = []
        for interval in intervals:
            if not len(merge) or interval[0] > merge[-1][1]:
                merge.append(interval)
            else:
                merge[-1][1] = max(interval[1], merge[-1][1])
            
        return merge
                
