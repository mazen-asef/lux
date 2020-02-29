import pprint
from collections import defaultdict

class Graph (object):

    """ Graph data structure, directed by default """

    def __init__ (self, connections, text, directed = True):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections (connections)
        
    def add_connections (self, connections):
        """ Add connections (list of tuple pairs) to graph """
        
        for node1, node2 in connections:
            self.add (node1, node2)
            
    def add (self, node1, node2):
        """ Add connection between node1 and node2 """
        
        self._graph[node1].add (node2)
        if not self._directed:
            self._graph[node2].add (node1)
    
    def remove (self, node):
        """ Remove all references to node """
        
        for n, cnxs in self._graph.items ():
            try:
                cnxs.remove (node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass
        
    def __str__ (self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))
        

def main():
    connections = [('A', 'B'), ('B', 'C'), ('B', 'D'),
                   ('C', 'D'), ('E', 'F'), ('F', 'C')]
    g = Graph(connections, directed = True)
    pretty_print = pprint.PrettyPrinter()
    pretty_print.pprint(g._graph)
    
    
    
    
    
    
    
    
    
    
    
    
