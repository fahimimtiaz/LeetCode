from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        column = len(grid[0])

        island = '1'
        not_island = '0'

        island_count = 0
        
        island_count += 1 if grid[0][0] == island else 0
        island_count += 1 if grid[0][column-1] == island and column > 1 else 0
        island_count += 1 if grid[row-1][0] == island and row > 1 else 0
        island_count += 1 if grid[row-1][column-1] == island and column > 1 and row > 1 else 0

        for clm in range(0,column):
            for rw in range(0,row):
                if clm == 0 and rw != 0 and rw != row-1:
                    if grid[rw][clm] == island and grid[rw][clm+1] == not_island and grid[rw-1][clm] == not_island and grid[rw+1][clm] == not_island:
                        island_count += 1
                elif clm == column-1 and rw != 0 and rw != row-1:
                    if grid[rw][clm] == island and grid[rw][clm-1] == not_island and grid[rw-1][clm] == not_island and grid[rw+1][clm] == not_island:
                        island_count += 1
                elif rw == 0 and clm != 0 and clm != column-1:
                    if grid[rw][clm] == island and grid[rw][clm-1] == not_island and grid[rw][clm+1] == not_island and grid[rw+1][clm] == not_island:
                        island_count += 1
                elif rw == row-1 and clm != 0 and clm != column-1:
                    if grid[rw][clm] == island and grid[rw][clm-1] == not_island and grid[rw][clm+1] == not_island and grid[rw-1][clm] == not_island:
                        island_count += 1
                else:
                    if grid[rw][clm] == island and grid[rw][clm-1] == not_island and grid[rw][clm+1] == not_island and grid[rw-1][clm] == not_island and grid[rw+1][clm] == not_island:
                        island_count += 1

        return island_count
        

ob1 = Solution()
# print(ob1.numIslands(grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]))


# print(ob1.numIslands(grid = [
#   ["1"]
# ]))


print(ob1.numIslands(grid = [
  ["1", "0"]
]))