class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        wordList = text.split(' ')
        ans = 0
        for word in wordList:
            flag = True
            for ch in brokenLetters:
                if ch in word:
                    flag = False
                    break
            if flag:
                ans += 1
        return ans