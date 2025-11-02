class Solution:
	def matSearch(self, mat, x):
		n = len(mat)
		m = len(mat[0])
		row = 0
		col = m-1
		while row < n and col > -1:
			curr = mat[row][col]
			if curr > mat[row][col]:
				row += 1
			elif curr < mat[row][col]:
				col -= 1
			else:
				return True
		return False