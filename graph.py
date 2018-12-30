import collections
class Node():
    def __init__(self, name):
        self.name=name
    def getName(self):
        return self.name
    def __str__(self):
        return str(self.name)

class Edge():
    def __init__(self, src, dest):
        self.src=src
        self.dest=dest
    def getSource(self):
        return self.src
    def getDest(self):
        return self.dest
    def __str__(self):
        return str(self.src.getName())+ "-->"+ str(self.dest.getName())

class Digraph():
    def __init__(self):
        self.graph={}
    def addNode(self, node):
        if node in self.graph:
            raise ValueError("Duplicate Node")
        else:
            self.graph[node]=[]
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDest()
        if not(src in self.graph and dest in self.graph):
            raise ValueError("Node not in graph")
        else:
            self.graph[src].append(dest)
    def childrenOf(self, node):
        return self.graph[node]
    def hasNode(self, node):
        return node in self.graph
    def getNode(self, name):
        for n in self.graph:
            if n.getName()==name:
                return n
        raise NameError(name)

    def __str__(self):
        result=""
        for nodeS in self.graph:
            result+="-----------------" + str(nodeS.getName()) + "-----------------" + '\n'
            for nodeE in self.graph[nodeS]:
                result+= nodeS.getName() + "-->" + nodeE.getName()
            result+='\n'
        return result

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev =Edge(edge.getDest(), edge.getSource())
        Digraph.addEdge(self, rev)

def DFS(graph, start, end, path, shortest):
    path.append(start)
    if start==end:
        return None
    for node in graph.childrenOf(start):
        if node not in path:
            print(str(node))
            newPath=DFS(graph, node, end, path, shortest)
            if newPath:
                if shortest!=0 and len(path)<len(shortest):
                    shortest=newPath
        else:
            print(f"already visited {node}")
    return shortest

def BFS(graph, start):
    visited, queue=set(), collections.deque([start])
    while(queue):
        node=queue.popleft()
        for node in graph.childrenOf(node):
            if node not in visited:
                visited.add(node)
                queue.append(node)
    print("-----------------BFS-----------------")
    for node in visited:
        print(str(node) + "-->", end="")

def main():

    g=Digraph()
    for name in ('Boston', 'Providence', 'New York', 'Chicago','Denver', 'Phoenix', 'Los Angeles'):
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    print(g)
    print("---------------------DFS---------------------")
    a=DFS(g, g.getNode('Boston'), g.getNode('Phoenix'), [], None)
    if a:
        print(a)
    BFS(g, g.getNode('Boston'))


if __name__ == '__main__':
    main()
