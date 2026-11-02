class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return 0
        nums.sort()
        median = nums[len(nums) // 2]
        moves = 0
        for num in nums:
            moves += abs(num - median)
        return moves