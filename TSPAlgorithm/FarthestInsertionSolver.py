import random
from .Solver import Solver
import tsplib95
import tqdm


class FarthestInsertionSolver(Solver):
    def __init__(self) -> None:
        pass

    @staticmethod
    def find_farthest_city(tour, unvisited, problem):
        farthest_city = None
        max_distance = -1
        for city in unvisited:
            min_distance = min(problem.get_weight(
                city, visited) for visited in tour)
            if min_distance > max_distance:
                farthest_city = city
                max_distance = min_distance
        return farthest_city

    @staticmethod
    def find_best_position(city, tour, problem):
        best_position = 0
        min_increase = float('inf')
        for i in range(len(tour)):
            increase = (problem.get_weight(city, tour[i-1]) +
                        problem.get_weight(city, tour[i]) -
                        problem.get_weight(tour[i-1], tour[i]))
            if increase < min_increase:
                best_position = i
                min_increase = increase
        return best_position

    @staticmethod
    def solve(problem: tsplib95.models.StandardProblem, describe: dict = {}) -> list:
        unvisited = list(problem.get_nodes())
        current_node = random.choice(unvisited)
        tour = [current_node]
        unvisited.remove(current_node)
        iter_num = len(unvisited)

        for _ in tqdm.trange(iter_num):
            farthest_city = FarthestInsertionSolver.find_farthest_city(
                tour, unvisited, problem)
            unvisited.remove(farthest_city)
            best_position = FarthestInsertionSolver.find_best_position(
                farthest_city, tour, problem)
            tour.insert(best_position, farthest_city)

        return tour
