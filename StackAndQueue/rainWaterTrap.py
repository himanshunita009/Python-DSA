class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        nextGreatestElement= [-1] * n
        prevGreatestElement= [-1] * n
        
