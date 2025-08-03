def solve(nums: list[int]) :
    nums.sort()
    ans = 0
    for idx in range(len(nums)):
        if nums[idx] == 0:
            ans += 1
        else :
            ans += nums[idx]
    return ans


if __name__ == "__main__":
    t = int(input())
    while t> 0:
        n = int(input())
        arr = list(map(int,input().split()))
        print(solve(arr))
        t -= 1
    