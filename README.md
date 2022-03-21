Code for solving linear equations: https://www.geeksforgeeks.org/gaussian-elimination/.

To create the distribution version, I used the wheel package and the command: 

```
python setup.py sdist bdist_wheel
```

Copy the dist folder to the project with the application and use the following command to install the package:

```
pip install /dist/linear_equations_system_solver_package-1.0-cp38-cp38-linux_x86_64.whl 
```

PyInstaller installation:

```
pip install pyinstaller
```

To create the executable file use:

```
pyinstaller app.py
```

In order for the program to run correctly, copy the file containing the compiled C++ code to the folder with the executable file (dist/app).