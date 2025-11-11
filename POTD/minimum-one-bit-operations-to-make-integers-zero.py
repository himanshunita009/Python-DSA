class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        arr = []
        while n > 0:
            arr.append(n%2)
            n //= 2
        n = len(arr)
        ans = 0 
        for idx in range(n):
            if arr[idx] == 1:
                arr[idx] = 0
                ans += (2**(idx+1)-1)
                if idx < n-1 and arr[idx+1] == 1:
                    ans += 1
                    arr[idx+1] = 0
        return ans

obj = Solution()
print(obj.minimumOneBitOperations(137))