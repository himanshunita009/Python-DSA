class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        if bits[-1] != 0:
            return False
        idx = 0
        while idx < len(bits)-1:
            if bits[idx] == 1 and bits[idx+1] == 1 or bits[idx] == 1 and bits[idx+1] == 0:
                idx += 2
            else:
                idx += 1
        return idx == len(bits)-1


obj = Solution()
print(obj.isOneBitCharacter([0,1,0]))