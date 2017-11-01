# MPCS 51042-2, Python Programming

**Week 8 Assignment**

**Due**: November 19 at 11:59pm CT

## Problem 1: Power Iteration

[Linear algebra](https://en.wikipedia.org/wiki/Linear_algebra) is central to many disciplines in the sciences, including mathematics, engineering, physics, and computer science. At the heart of linear algebra is the solution of [systems of linear equations](https://en.wikipedia.org/wiki/System_of_linear_equations), such as:

<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/d691839a2b284331b58b0820654d32e101e26a03" />

Usually, such systems of equations are cast in matrix form:

<img src="http://latex2png.com/output//latex_32ccf6bfaaa319fbc2ee96110136e276.png" width="200" />

Understanding the properties of the matrices represented such systems is one primary goal of linear algebra. For this problem, you are asked to write an algorithm to solve for the largest [eigenvalue](https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors) of a matrix using the [power iteration](https://en.wikipedia.org/wiki/Power_iteration) method.

Your algorithm should implement the following steps to find the largest eigenvalue of a matrix, A:

1. The algorithm begins with a "guess" of the eigenvector. Your guess should be a column vector of ones. Let's refer to this vector as x.
2. Calculate the matrix multiplication of the A and x and store it in a new vector y. This can be done with the [numpy.dot](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.dot.html) function, the [numpy.matmul](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.matmul.html) function, or the `@` operator.
3. Calculate the [infinity norm](http://mathworld.wolfram.com/L-Infinity-Norm.html) of the y vector, either using regular numpy functions or [numpy.linalg.norm](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.linalg.norm.html). This is an estimate of the largest eigenvalue which we'll call k.
4.  Calculate a new estimate of the eigenvector, x, by dividing each element in y by k.
5.  Calculate the infinity norm of the residual, <img src="http://latex2png.com/output//latex_ccac517afce41ee8e0632cf9594e4020.png" width="60">.
6.  If the infinity norm of the residual is less than some specified tolerance, return the current value of k and x.
7.  Otherwise, repeat from step 2.

### Specifications: `power_iteration`

- Your program should define a function `power_iteration(A, tolerance)` that solves for the largest eigenvalue of a matrix using the power iteration method as described above.
- `A` is a square matrix that is passed in an `tolerance` is the tolerance used in step 6 of the algorithm.
- The function should return a tuple with three objects:
  1. The final estimate of the largest eigenvalue, k.
  2. The final estimate of the corresponding eigenvector, x.
  3. The number of iterations that it took to reach convergence.

### Specifications: `main`

- Write a function called `main` that solves for the largest eigenvalue of a 5x5 matrix of random numbers using the `power_iteration` function. You can create this matrix with the following code (we set the random number "seed" to ensure that the same matrix is always created): 
    ```python
    import numpy as np

    np.random.seed(1)
    A = np.random.rand(5, 5)
    ```
- Vary the tolerance passed to `power_iteration` to see how the number of iterations changes as the tolerance becomes smaller. Use the values 10<sup>-3</sup>, 10<sup>-4</sup>, 10<sup>-5</sup>, 10<sup>-6</sup>, 10<sup>-7</sup>, and 10<sup>-8</sup>.
- Using matplotlib, make a plot of the number of iterations (y-axis) versus the tolerance used in `power_iteration` (x-axis). Since the tolerance varies over multiple orders of magnitude, use [plt.semilogx](https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.semilogx) instead of plt.plot. Make sure your axes are labeled and save the plot as a PNG file with the name "iterations.png".