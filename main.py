import math
def gcd(a: int,b: int):
    if a < b:
        return gcd(b,a)
    while b != 0:
        a,b = b,a%b
    return a
def main():
    t = int(input())
    while t > 0:
        n = int(input())
        arr = list(map(int,input().split()))
        g = arr[0]
        for num in arr[1:]:
            g = gcd(g,num)
        x = 2
        while True:
            if math.gcd(g,x) == 1:
                print(x)
                break
            x += 1
        t -= 1


main()