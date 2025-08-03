class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        n = len(folder)
        folder.sort(key=lambda x : len(x))
        visited = [False for _ in range(n)]
        ans = []
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                ans.append(folder[i])
                for j in range(i+1,n):
                    if not visited[j] and len(folder[j]) > len(folder[i]):
                        if  folder[j].startswith(folder[i]) and folder[j][len(folder[i])] == '/':  
                            visited[j] = True
        return ans
            
obj = Solution()
print(obj.removeSubfolders(["/a/b/c","/a/b/ca","/a/b/d"]))