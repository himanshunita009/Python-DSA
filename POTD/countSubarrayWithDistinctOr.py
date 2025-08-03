class Solution:
    def subarrayBitwiseORs(self, arr: list[int]) -> int:
        n = len(arr)
        ans = set()
        i = 0
        for i in range(n):
            if arr[i] not in ans:
                ans.add(arr[i])
            temp = arr[i]
            j = i+1
            while j < n and (arr[j] | temp) != temp:
                temp |= arr[j]
                ans.add(arr[j])
                j += 1  
        return len(ans)

obj = Solution()
print(obj.subarrayBitwiseORs([1,2,4]))