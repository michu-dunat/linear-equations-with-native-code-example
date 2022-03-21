from setuptools import setup, Extension

setup(
    ext_modules=[Extension('gaussianElimination', ['linear_lib/linear_solver.cpp'],),],
    name='linear-equations-system-solver-package',
    version='1.0',
    packages=['linear_lib'],
    license='MIT',
    description='Python package for solving systems of three linear equations',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='',
    author='Michał Dunat',
    author_email='kontaktmichaldunat@gmail.com'
)
