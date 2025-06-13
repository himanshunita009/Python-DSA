class Solution:
    def __init__(self):
        self.dp = dict()
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        if s == "":
            return True
        if s in self.dp:
            return self.dp[s]
        for word in wordDict:
            if s.startswith(word):
                temp = s[len(word):]
                if self.wordBreak(temp,wordDict):
                    return True
        self.dp[s] = False
        return False

obj = Solution()
print(obj.wordBreak("ccbb",["cb","bc"]))