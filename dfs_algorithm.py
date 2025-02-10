graph={
    "A":["B","C"],
    "B":["D","E"],
    "C":["F","G"],
    "D":[],
    "E":[],
    "F":[],
    "G":[]
}

def dfs(g,start):
    queue=[]
    queue.append(start)
    visited=[]

    while queue:
        node =queue.pop(0)
        print(node,end=" ")
        visited.append(node)
        for i in g[node]:
            queue.append(i)






dfs(graph,"A")