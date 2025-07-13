# Python code for the above approach

# Program to convert the base of
# given binary number to base 6


def convertBase(N):

    # 128 bit integer to store
    # the decimal conversion
    decimal = 0

    # Loop to iterate N
    for i in range(len(N)):

        # Binary to decimal
        decimal = decimal * 2 + (ord(N[i]) - ord('0'))

    # Stores the base 6 int
    ans = []

    # Decimal to base 6
    while (decimal > 0):
        ans.append(decimal % 6)
        decimal = decimal // 6

    # Print Answer
    for i in range(len(ans) - 1, -1, -1):
        print(ans[i], end="")


# Driver Code
N = "100111"
convertBase(N)

# This code is contributed by gfgking