from collections import deque
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        segments = deque()
        start = i =0
        n = len(nums)
        while i < n:
            if nums[i] ==  0:
                segments.append([start,i-1])
                start =i+1
            i += 1
        if start != n:
            segments.append([start,n-1])

        ans = 0
        while segments:
            size = len(segments)
            for _ in range(size):
                [l,r] = segments.popleft()
                if l > r :
                    continue
                mn = min(nums[l:r+1])
                for idx in range(l,r+1):
                    if nums[idx] == mn:
                        nums[idx] = 0
                        if l <= idx-1 :
                            segments.append([l,idx-1])
                        l = idx+1
                if l != r+1:
                    segments.append([l,r])
                ans += 1
        return ans
obj = Solution()
print(obj.minOperations([2, 1, 1, 2]))