import re
class Solution:
    def validateCoupons(self, codes: list[str], businessLine: list[str], isActive: list[bool]) -> list[str]:
        validCategories = set(["electronics", "grocery", "pharmacy", "restaurant"])
        n = len(codes)
        pattern = r"^[a-zA-Z0-9_]+$"
        temp = []
        for idx in range(n):
            if businessLine[idx] in validCategories and isActive[idx] and re.match(pattern,codes[idx]):
                temp.append((businessLine[idx],codes[idx]))
        temp.sort()
        ans = []
        for _,code in temp:
            ans.append(code)
        return ans