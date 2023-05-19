from .Solver import Solver
import tsplib95
import tqdm
import networkx as nx
from networkx.algorithms.approximation import min_weighted_dominating_set
from networkx.algorithms.matching import max_weight_matching
from networkx.algorithms.euler import eulerian_circuit


class ChristofidesSolver(Solver):
    def __init__(self) -> None:
        pass

    @staticmethod
    def solve(problem: tsplib95.models.StandardProblem, describe: dict = {}) -> list:
        # Create a graph from the problem
        graph = problem.get_graph()

        # Step 1: Create a minimum spanning tree of graph
        tree = nx.minimum_spanning_tree(graph)

        # Step 2: Find set O of vertices with odd degree in tree
        O = [v for v, d in tree.degree() if d % 2 == 1]

        # Step 3: Find a minimum-weight perfect matching M in the subgraph of G induced by O
        subgraph = graph.subgraph(O)
        M = max_weight_matching(subgraph, maxcardinality=True)

        # Add the edges of M to T, resulting in an Eulerian multigraph T′
        T_prime = tree.copy()
        T_prime.add_edges_from(M)

        # Step 4: Form an Eulerian circuit in T′
        circuit = list(eulerian_circuit(T_prime))

        # Step 5: Make the circuit found into a Hamiltonian circuit H by skipping repeated vertices
        Hamiltonian = []
        visited = set()

        for u, v in circuit:
            if u not in visited:
                Hamiltonian.append(u)
                visited.add(u)

            # If we have visited all nodes and there is a direct edge from current node to the start node
            # We can directly go to the start node and finish the cycle.
            if len(visited) == graph.number_of_nodes() and graph.has_edge(u, Hamiltonian[0]):
                Hamiltonian.append(Hamiltonian[0])
                break

        print(Hamiltonian)
        return Hamiltonian

    @staticmethod
    def setting() -> str:
        return ''
