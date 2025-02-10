graph={
    "A":["B","C"],
    "B":["D","E"],
    "C":["F","G"],
    "D":[],
    "E":[],
    "F":[],
    "G":[]
}

def DFS(g,start):
    stack=[]
    stack.append(start)
    visited=[]

    while stack:
        node =stack.pop()
        print(f'{node}-->',end=" ")
        visited.append(node)
        for each in reversed(g[node]):
            stack.append(each)


DFS(graph,"A")