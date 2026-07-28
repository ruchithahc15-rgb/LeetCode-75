from collections import deque

class RecentCounter:

    def __init__(self):
        # Initialize an empty queue to store timestamps
        self.queue = deque()

    def ping(self, t: int) -> int:
        # 1. Add the new request timestamp to the back of the queue
        self.queue.append(t)
        
        # 2. Check the front of the queue. 
        # While the oldest timestamp is out of the 3000ms window, remove it.
        while self.queue[0] < t - 3000:
            self.queue.popleft()
            
        # 3. The length of the queue is the number of valid recent requests
        return len(self.queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
