"""Solve Ordinary Differential Equations.

    This module provides a method to find the solution to ODEs.

    The module contains the following funtions:

    - `euler(f, x0, ti, tf, stps)` - Returns the solution of ODEs using Euler`s Method.
"""

def euler(f, x0, ti, tf, stps):
    """Returns the solution of an ODE of the form x` = f(x, t) for an interval 't' using Euler`s Method.

    Examples:
        >>> euler(func, -1, 0, 1, 10)  # 'func' being exp(-t) returned by another function.
        array([-1.        , -0.9       , -0.81051607, -0.73044233, -0.6587892 , -0.59467116, -0.53729582, -0.4859541 , -0.44001152, -0.39890029])
        
    Args:
        f: Function f(x, t) to be solved.
        x0 (float): Initial condition.
        ti (float): Initial value of the interval t.
        tf (float): Final value of the interval t.
        stps (int): Steps to take along the interval.

    Returns:
        tuple: A tuple containing the aproximate value of 'x' for every 't'.
    """

    h = (tf - ti) / stps
    t = np.linspace(ti, tf, num=stps)
    x = np.zeros(t.size)
    x[0] = x0
    for i in range(0, t.size - 1):
        x[i + 1] = x[i] + h*f(x[i], t[i])
    return x

