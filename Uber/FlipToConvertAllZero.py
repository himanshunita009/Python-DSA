# Python 3 program for the above approach

# Function to find the maximum value of K
# such that flipping substrings of size
# at least K make all characters 0s
def maximumK(S):
    N = len(S)

    # Stores the maximum value of K
    ans = N

    flag = 0

    # Traverse the given string S
    for i in range(N - 1):
      
        # Store the minimum of the
        # maximum of LHS and RHS length
        if (S[i] != S[i + 1]):

            # Flip performed
            flag = 1
            ans = min(ans, max(i + 1,N - i - 1))

    # If no flips performed
    if (flag == 0):
        return 0

    # Return the possible value of K
    return ans

# Driver Code
if __name__ == '__main__':
    S = "010"
    print(maximumK(S))
    
    # This code is contributed by SURENDRA_GANGWAR.