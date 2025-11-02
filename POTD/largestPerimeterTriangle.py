class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort()
        i = len(nums)-1
        while i > 1:
            c = nums[i]
            j = i -1
            while j > 0:
                b = nums[j]
                k = j-1
                while k >=0 :
                    a = nums[k]
                    if c < a+b :
                        return a + b + c
                    elif c > a+b:
                        j = -1
                        k = -1
                    else :
                        k -= 1
                j -= 1
            i -= 1
        return 0

            