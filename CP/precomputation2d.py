def main():
    n,m = list(map(int,input().split()))
    arr = [[0]*m for _ in range(n)]
    for row in range(n):
        arr[row] = list(map(int,input().split()))
    pf = [[0]*(m+1) for _ in range(n+1)]
    for row in range(1,n+1):
        for col in range(1,m+1):
            pf[row][col] = arr[row-1][col-1] + pf[row][col-1]+pf[row-1][col] - pf[row-1][col-1]
    t = int(input())
    for _ in range(t):
        [a,b,c,d] = list(map(int,input().split()))
        ans = pf[c][d] - pf[a-1][d] - pf[c][b-1] + pf [a-1][b-1]
        print(ans)

