from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        provinces = 0
        
        def dfs(city):
            # Explore all potential neighbor cities
            for neighbor in range(n):
                # If they are connected and we haven't visited the neighbor yet
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        # Iterate through every city
        for i in range(n):
            if i not in visited:
                # Found a new unvisited city = a new province cluster
                provinces += 1
                visited.add(i)
                dfs(i) # Mark all connected cities
                
        return provinces
