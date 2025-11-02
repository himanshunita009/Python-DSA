class Solution:
    def score(self, cards: list[str], x: str) -> int:
        firstPos = [0 for _ in range(26)]
        secondPos = [0 for _ in range(26)]
        both = 0
        for temp in cards:
            if temp[0] == x and temp[1] == x:
                both += 1
            elif temp[0] == x:
                firstPos[ord(temp[1])-ord('a')] += 1
            elif temp[1] == x:
                secondPos[ord(temp[0])-ord('a')] += 1
        ans = 0
        i = 0
        j = 25
        while i < j :
            if firstPos[i] == 0:
                i += 1
                continue
            if firstPos[j] == 0:
                j -= 1
                continue
            temp1 = min(firstPos[i],firstPos[j])
            firstPos[i] -= temp1
            firstPos[j] -= temp1
            ans += temp1
        
        i = 0
        j = 25
        while i < j :
            if secondPos[i] == 0:
                i += 1
                continue
            if secondPos[j] == 0:
                j -= 1
                continue
            temp1 = min(secondPos[i],secondPos[j])
            secondPos[i] -= temp1
            secondPos[j] -= temp1
            ans += temp1
        fr = sr = 0
    
        for i in  range(26):
            fr += firstPos[i]
            sr += secondPos[i]

        ans = ans  + min(sr+fr,both)
        return ans
        

obj = Solution()
print(obj.score(["ab","aa","ab","bc","cc","bc","bb","ac","bc","bc","aa","aa","ba","bc","cb","ba","ac","bb","cb","ac","cb","cb","ba","bc","ca","ba","bb","cc","cc","ca","ab","bb","bc","ba","ac","bc","ac","ac","bc","bb","bc","ac","bc","aa","ba","cc","ac","bb","ba","bb"],"b"))