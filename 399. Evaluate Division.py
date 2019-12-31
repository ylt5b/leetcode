class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # 1. dfs
        graph = collections.defaultdict(list)
        for equation, value in zip(equations, values):
            x, y = equation
            if x not in graph:
                graph[x] = [(y, value)]
            else:
                graph[x].append((y, value))
            if y not in graph:
                graph[y] = [(x, 1.0 / value)]
            else:
                 graph[y].append((x, 1.0 / value))
        def dfs(start, end, value, res):
            if start == end and start in graph: 
                res[0] = value
                return
            if start in visited:
                return
            visited.add(start)
            for node in graph[start]:
                dfs(node[0], end, value * node[1], res)
                
        ans = []      
        for query in queries:
            if query[0] not in graph or query[1] not in graph: 
                ans.append(-1.0)
                continue
            visited = set()
            res = [-1.0] 
            dfs(query[0], query[1], 1.0, res)
            ans.append(res[0])
        return ans
    
    
   # bfs
        graph = collections.defaultdict(list)
        for equation, value in zip(equations, values):
            x, y = equation       
            graph[x].append((y, value))     
            graph[y].append((x, 1.0 / value))
            
        def  bfs(src, dst):
            if src not in graph or dst not in graph:
                return -1.0
            seen = set()
            queue = collections.deque([(src, 1.0)])
            while queue:
                x, value = queue.popleft()
                if x == dst:
                    return value
                seen.add(x)
                for node, val in graph[x]:
                    if node not in seen:
                        seen.add(node)
                        queue.append((node, value * val))
            return -1.0
        return [bfs(s, d) for s, d in queries]

    
    
       # bfs
        graph = collections.defaultdict(list)
        for equation, value in zip(equations, values):
            x, y = equation       
            graph[x].append((y, value))     
            graph[y].append((x, 1.0 / value))
            
        def  bfs(src, dst):
            if src not in graph or dst not in graph:
                return -1.0
            seen = set()
            queue = collections.deque([(src, 1.0)])
            while queue:
                x, value = queue.popleft()
                if x == dst:
                    return value
                seen.add(x)
                for node, val in graph[x]:
                    if node not in seen:
                        seen.add(node)
                        queue.append((node, value * val))
            return -1.0
        return [bfs(s, d) for s, d in queries]
