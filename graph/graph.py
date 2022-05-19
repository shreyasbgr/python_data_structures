from numpy import short


class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.graph_dict = {}
        for start,end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start]=[end]
        print(self.graph_dict)
    
    def find_paths(self,start,end):
        
        if start == end:
            return [[start]]
        
        if start not in self.graph_dict:
            return []
        all_paths = []
        for node in self.graph_dict[start]:
            next_paths = self.find_paths(node,end)
            if next_paths:
                for i in range(len(next_paths)):
                    next_paths[i] = [start]+next_paths[i]
                all_paths = all_paths +next_paths
        return all_paths
    
    def find_shortest_path(self,start,end):

        if start == end:
            return [start]
        
        if start not in self.graph_dict:
            return []
        
        all_shortest_paths = []
        for node in self.graph_dict[start]:
            shortest_next_path = self.find_shortest_path(node,end)
            if shortest_next_path:
               all_shortest_paths.append(shortest_next_path)
        
        if not all_shortest_paths:
            return []
        else:
            shortest_path = all_shortest_paths[0]
            for i in range(1,len(all_shortest_paths)):
                if len(shortest_path) > len(all_shortest_paths[i]):
                    shortest_path = all_shortest_paths[i]
            shortest_path = [start] +shortest_path
            return shortest_path      


if __name__ =='__main__':
    routes = {
        ("Mumbai","Paris"),
        ("Mumbai","Dubai"),
        ("Mumbai","Sydney"),
        ("Sydney","Toronto"),
        ("Paris","Dubai"),
        ("Paris","New York"),
        ("Dubai","New York"),
        ("New York","Toronto")
    }

    g1 = Graph(routes)
    paths = g1.find_shortest_path("Mumbai","New York")
    print(paths)

