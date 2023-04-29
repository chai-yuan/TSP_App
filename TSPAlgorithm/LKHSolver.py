import random
import numpy
from .Solver import Solver
import tsplib95
import elkai


class LKHSolver(Solver):
    def __init__(self) -> None:
        pass

    @staticmethod
    def solve(problem: tsplib95.models.StandardProblem,  describe: dict = {}) -> list:
        algorithm_iter = int(describe["algorithm_iter"])
        nodes = list(problem.get_nodes())
        graph = numpy.zeros((len(nodes), len(nodes)), dtype=int)

        for i in nodes:
            for j in nodes:
                if i != j:
                    graph[i-1, j-1] = problem.get_weight(i, j)

        solution = elkai.solve_int_matrix(graph, algorithm_iter)
        solution = [i+1 for i in solution]

        return solution

    @staticmethod
    def setting() -> str:
        return '<label>算法迭代次数</label> \
                <input type="number" id="algorithm_iter" name="algorithm_iter" min="1" value="5">'
