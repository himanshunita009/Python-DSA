# cook your dish here
def findGcd(a,b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a >  b:
        return findGcd(a-b,b)
    return findGcd(a,b-a)


def main():
    t = int(input())
    while(t > 0):
        a,b = map(int,list(input().split(' ')))
        gcd = findGcd(a,b)
        if gcd > 1:
            print(0)
        if b%2 != 0 and a%2 != 0:
            print(2)
        else :
            print(1)
        t -= 1
if __name__ == '__main__':
    main()