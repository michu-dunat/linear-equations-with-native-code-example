import numpy
from linear_lib import linear_equations_system_solver

if __name__ == "__main__":
    solver = linear_equations_system_solver.LinearEquationsSystemSolver()
    array = numpy.array([[2.0, 1.0, 1.0, 3.0], [1.0, -1.0, 1.0, 4.0], [1.0, 1.0, 1.0, 2.0]], numpy.float64)
    result = solver.solve_system(array)
    print(result)