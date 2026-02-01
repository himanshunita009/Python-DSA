def main():
    n,m = list(map(int,input().split()))
    toggle = True
    for row in range(n):
        if row%2 == 0:
            print(("#"*m))
        elif toggle :
            print(("."*(m-1)+"#"))
            toggle = not toggle
        else:
            print("#"+("."*(m-1)))
            toggle = not toggle
if __name__ == "__main__":
    main()

             
