import random
import numpy
from .Solver import Solver
import tsplib95
import tqdm


class TwoOptSolver(Solver):
    def __init__(self) -> None:
        pass

    @staticmethod
    def solve(problem: tsplib95.models.StandardProblem,  describe: dict = {}) -> list:
        algorithm_iter = int(describe["algorithm_iter"])
        # 创建初始解（随机解）
        nodes = list(problem.get_nodes())
        random.shuffle(nodes)

        best = nodes
        for _ in tqdm.trange(algorithm_iter):
            i = random.randint(1, len(nodes) - 3)
            j = random.randint(i+2, len(nodes)-1)
            newRoute = nodes[:]
            newRoute[i:j] = nodes[j - 1:i - 1:-1]
            if TwoOptSolver.calculate_distance(newRoute, problem) < TwoOptSolver.calculate_distance(best, problem):
                best = newRoute

            nodes = best
        return nodes

    @staticmethod
    def setting() -> str:
        return '<label>算法迭代次数</label> \
                <input type="number" id="algorithm_iter" name="algorithm_iter" min="1" value="20000">'

    @staticmethod
    def calculate_distance(route: list, problem: tsplib95.models.StandardProblem):
        distance = 0
        for i in range(len(route) - 1):
            distance += problem.get_weight(route[i], route[i+1])
        return distance + problem.get_weight(route[-1], route[0])
