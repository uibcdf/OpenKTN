
class Component():


    def __init__(self, nodes=None, index=None, weight=0):

        self.n_nodes=0
        self.n_edges=0

        self.index=None
        self.node=set()
        self.edge=set()
        self.weight=0.0
        self.probability=None

        self.symmetrized=False
        self.T_arrays=None

        if nodes is not None:
            self.n_nodes=len(nodes)
            for index_in_component in range(self.n_nodes):
                node = nodes[index_in_component]
                self.edge.union(set(node.edge.values()))
                self.node.add(node)
                self.weight+=node.weight
                if node.probability is not None:
                    self.probability+=node.probability
            self.n_edges=len(self.edge)

