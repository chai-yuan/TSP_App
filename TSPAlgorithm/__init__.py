from .Solver import Solver
from .NearestNeighborSolver import NearestNeighborSolver
from .NearestInsertionSolver import NearestInsertionSolver
from .FarthestInsertionSolver import FarthestInsertionSolver
from .TwoOptSolver import TwoOptSolver
from .LKHSolver import LKHSolver
from .ChristofidesSolver import ChristofidesSolver
from .SASolver import SASolver
from .TestSolver import TestSolver

TSP_Solver: dict = {"NearestNeighborSolver": NearestNeighborSolver,
                    "NearestInsertionSolver": NearestInsertionSolver,
                    "FarthestInsertionSolver": FarthestInsertionSolver,
                    "2_OptSolver": TwoOptSolver,
                    "ChristofidesSolver": ChristofidesSolver,
                    "LKHSolver": LKHSolver,
                    "SASolver": SASolver,
                    "TestSolver": TestSolver}
