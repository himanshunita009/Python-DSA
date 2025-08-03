
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        m = len(nums2)
        nextGreater = dict()
        for i in range(m-2,-1,-1):
            for j in range(i+1,m):
                if nums2[j] > nums2[i]:
                    nextGreater[nums2[i]] = nums2[j]
                    break
        ans = [-1 for _ in range(n)]
        for i in range(n):
            if nums1[i] in nextGreater:
                ans[i] = nextGreater[nums1[i]]
        return ans

# Using Monotonic Stask
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        m = len(nums2)
        nextGreater = dict()
        stack = list()
        for i in range(m-1,-1,-1):
            if len(stack) == 0:
                nextGreater[nums2[i]] = -1
                stack.append(nums2[i])
                continue
            while len(stack) > 0 and stack[-1] <= nums2[i]:
                stack.pop()
            if len(stack) > 0:
                nextGreater[nums2[i]] = stack[-1]
            else:
                nextGreater[nums2[i]] = -1
                stack.append(nums2[i])
        ans = [-1 for _ in range(n)]
        for i in range(n):
            ans[i] = nextGreater[nums1[i]]
        return ans
        
            