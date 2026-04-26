def main():
    input()
    arr = list(map(int,input().split()))
    maxIdx = arr.index(max(arr))
    arr.reverse()
    minIdx = len(arr) - arr.index(min(arr))-1
    ans = maxIdx
    ans += (len(arr)-minIdx-1)
    ans = ans - (0 if minIdx > maxIdx else 1)
    print(ans)

main()