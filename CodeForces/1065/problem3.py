# def solve():
#     pass
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        brr = list(map(int,input().split()))
        aAns = 0
        bAns = 0
        for idx in range(n):
            aAns ^= arr[idx] 
            bAns ^= brr[idx]
        for idx in range(n):
            tempA = aAns^arr[idx]^brr[idx]
            tempB = bAns^arr[idx]^brr[idx]
            if idx&1 == 0 and tempA > tempB:
                arr[idx],brr[idx] = brr[idx],arr[idx]
                aAns = tempA
                bAns = tempB
            elif idx&1 == 1 and tempB > tempA:
                arr[idx],brr[idx] = brr[idx],arr[idx]
                aAns = tempA
                bAns = tempB
        if aAns > bAns:
            print("Ajisai")
        elif bAns > aAns:
            print("Mai")
        else:
            print("Tie")        


main()
