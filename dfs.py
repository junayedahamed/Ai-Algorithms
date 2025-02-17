g={
    1:[(2,1),(3,2)],
    2:[(4,1),(5,3)],
    3:[(6,3),(7,2)],
    4:[(8,3),(9,1)],
    5:[(10,3),(11,5)],
    6:[(13,2),(14,4)],
    7:[(15,4),(16,3)],
    8:[],
    9:[],
    10:[],
    11:[],
    12:[],
    13:[],
    14:[],
    15:[],
    16:[],
}

def dfs(g,start):
    visited=[]
    cost=0
    queue=[]
    queue.append(start)
    while queue:
        node =queue.pop(0)
        visited.append(node)
        print(node,end=" ")
        mylist=g[node]
        for value in mylist:
            # print(value[1])
            cost+=value[1]
            queue.append(value[0])
    # return  cost


print(dfs(g,1))

