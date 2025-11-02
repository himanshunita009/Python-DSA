from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        wordSet = set(wordList)
        que = deque()
        que.append(beginWord)
        cnt = 0
        vis = set()
        vis.add(beginWord)
        while que:
            size = len(que)
            cnt += 1
            for _ in range(size):
                currWord = que.popleft()
                if currWord == endWord:
                    return cnt + 1
                for chi in range(26):
                    ch = chr(chi + ord("a"))
                    for i in range(len(currWord)):
                        if currWord[i] == ch :
                            continue
                        newWord = currWord[:i]+ch+currWord[i+1:]
                        if newWord in wordSet and newWord not in vis:
                            que.append(newWord)
                            vis.add(newWord)

        return 0