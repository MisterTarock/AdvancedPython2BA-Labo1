# coding=utf-8
# Math library
# Author: Sébastien Combéfis
# Version: February 2, 2016

from math import *

def fact(n):
    """Computes the factorial of a natural number.
    
    Pre: -
    Post: Returns the factorial of 'n'.
    Throws: ValueError if n < 0
    """
    if n < 0: raise ValueError('Err')

    result = 1
    for i in range(1, n+1):
        result *= i

    return result

def roots(a, b, c):
    """Computes the roots of the ax^2 + bx + x = 0 polynomial.
    
    Pre: -
    Post: Returns a tuple with zero, one or two elements corresponding
          to the roots of the ax^2 + bx + c polynomial.
    """
    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        return ()
    elif discriminant == 0:
        return ( (-b + sqrt(discriminant)) / (2 * a) )
    else:
        return ( (-b + sqrt(discriminant)) / (2 * a), (-b - math.sqrt(discriminant)) / (2 * a) )



def integrate(function, lower, upper):
    """Approximates the integral of a fonction between two bounds
    
    Pre: 'function' is a valid Python expression with x as a variable,
         'lower' <= 'upper',
         'function' continuous and integrable between 'lower‘ and 'upper'.
    Post: Returns an approximation of the integral from 'lower' to 'upper'
          of the specified 'function'.
    """

    steps = 100
    h = (upper - lower) / steps
    x = lower

    integral = 0

    for i in range(steps + 1):
        if i == 0 or i == steps:
            integral += eval(function, {}, {'x': x})
        elif i % 2 == 0:
            integral += 2 * eval(function, {}, {'x': x})
        else:
            integral += 4 * eval(function, {}, {'x': x})

        x += h

    integral *= h/3

    return integral

if __name__ == '__main__':
    print(fact(5))
    print(roots(1, 0, 1))
    print(integrate('x ** 2 - 1', -1, 1))