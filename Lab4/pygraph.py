from typing import Tuple, Union, Iterable
Node = Union[str, int]
Edge = Tuple[Node, Node]



class Graph(object):
    """Graph data structure, undirected by default."""
    def __init__(self, edges: Iterable[Edge] = [], directed: bool = False):
        raise NotImplementedError()


    def has_node(self, node: Node):
            """Whether a node is in graph"""
            raise NotImplementedError()
    def has_edge(self, edge: Edge):



     """Whether an edge is in graph"""
     raise NotImplementedError()
    def add_node(self, node: Node):
       """Add a node"""
       raise NotImplementedError()


    def add_edge(self, edge: Edge):


         """Add an edge (node1, node2). For directed graph, node1 -> node2"""
         raise NotImplementedError()
    def remove_node(self, node: Node):
     """Remove all references to node"""


     raise NotImplementedError()
    def remove_edge(self, edge: Edge):


           """Remove an edge from graph"""
           raise NotImplementedError()
    def indegree(self, node: Node) -> int:
      """Compute indegree for a node"""
      raise NotImplementedError()
    def outdegree(self, node: Node) -> int:


        """Compute outdegree for a node"""
        raise NotImplementedError()
        
    def __str__(self):
         raise NotImplementedError()
    def __repr__(self):



          raise NotImplementedError()
