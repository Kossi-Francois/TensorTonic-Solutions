def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    """
    Returns the final scalar x after the requested iterations.
    """
    # Write code here
    # optimization: vanilla grad desc
    # min_x f(x)

    # xt+1 = xt - n. f'(xt)
    
    # for quradatic fun: f(x) = ax^2 + bx + c
    # f'(x) = 2ax + b
    # for a > 0: its parabola: convex: with mini closed form | f'(xmin)= 0: xmin = - b/(2a)
    def f_prime(x): return 2 * a * x + b;
    x1 = x0
    for step in range(steps):
        x1 = x0 - lr * f_prime(x0)
        x0 = x1
    return x1