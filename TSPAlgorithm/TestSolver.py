import random
from .Solver import Solver
import tsplib95
import tqdm


class TestSolver(Solver):
    def __init__(self) -> None:
        pass

    @staticmethod
    def solve(problem: tsplib95.models.StandardProblem,  describe: dict = {}) -> list:
        nodes = []
        node_coords = problem.node_coords.items()
        sorted_nodes_0 = sorted(node_coords, key=lambda x: - x[1][0] - x[1][1])
        sorted_nodes_1 = sorted(node_coords, key=lambda x: - x[1][0] + x[1][1])
        sorted_nodes_2 = sorted(node_coords, key=lambda x:   x[1][0] + x[1][1])
        sorted_nodes_3 = sorted(node_coords, key=lambda x:   x[1][0] - x[1][1])

        while len(sorted_nodes_3):
            nodes.append(sorted_nodes_0[-1][0])
            nodes.append(sorted_nodes_1[-1][0])
            nodes.append(sorted_nodes_2[-1][0])
            nodes.append(sorted_nodes_3[-1][0])
            sorted_nodes_0.pop()
            sorted_nodes_1.pop()
            sorted_nodes_2.pop()
            sorted_nodes_3.pop()

        return nodes
