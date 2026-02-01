class Solution:
    def rangeAddQueries(self, n: int, queries: list[list[int]]) -> list[list[int]]:
        mat = [[0]*(n+1) for _ in range(n+1)]
        for row1,col1,row2,col2 in queries:
            mat[row1][col1] += 1
            mat[row2+1][col1] -= 1
            mat[row1][col2+1] -= 1
            mat[row2+1][col2+1] += 1
        for row in range(n):
            for col in range(n):
                mat[row][col] += mat[row][col+1]
        for col in range(n):
            for row in range(n):
                mat[row+1][col] += mat[row+1][col]
        return [row[:n] for row in mat[:n]]