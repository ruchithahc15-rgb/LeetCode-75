import heapq
class SmallestInfiniteSet:
    def __init__(self):
        self.curr = 1
        self.heap = []
        self.seen = set()
    def popSmallest(self) -> int:
        if self.heap:
            smallest = heapq.heappop(self.heap)
            self.seen.remove(smallest)
            return smallest
        smallest = self.curr
        self.curr += 1
        return smallest
    def addBack(self, num: int) -> None:
        if num < self.curr and num not in self.seen:
            heapq.heappush(self.heap, num)
            self.seen.add(num)