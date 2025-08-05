class Solution:
    def bfs(self,edges: list[list[int]],n: int):
        adj = [[] for _ in range(n)]
        for edge in edges:
            u = edge[0]
            v = edge[1]
            adj[u].append(v)
            adj[v].append(u)
        visited = [0]*n
        ans = []
        queue = []
        queue.append(0)
        while len(queue) > 0:
            size = len(queue)
            for _ in range(size):
                node = queue[0]
                queue = queue[1:]
                visited[node] =1 
                ans.append(node)
                for adjNode in adj[node]:
                    if visited[adjNode] == 0:
                        queue.append(adjNode)
        return ans