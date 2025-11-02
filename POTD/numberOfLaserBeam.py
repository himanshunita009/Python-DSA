class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        prev_row = 0
        curr_row = 0
        ans = 0
        for row in bank:
            curr_row = row.count("1")
            ans += (curr_row*prev_row)
            prev_row = curr_row
        return ans


obj =