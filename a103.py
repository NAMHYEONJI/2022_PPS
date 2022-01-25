class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []

        col = len(matrix[0])
        row = len(matrix)
        
        for c in range(col):
            res.append([]) 
            for r in range(row):
                res[c].append(matrix[r][c])
        return res
