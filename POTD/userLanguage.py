class Solution:
    def minimumTeachings(self, n: int, languages: list[list[int]], friendships: list[list[int]]) -> int:
        mp = dict()
        for (user,languageSet) in enumerate(languages):
            languageBitMask = 0
            for language in languageSet:
                languageBitMask |= (1<<(language-1))
            mp[user+1] = languageBitMask

        ans = float('inf')
        for language in range(1,n+1):
            uniqueUser = set()
            for [a,b] in friendships:
                aMask = mp.get(a)
                bMask = mp.get(b)
                lMask = 1<<(language-1)
                if not aMask & bMask:
                    if not lMask & aMask:
                        uniqueUser.add(a)
                    if not lMask & bMask:
                        uniqueUser.add(b)
                
            ans = min(ans,len(uniqueUser))
        return ans
    
n = 3
languages = [[2],[1,3],[1,2],[3]]
frnd = [[1,4],[1,2],[3,4],[2,3]]
obj = Solution()
print(obj.minimumTeachings(n,languages,frnd))