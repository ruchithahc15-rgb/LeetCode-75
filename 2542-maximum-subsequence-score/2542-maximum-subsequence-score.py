class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:

        pairs = sorted(
            zip(nums1, nums2),
            key=lambda x: x[1],
            reverse=True
        )

        heap = []
        total = 0
        ans = 0

        for n1, n2 in pairs:

            heapq.heappush(heap, n1)
            total += n1

            if len(heap) > k:
                smallest = heapq.heappop(heap)
                total -= smallest

            if len(heap) == k:
                score = total * n2
                ans = max(ans, score)

        return ans