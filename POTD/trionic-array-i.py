class Solution:
    def isTrionic(self, nums: list[int]) -> bool:
        if nums[0] > nums[1]:
            return False
        cnt = 1 
        idx = 2
        isIncreasing = True
        while idx < len(nums) and cnt < 4:
            if isIncreasing and nums[idx-1] > nums[idx]:
                isIncreasing = False
                cnt += 1
            elif not isIncreasing and nums[idx-1] < nums[idx] :
                isIncreasing = True
                cnt += 1
            elif nums[idx-1] == nums[idx]:
                return False
            idx += 1
        return idx == len(nums) and cnt == 3
    
obj = Solution()
print(obj.isTrionic([1,3,5,4,2,6]))
