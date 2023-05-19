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
        nodes = problem.node_coords.items()

        graph = {k: v for k, v in nodes}

        cities = elkai.Coordinates2D(graph)

        solution = cities.solve_tsp(algorithm_iter)

        return solution

    @staticmethod
    def setting() -> str:
        return '<label>算法迭代次数</label> \
                <input type="number" id="algorithm_iter" name="algorithm_iter" min="1" value="5">'
