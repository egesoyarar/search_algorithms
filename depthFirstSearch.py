from collections import deque
 
def expandBFS(frontier, nodes, visited):
    curLeaf = frontier[0]
    if curLeaf in nodes:
        frontier.extend(getUnvisited(nodes[curLeaf], visited))
    else:
        print("The {} is dead end!".format(curLeaf))
    frontier.pop(0)

def getUnvisited(childs, visited):
    unvisited = []
    for x in childs:
        if x not in visited:
            unvisited.append(x)
    return unvisited

def dfs(root, nodes, dest):
    visited = []

    stack = deque()
    stack.append(root)

    while stack:
        curLeaf = stack.pop()
        visited.append(curLeaf)

        if(curLeaf == dest):
            print("The algo reached {}!".format(dest))
            print(visited)
            return True
        
        expandBFS(stack, nodes, visited)

    return False
