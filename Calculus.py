from sympy import *
from sympy.abc import x,y

def get_partial_diff():
    # x = symbols('x')
    # y = symbols('y')
    f = Function('f')(x,y)
    f = x**2+3*y
    fx = diff(x)
    fy = diff(y)
    print(f)
    print(fx)
    print(fy)
get_partial_diff()