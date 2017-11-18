import numpy as np
import matplotlib.pyplot as plt


def power_iteration(A, tolerance = 0.001):
    '''
    The power_iteration function is used to solve for the largest eigenvalue of a matrix using the power iteration method.

    Args: A - represent a square matrix that is used to caculated the largest eigenvalue
          tolerance - use to compared with the infinity norm of the residual

    Return: The function return a tuple with three objects:
            i. The final estimate of the largest eigenvalue, k
           ii. The final estimate of the corresponding eigenvector, x
          iii. The number of iterations that it took to reach convergence
    '''
    counter = 0
    x = np.ones((5,1))                      #initial setup of vector x
    residual = tolerance + 0.1              #set residual greater than tolerance so that the while loop could start
    while residual > tolerance:
        counter += 1
        y = np.dot(A, x)
        k = np.linalg.norm(y)
        x = y/k
        residual = np.linalg.norm(np.dot(A, x) - k * x)
    return (k, x, counter)

if __name__ == '__main__':
    np.random.seed(1)
    A = np.random.rand(5, 5)
    num_iter = []
    toler = np.array([10**x for x in range(-8, -2)])
    for i in toler:
        num_iter.append(power_iteration(A, i)[2])
    plt.semilogx(toler, num_iter)
    plt.xlabel('power iteration')
    plt.ylabel('number of iteration')
    plt.title('iterations')
    plt.savefig('iterations')
    print(power_iteration.__doc__)
