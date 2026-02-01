class Solution:
    def maxRunTime(self, n: int, batteries: list[int]) -> int:
        if n > len(batteries):
            return 0
        if n == len(batteries):
            return min(batteries)
        hi = sum(batteries)//n
        lo = min(batteries)
        ans = 0
        def possible(t: int):
            usable = 0
            for b in batteries:
                if b >= t:
                    usable += t
                else:
                    usable += b
                if usable - n*t >= 0:
                    return True
            return usable - n*t >= 0
        while lo <= hi:
            mid = (lo+hi)//2
            if possible(mid):
                ans = mid
                lo = mid+1
            else:
                hi = mid-1
        return ans