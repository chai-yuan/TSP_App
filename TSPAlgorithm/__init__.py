from .Solver import Solver
from .NearestNeighborSolver import NearestNeighborSolver
from .NearestInsertionSolver import NearestInsertionSolver
from .FarthestInsertionSolver import FarthestInsertionSolver
from .TwoOptSolver import TwoOptSolver

TSP_Solver: dict = {"NearestNeighborSolver": NearestNeighborSolver,
                    "NearestInsertionSolver": NearestInsertionSolver,
                    "FarthestInsertionSolver": FarthestInsertionSolver,
                    "2_OptSolver": TwoOptSolver}
