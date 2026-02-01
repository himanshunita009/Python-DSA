from collections import deque

MOD = 10**9 + 7

def countPartitions(nums, k):
    n = len(nums)
    maxQ, minQ = deque(), deque()
    dp = [0]*(n+1)
    pref = [0]*(n+1)
    
    dp[0] = 1
    pref[0] = 1
    
    left = 0
    
    for i in range(n):
        # maintain max queue
        while maxQ and nums[maxQ[-1]] < nums[i]:
            maxQ.pop()
        maxQ.append(i)

        # maintain min queue
        while minQ and nums[minQ[-1]] > nums[i]:
            minQ.pop()
        minQ.append(i)

        # shrink window
        while nums[maxQ[0]] - nums[minQ[0]] > k:
            left += 1
            if maxQ[0] < left:
                maxQ.popleft()
            if minQ[0] < left:
                minQ.popleft()

        # dp transition
        dp[i+1] = pref[i] - (pref[left-1] if left > 0 else 0)
        dp[i+1] %= MOD
        
        pref[i+1] = (pref[i] + dp[i+1]) % MOD

    return dp[n]
