class Solution:
    def calcEquation(self, equations, values, queries):

        graph = collections.defaultdict(list)

        # Build graph
        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))

        def dfs(current, target, visited):

            if current == target:
                return 1.0

            visited.add(current)

            for neighbor, value in graph[current]:
                if neighbor not in visited:

                    result = dfs(neighbor, target, visited)

                    if result != -1.0:
                        return value * result

            return -1.0

        answer = []

        for a, b in queries:

            if a not in graph or b not in graph:
                answer.append(-1.0)
            else:
                answer.append(dfs(a, b, set()))

        return answer