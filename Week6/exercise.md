# Week 6 Exercises — Manifold Metrics & Geodesics

Source: `02460_week6_exercises.pdf` (Advanced Machine Learning 02460, March 2026, v1.0)

## Theoretical Exercises

### Exercise 6.1 (Quadratic metric)

Consider a two-dimensional abstract manifold with the metric

$$G_x = (1 + \|x\|^2)\,I, \quad x \in \mathbb{R}^2.$$

Consider the points

$$x_1 = \begin{pmatrix}1\\1\end{pmatrix},\quad x_2 = \begin{pmatrix}2\\3\end{pmatrix},\quad x_3 = \begin{pmatrix}0\\3\end{pmatrix}.$$

1. Compute the local norms of the tangent vector $v_1 = (1,\,0)^\top$ assuming the point of tangency is $x_1$, $x_2$, and $x_3$, respectively.
2. Compute the local angles between $v_1$ and $v_2 = (0,\,1)^\top$ in the same three points of tangency.

### Exercise 6.2 (Euclidean metric)

Consider the Euclidean metric of $\mathbb{R}^d$, i.e. $G = I$.

1. Derive the coefficients of the geodesics ode of this metric (Eq. 7.20 in the LMLG book).
2. Derive the geodesic ode.
3. What is the geodesic that connects points $x_1$ and $x_2$?

**Reference (LMLG, Hauberg p.64) — used in 6.2 and 6.3:**

Eq. 7.19 — Geodesic ODE:

$$[\ddot c_t]_m = -\sum_{j=1}^{d}\sum_{k=1}^{d} \Gamma^{m}_{jk}(c_t)\,[\dot c_t]_j\,[\dot c_t]_k$$

Eq. 7.20 — Christoffel coefficients:

$$\Gamma^{m}_{jk}(c_t) = \frac{1}{2}\sum_{i=1}^{d} [\mathbf{G}_{c_t}^{-1}]_{mi}\left(2\,\frac{\partial [\mathbf{G}_{c_t}]_{ij}}{\partial [c_t]_k} - \frac{\partial [\mathbf{G}_{c_t}]_{jk}}{\partial [c_t]_i}\right)$$

where $[\cdot]_i$ indexes the $i$-th vector component and $[\cdot]_{ij}$ the $(i,j)$ matrix entry.

### Exercise 6.3 (Quadratic metric)

Consider a two-dimensional abstract manifold with the metric

$$G_x = (1 + \|x\|^2)\,I, \quad x \in \mathbb{R}^2.$$

1. Derive the coefficients of the geodesics ode of this metric (Eq. 7.20 in the LMLG book). *Hint: note that some terms of the metric are zero, which renders some coefficients to be zero as well.*
2. Derive the geodesic ode.
3. Consider a geodesic $c$ starting at $c(0) = 0$ and initial velocity $\dot c(0) = v$. What is the acceleration $\ddot c(0)$?

## Programming Exercises

### Exercise 6.4 (Curve parametrizations)

Consider a two-dimensional abstract manifold with the metric

$$G_x = (1 + \|x\|^2)\,I, \quad x \in \mathbb{R}^2.$$

1. Implement direct energy minimization for computing geodesics using piecewise straight lines to parameterize the solution curve.
2. Extend the previous implementation to also support third-order polynomials to parametrize the solution curve.

### Exercise 6.5 (Density metrics)

Consider the dataset available at <https://www2.compute.dtu.dk/~sohau/weekendwithbernie/toybanana.npy>. This consists of $N = 992$ observations in $\mathbb{R}^2$. Consider the metric over $\mathbb{R}^2$ defined as

$$G_x = \frac{1}{p(x) + \epsilon}, \qquad p(x) = \frac{1}{N}\sum_{n=1}^{N} \mathcal{N}(x \mid x_n, \sigma^2 I),$$

where $\sigma = 0.1$ and $\epsilon = 10^{-4}$ avoids dividing by zero.

1. Implement direct energy minimization for computing geodesics using piecewise straight lines to parameterize the solution curve.
2. Extend the previous implementation to also support third-order polynomials to parametrize the solution curve.
