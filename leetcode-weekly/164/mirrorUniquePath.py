class Solution:
    def find(self,arr: list[int],key: int):
        lo = 0
        hi= len(arr)-1
        while lo <= hi:
            mid = (lo+hi)//2
            if arr[mid] > key:
                hi = mid-1
            elif arr[mid]< key :
                lo = mid+1
            else:
                return True
        return False
    def recoverOrder(self, order: list[int], friends: list[int]) -> list[int]:
        ans= list()
        for num in order:
            if self.find(friends,num):
                ans.append(num)
        return ans