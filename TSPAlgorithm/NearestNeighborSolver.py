import random
import sys
from .Solver import Solver
import tsplib95
import tqdm


class NearestNeighborSolver(Solver):
    def __init__(self) -> None:
        pass

    @staticmethod
    def solve(problem: tsplib95.models.StandardProblem, describe: dict = {}) -> list:
        unvisited = list(problem.get_nodes())
        current_node = random.choice(unvisited)
        unvisited.remove(current_node)
        tour = [current_node]
        iter_num = len(unvisited)

        for _ in tqdm.trange(iter_num):
            nearest_node = None
            nearest_dis = sys.maxsize
            for next_node in unvisited:
                if problem.get_weight(current_node, next_node) < nearest_dis:
                    nearest_node = next_node
                    nearest_dis = problem.get_weight(current_node, next_node)

            current_node = nearest_node
            unvisited.remove(nearest_node)
            tour.append(current_node)

        return tour
