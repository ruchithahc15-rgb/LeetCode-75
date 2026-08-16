class Solution:
    # Repeatedly traverse list until all connections made. Somewhat of a BFS flavour?
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        connected = [False] * n
        connected[0] = True
        res = 0
        while connections:
            to_process = []
            for a, b in connections:                
                if connected[a]:
                    res += 1
                    connected[b] = True
                elif connected[b]:
                    connected[a] = True
                else:
                    to_process.append((a, b))
            connections = to_process[::-1]
        return res
