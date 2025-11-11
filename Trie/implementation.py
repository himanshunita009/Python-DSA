class Trie:
    def __init__(self):
        self.nodeList= [None]*26
        self.flag=False 
        self.cp  = 0
        self.ce  = 0
    def getIdx(self,ch):
        return ord(ch)-ord('a')
    def isExists(self,root,ch):
        idx = self.getIdx(ch)
        return root.nodeList[idx]
    def insert(self, word: str) -> None:
        root = self
        for ch in word:
            idx = self.getIdx(ch)
            if not self.isExists(root,ch):
                node = Trie()
                root.nodeList[idx] = node
            root = root.nodeList[idx]
            root.cp  += 1
        root.flag = True
        root.ce  += 1

    def search(self, word: str) -> bool:
        root = self
        for ch in word:
            idx = self.getIdx(ch)
            if not self.isExists(root,ch):
                return False
            root = root.nodeList[idx]
        return root.flag

    def startsWith(self, prefix: str) -> bool:
        root = self
        for ch in prefix:
            idx = self.getIdx(ch)
            if not self.isExists(root,ch):
                return False
            root = root.nodeList[idx]
        return True
    def countWord(self,word: str):
        root = self
        for ch in word:
            idx = self.getIdx(ch)
            if not self.isExists(root,ch):
                return False
            root = root.nodeList[idx]
        return root.ce
    def countStartWith(self, prefix: str) -> bool:
            root = self
            for ch in prefix:
                idx = self.getIdx(ch)
                if not self.isExists(root,ch):
                    return False
                root = root.nodeList[idx]
            return root.cp

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)