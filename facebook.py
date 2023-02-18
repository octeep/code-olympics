import networkx as nx
import os

def max_clique_dyn(G):
    n = len(G)
    cliques = {frozenset(): set()}  # initialize the table
    for k in range(1, n+1):  # loop over clique sizes
        cliques_k = {}
        for S in cliques:
            if len(S) != k-1:
                continue
            for v in set(G) - S:
                if all(v in G[u] for u in S):
                    S_v = S | {v}
                    cliques_k[S_v] = S | {v}
        cliques.update(cliques_k)
    return max(cliques, key=lambda S: len(S))


def get_biggest_group(friendsFile: str) -> nx.Graph:
    G = nx.Graph()
    if friendsFile not in os.listdir():
        raise ValueError("name of friends file incorrect: did you add .txt?")
    with open(os.path.join(os.getcwd(), friendsFile)) as f:
        for line in f.readlines():
            user1, user2 = line.split()
            G.add_edge(user1, user2)
            G.add_edge(user2, user1)
    return max_clique_dyn(G)
