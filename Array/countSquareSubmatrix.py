class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[0]*m for _ in range(n)]
        total = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1   # first row/col
                    else:
                        # dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                        dp[i][j] = 1 + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
                    total += dp[i][j]
        
        return total

# class Solution():
#     def calcPrefix2DMatrix(self,matrix: list[list[int]]):
#         n = len(matrix)
#         m = len(matrix[0])
#         tempMat = matrix.copy()
#         for j in range(1,m):
#             tempMat[0][j] += tempMat[0][j-1]
#         for i in range(1,n):
#             tempMat[i][0] += tempMat[i-1][0]
#         for i in range(1,n):
#             for j in range(1,m):
#                 tempMat[i][j] = tempMat[i][j] + tempMat[i-1][j] + tempMat[i][j-1] - tempMat[i-1][j-1]
#         return tempMat 
        
#     def kSubMatrix(self,matrix:list[list[int]],k : int):
#         n = len(matrix)
#         m = len(matrix[0])
#         r2 = c2 = k-1
#         ans = 0
#         while r2 < n:
#             c2 = k-1
#             while c2 < m:
#                 r1 = r2 - k +1
#                 c1 = c2 - k + 1
#                 sum = matrix[r2][c2]
#                 if r1 >0 :
#                     sum -= matrix[r1-1][c2] 
#                 if c1 > 0:
#                     sum -= matrix[r2][c1-1] 
#                 if r1 > 0 and c1 > 0:
#                     sum += matrix[r1-1][c1-1]
#                 if sum == k*k:
#                     ans += 1
#                 c2 += 1
#             r2 += 1
#         return ans
#     def countSquares(self, matrix: list[list[int]]) -> int:
#         n = len(matrix)
#         m = len(matrix[0])
#         k = min(n,m)
#         ans =0
#         tempMat = self.calcPrefix2DMatrix(matrix)
#         for i in range(1,k+1):
#             ans += self.kSubMatrix(matrix,i)
#         return ans

# obj = Solution()
# print(obj.countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]]))
            
# # class Solution:
# #     def solve(self,matrix: list[list[int]],k : int,n: int,m: int):
# #         temp = [[0]*(m-k+1) for _ in range(n)]
# #         for i in range(n):
# #             j = 0
# #             tempSum = 0
# #             while j < m:
# #                 tempSum += matrix[i][j]
# #                 if j >=k-1 :
# #                     temp[i][j-k+1] = tempSum
# #                     tempSum -= matrix[i][j-k+1]
# #                 j += 1
# #         temp2 = [[0]*(m-k+1) for _ in range(n-k+1)]
# #         for j in range(m-k+1):
# #             i =0
# #             tempSum = 0
# #             while i < n:
# #                 tempSum += temp[i][j]
# #                 if i >= k-1:
# #                     temp2[i-k+1][j] = tempSum
# #                     tempSum -= temp[i-k+1][j]
# #                 i += 1
# #         ans = 0
# #         for row in range(len(temp2)):
# #             for col in range(len(temp[0])):
# #                 if temp2[row][col] == k*k:
# #                     ans += 1
            
# #         return ans
# #     def countSquares(self, matrix: list[list[int]]) -> int:
# #         n = len(matrix)
# #         m = len(matrix[0])
# #         k = min(n,m)
# #         ans =0
# #         for i in range(1,k+1):
# #             ans += self.solve(matrix,i,n,m)
# #         return ans

#         # print(self.solve(matrix,1,n,m))
    
