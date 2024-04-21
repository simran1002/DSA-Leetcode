class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        return self.dfs(graph, source, destination, visited)
    
    def dfs(self, graph, source, destination, visited):
        if source == destination:
            return True
        
        visited.add(source)
        for neighbor in graph[source]:
            if neighbor not in visited:
                if self.dfs(graph, neighbor, destination, visited):
                    return True
        
        return False