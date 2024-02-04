import networkx as nx
from itertools import permutations

def is_pareto_efficient(valuations, allocation):
    # Create directed graph
    G = nx.DiGraph()
    n = len(valuations)  # Number of players
    G.add_nodes_from(range(n))

    # Add edges with weights
    for i, j in permutations(range(n), 2):
        smallest_valued_object_by_i = min([obj for obj, alloc in enumerate(allocation[i]) if alloc > 0], key=lambda x: valuations[i][x])
        if allocation[j][smallest_valued_object_by_i] > 0:  # If j has the object i values the least
            weight = valuations[i][smallest_valued_object_by_i] / valuations[j][smallest_valued_object_by_i]
            G.add_edge(i, j, weight=weight)

    # Check for Pareto efficiency
    for cycle in nx.simple_cycles(G):
        product_of_weights = 1
        for i in range(len(cycle)):
            j = (i + 1) % len(cycle)
            product_of_weights *= G[cycle[i]][cycle[j]]['weight']
        if product_of_weights < 1:
            return False  # Found a cycle where product of weights is less than 1
    
    return True  # No such cycle found, distribution is Pareto efficient

# Example usage
valuations = [[10, 20, 30, 40], [40, 30, 20, 10]]
allocation = [[0, 0.7, 1, 1], [1, 0.3, 0, 0]]
print(is_pareto_efficient(valuations, allocation))