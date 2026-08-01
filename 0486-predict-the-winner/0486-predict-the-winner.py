class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        # Dictionary to store calculated subproblems (Memoization)
        memo = {}
        
        def get_max_diff(i, j):
            # Base Case: Only one number left, the current player must take it
            if i == j:
                return nums[i]
            
            # If already calculated, return the cached result
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Option 1: Pick left element, subtract the opponent's optimal future score
            pick_left = nums[i] - get_max_diff(i + 1, j)
            
            # Option 2: Pick right element, subtract the opponent's optimal future score
            pick_right = nums[j] - get_max_diff(i, j - 1)
            
            # Store and return the best choice for the current player
            memo[(i, j)] = max(pick_left, pick_right)
            return memo[(i, j)]
        
        # Player 1 wins if the maximum net score difference is >= 0
        return get_max_diff(0, len(nums) - 1) >= 0
