MOD = int(1e9) + 7

def maxBowlingScore(arr):
    n = len(arr)
    # Pad the array with 1 on both sides to handle boundaries
    nums = [1] + arr + [1]
    
    # Create a 2D DP array initialized with -1
    dp = [[-1 for _ in range(n + 2)] for _ in range(n + 2)]

    def solve(l, r):
        if r - l + 1 < 2:
            return 0
        if dp[l][r] != -1:
            return dp[l][r]
        
        max_score = 0
        for i in range(l, r):
            # Try removing nums[i] and nums[i+1]
            left = nums[l - 1] if l - 1 >= 0 else 1
            right = nums[r + 1] if r + 1 < len(nums) else 1
            score = left * nums[i] * nums[i + 1] * right
            score += solve(l, i - 1) + solve(i + 2, r)
            max_score = max(max_score, score)
        
        dp[l][r] = max_score % MOD
        return dp[l][r]

    return solve(1, n)
