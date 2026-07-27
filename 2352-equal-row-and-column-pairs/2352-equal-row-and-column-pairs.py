class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        pair_count = 0
        row_count = Counter(tuple(row) for row in grid)
        for col in zip(*grid):
            pair_count += row_count[col]
        return pair_count
        
        