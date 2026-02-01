# def solve():
#     pass
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        if arr[-1] == -1 and arr[0] != -1:
            arr[-1] = arr[0]
        elif arr[-1] != -1 and arr[0] == -1:
            arr[0] = arr[-1]
        elif arr[-1] == -1 and arr[0] == -1:
            arr[-1] = arr[0] = 0
        print(abs(arr[-1]-arr[0]))
        for num in arr:
            if num == -1:
                print(0,end=" ")
            else:
                print(num,end=" ")
        print()


main()
