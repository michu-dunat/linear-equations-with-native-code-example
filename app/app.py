from linear_lib import linear_equations_system_solver
import numpy


class App:
    def __init__(self, input_file_name, output_file_name) -> None:
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name
        self.lines = None
        self.rows = list()
        self.solver = linear_equations_system_solver.LinearEquationsSystemSolver()
        self.results = list()

    def read_file(self):
        file = open(self.input_file_name, 'r')
        self.lines = file.readlines()
        file.close()

    def split_lines(self):
        for line in self.lines:
            self.rows.append(line.split())

    def solve(self):
        for i in range(0, len(self.rows), 3):
            array = numpy.array([self.rows[i], self.rows[i+1], self.rows[i+2]], numpy.float64)
            result = self.solver.solve_system(array)
            self.results.append(str(result))

    def save_results(self):
        file = open(self.output_file_name, 'w')
        file.write(str(self.results))
        file.close()


if __name__ == "__main__":

    input_file_name = input('Input file name: ')
    output_file_name = input('Output file name: ')
    
    app = App(input_file_name, output_file_name)
    app.read_file()
    app.split_lines()
    app.solve()
    app.save_results()
    