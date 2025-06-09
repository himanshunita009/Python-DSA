# Good suffix 
def is_prefix(pattern,suffix,mistatched):
    m = len(suffix)
    for startIndex in range(mistatched+1-m,-1,-1):
        prefix = pattern[startIndex:startIndex+m]
        if prefix == suffix :
            return startIndex
    return len(pattern)

def calculate_suffix(pattern):
    good_suffix = [0]*len(pattern)
    good_suffix[len(pattern)-1] = len(pattern)
    for i in range(len(pattern)-2,-1,-1):
        suffix = pattern[i+1:]
        good_suffix[i] = min(good_suffix[i+1],is_prefix(pattern,suffix,i))
    return good_suffix
print(calculate_suffix("ababcdab"))


# Bad Character Rule 
def solve(text,pattern):
    lastOccurenceOf = dict()
    for i in range(len(pattern)):
        lastOccurenceOf[pattern[i]] = i
    i=0
    while(len(text)-i >= len(pattern)):
        misMatchedIndex = -1
        for j in range(i+len(pattern)-1,i-1,-1):
            if text[j] != pattern[j-i]:
                misMatchedIndex = j
                break
        if misMatchedIndex == -1:
            return i
        lastOcc = lastOccurenceOf.get(text[misMatchedIndex],-1)
        i += misMatchedIndex - (i+lastOcc)
    return -1


# ans = solve("abaaabcd","abc")
# if ans == -1:
#     print("Pattern is not found in text")
# else:
#     print(f"pattern is found at index {ans}")

