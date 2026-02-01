def main():
    t = int(input())
    for idx in range(t):
        num = int(input())
        temp = 1
        ans = []
        while num > 0:
            if num%10 != 0:
                ans.append((num%10)*temp)
            temp *= 10
            num //= 10
        print(len(ans))
        for ch in ans:
            print(ch,end=" ")
        if idx < t:
            print()
main()

             
