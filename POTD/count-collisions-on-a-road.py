class Solution:
    def countCollisions(self, directions: str) -> int:
        cnt = 0
        curr = ''
        ans = 0
        for ch in directions:
            if ch == 'R':
                if curr == "" or curr == ch:
                    curr = ch
                    cnt += 1
                elif curr == "S":
                    curr = 'R'
                    cnt = 1
            elif ch == 'L':
                if curr == 'R':
                    ans += 2
                    ans += (cnt-1)
                    curr = 'S'
                    cnt = 1
                elif curr == "S":
                    ans += 1
            else:
                if curr == "R":
                    ans += cnt
                    curr = "S"
                    cnt = 1
        return ans