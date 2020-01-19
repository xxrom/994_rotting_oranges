from typing import List, Dict, Tuple


class Solution:
    def getNewRotting(self, grid: List[List[int]], pair: Tuple[int, int]):
        i = pair[0]
        j = pair[1]

        newActive = []
        # top
        if i > 0 and grid[i - 1][j] == 1:
            newActive.append([i - 1, j])
            grid[i - 1][j] = 2
            self.fresh -= 1
        # right
        if j < len(grid[i]) - 1 and grid[i][j + 1] == 1:
            newActive.append([i, j+1])
            grid[i][j + 1] = 2
            self.fresh -= 1
        # bottom
        if i < len(grid) - 1 and grid[i + 1][j] == 1:
            newActive.append([i + 1, j])
            grid[i + 1][j] = 2
            self.fresh -= 1
        # left
        if j > 0 and grid[i][j - 1] == 1:
            newActive.append([i, j - 1])
            grid[i][j - 1] = 2
            self.fresh -= 1

        return newActive

    def findAllFreshOranges(self, grid: List[List[int]]) -> bool:
        check = False
        for list in grid:
            for item in list:
                if item == 1:
                    check = True

        return check

    def rotting(self, grid: List[List[int]], active: List[Tuple[int, int]], minutes: int = 0) -> int:
        newActive = []
        for pair in active:
            bitOfActive = self.getNewRotting(grid, pair)
            if len(bitOfActive) > 0:
                newActive = newActive + bitOfActive

        if len(newActive) > 0:
            return self.rotting(grid, newActive, minutes + 1)
        else:
            return minutes

    def findActiveOranges(self, grid: List[List[int]]) -> List[Tuple[int, int]]:
        active = []
        self.fresh = 0
        for i, list in enumerate(grid):
            for j, item in enumerate(list):
                # Count fresh
                if (item == 1):
                    self.fresh += 1
                # Count rotting
                if (item == 2):
                    active.append([i, j])

        return active

    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = self.rotting(grid, self.findActiveOranges(grid))
        # Old way to check fresh oranges =)
        # isHaveFreshOrange = self.findAllFreshOranges(grid)

        return minutes if self.fresh == 0 else -1


run = Solution()

grid0 = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
grid1 = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
grid2 = [[0, 2]]

print('ans minutes = %d' % run.orangesRotting(grid0))
