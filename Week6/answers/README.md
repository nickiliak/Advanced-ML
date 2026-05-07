# Week 6 — Answers

Topic: Manifold metrics, geodesic ODE, energy minimization.
Source questions: [Week6/exercise.md](../exercise.md)

## Theoretical Exercises

## Question 6.1: Quadratic metric — local norms and angles

Manifold $\mathbb{R}^2$ with $G_x = (1 + \|x\|^2)\,I$. Points $x_1=(1,1)^\top$, $x_2=(2,3)^\top$, $x_3=(0,3)^\top$.

1. Compute local norms of $v_1 = (1,0)^\top$ at $x_1$, $x_2$, $x_3$.
2. Compute local angles between $v_1$ and $v_2 = (0,1)^\top$ at the same three points.

**Answer:**

<!-- Add your answer here -->


## Question 6.2: Euclidean metric — geodesic ODE

Euclidean metric $G = I$ on $\mathbb{R}^d$.

1. Derive geodesic-ODE coefficients (Eq. 7.20 LMLG).
2. Derive the geodesic ODE.
3. Geodesic connecting $x_1$ and $x_2$?

**Answer:**

<!-- Add your answer here -->


## Question 6.3: Quadratic metric — geodesic ODE

Same metric as 6.1.

1. Derive geodesic-ODE coefficients (Eq. 7.20 LMLG).
2. Derive the geodesic ODE.
3. Geodesic $c$ with $c(0) = 0$, $\dot c(0) = v$. Acceleration $\ddot c(0)$?

**Answer:**

<!-- Add your answer here -->


## Programming Exercises

## Question 6.4: Curve parametrizations — quadratic metric

Same metric as 6.1.

1. Implement direct energy minimization with piecewise-straight-line parametrization.
2. Extend to third-order polynomial parametrization.

**Answer:**

<!-- Add your answer here -->


## Question 6.5: Density metrics — banana dataset

Dataset `toybanana.npy` ($N = 992$, $\mathbb{R}^2$). Metric $G_x = 1/(p(x) + \epsilon)$, $p(x) = \tfrac{1}{N}\sum_n \mathcal{N}(x \mid x_n, \sigma^2 I)$, $\sigma = 0.1$, $\epsilon = 10^{-4}$.

1. Implement direct energy minimization with piecewise-straight-line parametrization.
2. Extend to third-order polynomial parametrization.

**Answer:**

<!-- Add your answer here -->
