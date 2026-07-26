class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        ans = 0
        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + gain[i]
        ans = max(prefix)
        return ans
        