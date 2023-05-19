import random
import math
from .Solver import Solver
from .NearestNeighborSolver import NearestNeighborSolver
import tsplib95
import tqdm


class SASolver(Solver):
    def __init__(self) -> None:
        pass

    @staticmethod
    def solve(problem: tsplib95.models.StandardProblem,  describe: dict = {}) -> list:
        T = float(describe["temp"])
        T_end = float(describe["temp_end"])
        alpha = float(describe["alpha"])

        # 创建初始解（随机解）
        nodes = NearestNeighborSolver.solve(problem)

        best = nodes[:]
        while T > T_end:
            i = random.randint(0, len(nodes) - 1)
            j = random.randint(0, len(nodes) - 1)

            nodes[i], nodes[j] = nodes[j], nodes[i]
            delta_E = SASolver.calculate_distance(
                nodes, problem) - SASolver.calculate_distance(best, problem)

            P = math.exp(-delta_E / T)
            r = random.random()

            if delta_E < 0 or r < P:
                best = nodes[:]
            else:
                nodes[i], nodes[j] = nodes[j], nodes[i]
            T *= alpha

        return best

    @staticmethod
    def setting() -> str:
        return '<label>初始温度</label>\
            <input type="number" id="temp" name="temp"  value="1000">\
            <label>终止温度</label>\
            <input type="number" id="temp_end" name="temp_end"  value="0.001">\
            <label>降温速率</label>\
            <input type="number" id="alpha" name="alpha"  value="0.98">'

    @staticmethod
    def calculate_distance(route: list, problem: tsplib95.models.StandardProblem):
        distance = 0
        for i in range(len(route)-1):
            distance += problem.get_weight(route[i], route[i+1])
        return distance
