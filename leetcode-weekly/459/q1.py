class Solution:
    def __init__(self):
        self.dp = dict()
        self.dp[2] = 1
        self.dp[1] = 0
    def popcount(x):
        count = 0
        

    def popcount(self,n):
        if n in self.dp:
            return self.dp.get(n)
        cnt = 0
        temp = n
        while n:
            n &= n - 1
            cnt += 1

        self.dp[temp] = self.popcount(cnt) + 1
        return self.dp[temp]
    def popcountDepth(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        ans = []
        popcountD = []
        for i in range(len(nums)):
            popcountD.append(self.popcount(nums[i]))
        for q in queries:
            if q[0] == 1:
                [op,l,r,k] = q
                ans.append(popcountD[l:r+1].count(k))
            else :
                [op,idx,val] = q
                popcountD[idx] = self.popcount(val)
        return ans



obj = Solution()

print(obj.popcountDepth([1,2],[[1,0,1,1],[2,0,3],[1,0,0,1],[1,0,0,2]]))


class BIT:
    def __init__(self, n):
        self.n = n + 2
        self.tree = [0] * self.n

    def update(self, i, delta):
        i += 1  # 1-indexed
        while i < self.n:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

    def range_sum(self, l, r):
        return self.query(r) - self.query(l - 1)


class Solution:
    def __init__(self):
        self.dp = {1: 0, 2: 1}

    def popcount(self, n):
        if n in self.dp:
            return self.dp[n]
        cnt = 0
        temp = n
        while n:
            n &= n - 1
            cnt += 1
        self.dp[temp] = self.popcount(cnt) + 1
        return self.dp[temp]

    def popcountDepth(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        depths = []
        bits = [BIT(n) for _ in range(6)]  # as k <= 5

        # Initial population
        for i, num in enumerate(nums):
            d = self.popcount(num)
            depths.append(d)
            bits[d].update(i, 1)

        ans = []
        for q in queries:
            if q[0] == 1:
                _, l, r, k = q
                ans.append(bits[k].range_sum(l, r))
            else:
                _, idx, val = q
                old_depth = depths[idx]
                new_depth = self.popcount(val)
                if old_depth != new_depth:
                    bits[old_depth].update(idx, -1)
                    bits[new_depth].update(idx, 1)
                    depths[idx] = new_depth
        return ans
