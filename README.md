# Secant Method for Finding Roots

This Python script implements the Secant Method for finding the roots of a given function. The Secant Method is an iterative numerical technique used to find the root of a function, i.e., the point where the function evaluates to zero.

## Description

The Secant Method requires two initial approximations for the root, and it iteratively refines these approximations using the formula:

\[ x_{n+1} = x_n - f(x_n) \cdot \frac{x_n - x_{n-1}}{f(x_n) - f(x_{n-1})} \]

The iterations continue until the difference between successive approximations is less than a specified tolerance (`tol`) or a maximum number of iterations (`max_iter`) is reached.

## Parameters

- `f`: The function whose root we want to find.
- `x0`: The first initial approximation.
- `x1`: The second initial approximation.
- `tol`: The acceptable error tolerance (default is `1e-5`).
- `max_iter`: The maximum number of iterations (default is `100`).

## Returns

- The approximate root of the function if found within the specified tolerance and iteration limit.
- `None` if the root is not found or if a division by zero occurs during the iterations.

## Usage

To use the `secant_method` function, define the function `f` whose root you want to find and call `secant_method` with appropriate initial approximations:

```python
def secant_method(f, x0, x1, tol=1e-5, max_iter=100):
    """
    Implementation of the Secant Method for finding roots of a function.

    :param f: The function whose root we want to find.
    :param x0: The first initial approximation.
    :param x1: The second initial approximation.
    :param tol: The acceptable error tolerance.
    :param max_iter: The maximum number of iterations.
    :return: The approximate root.
    """
    for i in range(max_iter):
        if f(x1) - f(x0) == 0:
            print("Division by zero, stopping execution.")
            return None

        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        
        if abs(x2 - x1) < tol:
            print(f"Root found after {i+1} iterations: x = {x2}")
            return x2

        x0, x1 = x1, x2
    
    print(f"Root not found after {max_iter} iterations.")
    return None

# Example usage
def f(x):
    return x**2 - 4

root = secant_method(f, 1, 2)
print("Approximate root:", root)
