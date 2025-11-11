class Trie :
    def __init__(self):
        self.nodeList = [None]*26
        self.listOfDistinctSubstring = []    
    def getIdx(self,ch: str):
        return ord(ch)-ord('a')
    def isExsists(self,ch: str):
        idx = self.getIdx(ch)
        return self.nodeList[idx] is not None
    
    def insert(self,word: str):
        root = self
        ans = ""
        for ch in word:
            ans += ch
            idx = self.getIdx(ch)
            if not root.isExsists(ch):
                root.nodeList[idx] = Trie()
                self.listOfDistinctSubstring.append(ans)
            root = root.nodeList[idx]

if __name__ == "__main__":
    word = "abc"
    ans  = 0
    obj = Trie()
    for i in range(len(word)):
        subWord = word[i:]
        obj.insert(subWord) 
    obj.listOfDistinctSubstring.append("")
    print(obj.listOfDistinctSubstring)