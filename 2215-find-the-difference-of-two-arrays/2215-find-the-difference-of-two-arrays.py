class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        unique_in_set1 = set1 - set2
        unique_in_set2 = set2 - set1
        return [list(unique_in_set1),list(unique_in_set2)]


        