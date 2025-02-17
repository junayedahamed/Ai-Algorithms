graph = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Oradea', 71), ('Arad', 75)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Pitesti', 97), ('Craiova', 146)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Bucharest', 101), ('Craiova', 138)],
    'Craiova': [('Pitesti', 138), ('Rimnicu Vilcea', 146), ('Dobreta', 120)],
    'Dobreta': [('Craiova', 120), ('Mehadia', 75)],
    'Mehadia': [('Dobreta', 75), ('Lugoj', 70)],
    'Lugoj': [('Mehadia', 70), ('Timisoara', 111)],
    'Timisoara': [('Lugoj', 111), ('Arad', 118)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}

# Define heuristic values (straight-line distances to Bucharest)
heuristic = {
    'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Dobreta': 242, 'Eforie': 161, 'Fagaras': 176,
    'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234,
    'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193, 'Sibiu': 253, 'Timisoara': 329,
    'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
}
