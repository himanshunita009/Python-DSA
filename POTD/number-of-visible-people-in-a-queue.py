class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        n = len(heights)
        ans = [0]*n
        stack = [0]
        for idx in range(1,n):
            while stack and heights[stack[-1]] < heights[idx]:
                ans[stack[-1]] += 1
                stack.pop()
            if heights[stack[-1]] > heights[idx]:
                ans[stack[-1]] += 1
                stack.append(idx)
            if not stack:
                stack.append(idx)
        return ans
                
                

