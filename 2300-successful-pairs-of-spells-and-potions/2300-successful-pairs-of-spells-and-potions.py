class Solution:
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        n = len(potions)
        ans = []
        for spell in spells:
            left = 0
            right = n - 1
            while left <= right:
                mid = (left + right) // 2
                if spell * potions[mid] >= success:
                    right = mid - 1
                else:
                    left = mid + 1
            ans.append(n - left)
        return ans