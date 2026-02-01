class Solution:
    def countEffectiveSubsequences(self, nums):
        mod = 10**9 + 7
        n = len(nums)

        # 1. Find global OR → find relevant bits
        global_or = 0
        for x in nums:
            global_or |= x

        bits = []
        for b in range(32):
            if (global_or >> b) & 1:
                bits.append(b)

        B = len(bits)  # number of relevant bits

        # 2. For each bit, collect contributor indices
        bit_sets = []
        for b in bits:
            S = []
            for i in range(n):
                if nums[i] >> b & 1:
                    S.append(i)
            bit_sets.append(set(S))

        # Precompute powers of 2
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i - 1] * 2) % mod

        # 3. Inclusion–Exclusion over all non-empty subsets of bits
        answer = 0

        # there are at most 2^B subsets, usually B <= 10-15 for real constraints
        for mask in range(1, 1 << B):
            # intersection of S_b for all bits in this mask
            inter = None

            # count bits in this subset
            bits_count = 0
            for j in range(B):
                if (mask >> j) & 1:
                    bits_count += 1
                    if inter is None:
                        inter = bit_sets[j].copy()
                    else:
                        inter &= bit_sets[j]

            # size of the intersection
            k = len(inter)

            if k == 0:
                continue  # no way to kill all these bits

            ways = pow2[n - k]

            if bits_count % 2 == 1:
                answer = (answer + ways) % mod
            else:
                answer = (answer - ways) % mod

        return answer % mod

        
        
obj = Solution()
print(obj.countEffective([1,2,3]))