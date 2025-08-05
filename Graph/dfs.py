class Solution :
    def solve(self,node: int,adj: list[list[int]],visited: list[int],ans: list[int]):
        visited[node] =1
        ans.append(node)
        for adjNode in adj[node]:
            if visited[adjNode] == 0:
                self.solve(adjNode,adj,visited,ans)
    def dfs(self,edges: list[list[int]],n: int):
        adj = [[] for _ in range(n)] 
        for edge in edges:
            u = edge[0]
            v = edge[1]
            adj[u].append(v)
            adj[v].append(u)
        visited = [0]*n
        ans = []
        for i in range(n):
            if visited[i] == 0:
                self.solve(i,adj,visited,ans)
        return ans

