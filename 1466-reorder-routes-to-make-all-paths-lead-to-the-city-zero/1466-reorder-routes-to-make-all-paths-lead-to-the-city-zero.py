class Solution:
    def dfs(self, i, visited, adj, ans):
        visited[i] = True

        for node, direction in adj[i]:
            if not visited[node]:
                if direction:
                    ans[0] += 1

                self.dfs(node, visited, adj, ans)

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        ans = [0]
        visited = [False] * n
        adj = [[] for _ in range(n)]

        for u, v in connections:
            adj[u].append((v, True))
            adj[v].append((u, False))

        self.dfs(0, visited, adj, ans)

        return ans[0]