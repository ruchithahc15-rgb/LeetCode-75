class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        n = len(s)
        
        # Step 1: Count first window
        current_count = sum(1 for ch in s[:k] if ch in vowels)
        max_count = current_count
        
        # Step 2: Slide the window
        for i in range(k, n):
            if s[i] in vowels:   # new found
                current_count += 1
            if s[i - k] in vowels:  # kicked out
                current_count -= 1
            max_count = max(max_count, current_count)
        
        return max_count