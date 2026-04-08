import numpy as np

def generate_data(n:int=30, noise_std:float=0.2, seed:int = 42):
    np.random.seed(seed)
    x = np.linspace(-1, 1, n).reshape(-1, 1)
    y_true = np.sin(2 * np.pi * x)
    t = y_true + noise_std * np.random.randn(*x.shape)
    return x, t, y_true


def polynomial_basis(x, degree):
    return np.concatenate([x**i for i in range(degree + 1)], axis=1)


def solve_ls(Phi, t):
    return np.linalg.inv(Phi.T @ Phi) @ Phi.T @ t


def predict(Phi, w):
    return Phi @ w