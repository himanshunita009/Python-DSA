# def solve():
#     pass
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        i = 0
        j = 0
        brr =  list()
        while j < len(arr)-1:
            if arr[j] > arr[j+1]:
                brr.append((arr[i],arr[j]))
                i = j+1
            j = j+1
        brr.append((arr[i],arr[j]))
        arr = brr
        brr= []
        while len(arr) > 1:
            j = 1
            prev = arr[0]
            while j < len(arr):
                if prev[0] < arr[j][1]:
                    prev = [min(prev[0],arr[j][0]),max(prev[1],arr[j][1])]
                else:
                    brr.append(prev)
                    prev = arr[j]
                j += 1
            brr.append(prev)
            if len(arr) == len(brr):
                print("No")
                break
            arr = brr
            brr = []
        if len(arr) == 1:
            print("Yes")
        



main()
