class Solution:
    def __init__(self):
        self.vowels = set(['a','e','i','o','u','A','E','I','O','U'])
        self.dp = dict()
    def getWordMask(self,loWord: str):
        wordMask = ""
        for ch  in loWord:
            if ch in self.vowels:
                wordMask += '*'
            else :
                wordMask +=  ch
        return wordMask
    def spellchecker(self, wordlist: list[str], queries: list[str]) -> list[str]:
        exact = set(wordlist)
        maskWordsList = dict()
        loWordsList = dict()
        for (idx,word) in enumerate(wordlist):
            loWord = word.lower()
            if loWord not in loWordsList:
                loWordsList[loWord] = idx
            wordMask = self.getWordMask(loWord)
            if wordMask not in maskWordsList:
                maskWordsList[wordMask]  = idx 

        ans = []
        for query in queries:
            if query in exact:
                ans.append(query)
                continue
            loQuery = query.lower()
            if loQuery  in loWordsList:
                ans.append(wordlist[loWordsList[loQuery]])
                continue
            queryMask = self.getWordMask(loQuery)
            if queryMask in maskWordsList:
                ans.append(wordlist[maskWordsList[queryMask]])
            else:
                ans.append("")
        return ans

obj = Solution()
print(obj.spellchecker(["Yellow"],["yellow"]))