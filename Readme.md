A simple and naive battery modelisation + Kalman filter for state of charge (SoC) estimation

# Python implementation
The "Python" folder contain a python3 implementation of an extended Kalman filter for state of charge (SoC) estimation of a simulated lithium battery. The model used for the battery is a simple Thevenin model.


To run it just launch:
```sh
$> python3 Python/main.py
```

A CC/CV charge and a pulse discharge will be simulated. Then a graph will be displayed showing simulation results. You can play around with the capacity and Thevenin model values in Python/main.py. The charge/discharge protocol can also be changed, values are found in Python/protocol.py.

## Dependencies:
    - python3
    - numpy
    - matplotlib
