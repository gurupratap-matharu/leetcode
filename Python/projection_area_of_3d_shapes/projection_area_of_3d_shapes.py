class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        self.grid_transpose = list(zip(*self.grid))

        base = len(['x' for row in grid for elem in row if elem != 0])
        width = (sum([max(i) for i in self.grid]))
        height = (sum([max(row) for row in self.grid_transpose]))
        return base + width + height
        

# s1 = Solution()
# print(s1.projectionArea([[1, 0], [0, 2]]))
