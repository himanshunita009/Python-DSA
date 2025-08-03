class Solution:
    def maxTotalFruits(self, fruits: list[list[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        pos = [f[0] for f in fruits]
        amt = [f[1] for f in fruits]
        
        # Prefix sum of fruits
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + amt[i]
        
        ans = 0
        
        for i in range(n):
            # try to go left to i, then right
            left = i
            lo, hi = i, n-1
            while lo <= hi:
                mid = (lo + hi) // 2
                cost = (startPos - pos[i]) if startPos >= pos[i] else (pos[mid] - startPos)
                cost += (pos[mid] - pos[i])
                if cost <= k:
                    lo = mid + 1
                    ans = max(ans, prefix[mid+1] - prefix[i])
                else:
                    hi = mid - 1

            # try to go right to i, then left
            right = i
            lo, hi = 0, i
            while lo <= hi:
                mid = (lo + hi) // 2
                cost = (pos[i] - startPos) if startPos <= pos[i] else (startPos - pos[mid])
                cost += (pos[i] - pos[mid])
                if cost <= k:
                    hi = mid - 1
                    ans = max(ans, prefix[i+1] - prefix[mid])
                else:
                    lo = mid + 1

        return ans
