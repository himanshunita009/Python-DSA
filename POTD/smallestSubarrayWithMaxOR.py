class Solution:
    # def smallestSubarrays(self, nums: list[int]) -> list[int]:
    #     n = len(nums)
    #     bits = [-1] * 30
    #     ans = [1] * n
    #     for i in range(n-1,-1,-1):
    #         for bit in range(30):
    #             if nums[i] & (1 << bit):
    #                 bits[bit] = i

    #         for bit in range(30):
    #             if bits[bit] != -1:
    #                 ans[i] = max(ans[i],bits[bit]-i+1)
    #     return ans
    def smallestSubarrays(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [1] * n
        for i in range(n):
            x = nums[i]
            j = i-1
            while j >= 0 and nums[j] | x > nums[j]:
                nums[j] = nums[j] | x
                ans[i] = i-j+1
                j -= 1

        return ans


obj = Solution()
print(obj.smallestSubarrays([9,5,0,10,7,2,9,2,4]))
        