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

def bfs(root, nodes, dest):
    visited = []
    frontier = [root]

    while frontier:
        curLeaf = frontier[0]
        visited.append(curLeaf)

        if(curLeaf == dest):
            print("The algo reached {}!".format(dest))
            print(visited)
            return True
        
        expandBFS(frontier, nodes, visited)

    return False

        
if __name__ == "__main__":
    root = "A"
    nodes = {"A":["B","C"], "B":["A","D","E"], "C":["F","G"], "D":["A"], "E":["K"]}
    dest = "K"
    result = bfs(root, nodes, dest)
    print(result)
