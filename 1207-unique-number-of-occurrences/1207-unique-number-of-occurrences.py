class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        occurences = count.values()
        return len(occurences) == len(set(occurences))

        