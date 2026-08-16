class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for a, b in connections:
            adj[a].append((b, 1))
            adj[b].append((a, 0))

        ans = [0]
        visited = [False] * n

        def dfs(node):
            visited[node] = True

            for neighbor, direction in adj[node]:
                if not visited[neighbor]:
                    if direction == 1:
                        ans[0] += 1

                    dfs(neighbor)

        dfs(0)
        return ans[0]