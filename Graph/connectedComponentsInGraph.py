class Solution:
    # Function to return connected components of the graph
    def getComponents(self, V, edges):
        vis = [0]*V
        adjList = [[] for _ in range(V)]
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        def dfs(node: int,compoList: list):
            vis[node] = 1
            compoList.append(node)
            for adjNode in adjList[node]:
                if vis[adjNode] ==0 :
                    dfs(adjNode,compoList)
        ans = []  
        for node in range(V):
            if vis[node] == 0:
                compoList = []
                dfs(node,compoList)
                ans.append(compoList)

            