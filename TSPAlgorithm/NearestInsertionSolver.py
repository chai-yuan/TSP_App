import random
from .Solver import Solver
import tsplib95
import tqdm


class NearestInsertionSolver(Solver):
    def __init__(self) -> None:
        pass

    @staticmethod
    def solve(problem: tsplib95.models.StandardProblem, describe: dict = {}) -> list:
        unvisited = list(problem.get_nodes())
        current_node = random.choice(unvisited)
        tour = [current_node]
        unvisited.remove(current_node)
        iter_num = len(unvisited)

        for _ in tqdm.trange(iter_num):
            # Step 2: Find the nearest unvisited node to the tour
            min_distance = float('inf')
            for node in unvisited:
                for tour_node in tour:
                    weight = problem.get_weight(tour_node, node)
                    if weight < min_distance:
                        min_distance = weight
                        next_node = node

            # Step 3: Find the best place to insert next_node into the tour
            min_insertion_cost = float('inf')
            for i in range(len(tour)):
                insertion_cost = problem.get_weight(tour[i - 1], next_node) + problem.get_weight(
                    tour[i], next_node) - problem.get_weight(tour[i - 1], tour[i])
                if insertion_cost < min_insertion_cost:
                    min_insertion_cost = insertion_cost
                    insertion_index = i

            # Insert next_node into the tour
            tour.insert(insertion_index, next_node)
            unvisited.remove(next_node)

        # Return to the starting node
        tour.append(tour[0])

        return tour
