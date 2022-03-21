import ctypes
import numpy
import glob

class LinearEquationsSystemSolver:

    def __init__(self) -> None:
        # find the shared library, the path depends on the platform and Python version
        self.libfile = glob.glob('./**/gauss*.so', recursive = True)[0]
        # 1. open the shared library
        self.mylib = ctypes.CDLL(self.libfile)
        # 2. tell Python the argument and result types of function gaussianElimination
        self.mylib.gaussianElimination.restype = None
        self.mylib.gaussianElimination.argtypes = [numpy.ctypeslib.ndpointer(dtype=numpy.float64, ndim=2), numpy.ctypeslib.ndpointer(dtype=numpy.float64)]

    def solve_system(self, input_array):
        result = numpy.zeros(3)
        # 3. call function gaussianElimination
        self.mylib.gaussianElimination(input_array, result)
        return result
