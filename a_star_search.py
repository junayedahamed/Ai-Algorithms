import heapq

# Define the G.graph (city connections and distances)
import  graph_and_huristics as G
# A* Search Algorithm
def astar_search(start, goal):
    open_list = []
    heapq.heappush(open_list, (G.heuristic[start], 0, start, [start]))  # (f, g, node, path)
    visited = set()

    while open_list:
        f, g, node, path = heapq.heappop(open_list)

        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return path, g  # Return the path and total cost

        for neighbor, cost in G.graph.get(node, []):
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + G.heuristic[neighbor]
                heapq.heappush(open_list, (new_f, new_g, neighbor, path + [neighbor]))

    return None, float('inf')  # No path found

# Best-First Search Algorithm
def best_first_search(start, goal):
    open_list = []
    heapq.heappush(open_list, (G.heuristic[start], start, [start]))  # (h, node, path)
    visited = set()

    while open_list:
        h, node, path = heapq.heappop(open_list)

        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return path  # Return the path

        for neighbor, cost in G.graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(open_list, (G.heuristic[neighbor], neighbor, path + [neighbor]))

    return None  # No path found

# Run A* and Best-First Search from 'Arad' to 'Bucharest'
# value=input()
astar_path, astar_cost = astar_search('Arad', 'Bucharest')
best_first_path = best_first_search('Arad', 'Bucharest')

# Output the results
print("A* search path:", astar_path, "Cost of A star:", astar_cost)
print("BFS Path:", best_first_path)