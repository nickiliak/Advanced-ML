# Week 6 — Answers

Topic: Manifold metrics, geodesic ODE, energy minimization.
Source questions: [Week6/exercise.md](../exercise.md)

## Theoretical Exercises

## Question 6.1: Quadratic metric — local norms and angles

Manifold $\mathbb{R}^2$ with $G_x = (1 + \|x\|^2)\,I$. Points $x_1=(1,1)^\top$, $x_2=(2,3)^\top$, $x_3=(0,3)^\top$.

1. Compute local norms of $v_1 = (1,0)^\top$ at $x_1$, $x_2$, $x_3$.
2. Compute local angles between $v_1$ and $v_2 = (0,1)^\top$ at the same three points.

**Answer:**

**Part 1 — Local norms of $v_1 = (1,0)^\top$.**

General Riemannian norm: $\|v\|_{G_x} = \sqrt{v^\top G_x v}$. With $G_x = (1+\|x\|^2)\,I$, the scalar pulls out:

$$\|v\|_{G_x}^2 = (1+\|x\|^2)\,\|v\|_2^2$$

For $v_1$ with $\|v_1\|_2 = 1$, this collapses to:

$$\|v_1\|_{G_x} = \sqrt{1 + \|x\|^2} = \sqrt{1 + x_1^2 + x_2^2}$$

Evaluations:
- At $x_1=(1,1)^\top$: $\sqrt{1+2} = \sqrt{3}$
- At $x_2=(2,3)^\top$: $\sqrt{1+13} = \sqrt{14}$
- At $x_3=(0,3)^\top$: $\sqrt{1+9} = \sqrt{10}$

**Part 2 — Local angles between $v_1=(1,0)^\top$ and $v_2=(0,1)^\top$.**

$$\cos\theta = \frac{\langle v_1, v_2\rangle_{G_x}}{\|v_1\|_{G_x}\,\|v_2\|_{G_x}}$$

Numerator: $\langle v_1, v_2\rangle_{G_x} = v_1^\top G_x v_2 = (1+\|x\|^2)\,(v_1^\top v_2) = (1+\|x\|^2)\cdot 0 = 0$.

Therefore $\cos\theta = 0$, giving $\theta = \pi/2$ at **all three points** $x_1, x_2, x_3$.

The angle is independent of the base point because the metric is conformal (scalar $\times\,I$) — conformal metrics preserve Euclidean angles. Lengths scale by $\sqrt{s(x)}$ but angles are unchanged.


## Question 6.2: Euclidean metric — geodesic ODE

Euclidean metric $G = I$ on $\mathbb{R}^d$.

1. Derive geodesic-ODE coefficients (Eq. 7.20 LMLG).
2. Derive the geodesic ODE.
3. Geodesic connecting $x_1$ and $x_2$?

**Answer:**

**Part 1 — Coefficients $\Gamma^{m}_{jk}$ for $G = I$.**

The identity matrix has constant entries (1s on diagonal, 0s off-diagonal), none of which depend on $c$. Therefore every partial derivative vanishes:

$$\frac{\partial [\mathbf{G}_{c_t}]_{ij}}{\partial [c_t]_k} = 0 \quad \forall i,j,k.$$

Plugging into Eq. 7.20, the parenthesized term is $0$, so

$$\Gamma^{m}_{jk}(c_t) = 0 \quad \forall m,j,k.$$

**Part 2 — Geodesic ODE.**

Substituting $\Gamma^{m}_{jk} = 0$ into Eq. 7.19:

$$[\ddot c_t]_m = -\sum_{j,k} 0 \cdot [\dot c_t]_j [\dot c_t]_k = 0 \quad \forall m$$

Therefore $\ddot c = 0$.

**Part 3 — Geodesic connecting $x_1$ and $x_2$.**

Solve $\ddot c = 0$ by integrating twice:

$$\dot c(t) = C, \qquad c(t) = C\,t + B$$

with constants $B, C \in \mathbb{R}^d$. Apply boundary conditions $c(0) = x_1$ and $c(1) = x_2$ (BVP form, parametrized over $t \in [0,1]$):

- $c(0) = B = x_1 \;\Rightarrow\; B = x_1$
- $c(1) = C + B = x_2 \;\Rightarrow\; C = x_2 - x_1$

Final geodesic:

$$c(t) = x_1 + t\,(x_2 - x_1), \quad t \in [0,1]$$

i.e. the straight line from $x_1$ to $x_2$, as expected for flat (Euclidean) space.


## Question 6.3: Quadratic metric — geodesic ODE

Same metric as 6.1.

1. Derive geodesic-ODE coefficients (Eq. 7.20 LMLG).
2. Derive the geodesic ODE.
3. Geodesic $c$ with $c(0) = 0$, $\dot c(0) = v$. Acceleration $\ddot c(0)$?

**Answer:**

**Part 1 — Christoffel coefficients $\Gamma^m_{jk}$.**

Setup. With $G_{ij} = s(c)\,\delta_{ij}$, $s(c) = 1 + \|c\|^2$:

- $[G^{-1}]_{mi} = (1/s)\,\delta_{mi}$  (diagonal inverse)
- $\partial G_{ab}/\partial c_c = 2 c_c\,\delta_{ab}$  (only diagonal entries depend on $c$, and they depend via $\|c\|^2$)

Plug into Eq. 7.20:

$$\Gamma^m_{jk} = \frac{1}{2}\sum_i [G^{-1}]_{mi}\Big(2\,\partial_k G_{ij} - \partial_i G_{jk}\Big)$$

Collapse $\sum_i$ via $\delta_{mi}$ (replace $i \to m$):

$$\Gamma^m_{jk} = \frac{1}{2s}\Big(2\,\partial_k G_{mj} - \partial_m G_{jk}\Big) = \frac{1}{2s}\Big(2 \cdot 2 c_k \delta_{mj} - 2 c_m \delta_{jk}\Big)$$

Simplify (pull out factor of 2):

$$\boxed{\;\Gamma^m_{jk} = \frac{1}{s(c)}\Big(2\,c_k\,\delta_{mj} - c_m\,\delta_{jk}\Big), \qquad s(c) = 1 + \|c\|^2\;}$$

(Verifying the question's hint: $\Gamma^m_{jk} = 0$ whenever $m \ne j$ AND $j \ne k$ — both deltas vanish.)

**Part 2 — Geodesic ODE.**

Plug $\Gamma^m_{jk}$ into Eq. 7.19:

$$[\ddot c]_m = -\sum_{j,k}\Gamma^m_{jk}\,\dot c_j\,\dot c_k = -\frac{1}{s}\sum_{j,k}\big(2 c_k \delta_{mj} - c_m \delta_{jk}\big)\,\dot c_j\,\dot c_k$$

Split into two sums and collapse each delta:

- **Term 1**: $\sum_{j,k} 2 c_k \delta_{mj} \dot c_j \dot c_k = 2 \big(\sum_j \delta_{mj}\dot c_j\big)\big(\sum_k c_k \dot c_k\big) = 2\,\dot c_m\,\langle c, \dot c\rangle$
- **Term 2**: $\sum_{j,k} c_m \delta_{jk} \dot c_j \dot c_k = c_m \sum_j \dot c_j^2 = c_m\,\|\dot c\|^2$

Component form:

$$[\ddot c]_m = -\frac{1}{s(c)}\Big(2\,\dot c_m\,\langle c, \dot c\rangle - c_m\,\|\dot c\|^2\Big)$$

Vectorize (drop $[\cdot]_m$, replace $\dot c_m \to \dot c$, $c_m \to c$; scalars $\langle c, \dot c\rangle, \|\dot c\|^2$ pull out):

$$\boxed{\;\ddot c \;=\; \frac{1}{s(c)}\Big(\|\dot c\|^2\,c \;-\; 2\,\langle c, \dot c\rangle\,\dot c\Big), \qquad s(c) = 1 + \|c\|^2\;}$$

**Part 3 — Acceleration at $t = 0$.**

Initial conditions (from the question): $c(0) = 0$, $\dot c(0) = v$. Evaluate each piece at $t = 0$:

- $s(c(0)) = 1 + \|0\|^2 = 1$
- $\|\dot c(0)\|^2 = \|v\|^2$
- $\langle c(0), \dot c(0)\rangle = \langle 0, v\rangle = 0$
- $c(0) = 0$, $\dot c(0) = v$

Plug in:

$$\ddot c(0) = \frac{1}{1}\Big(\|v\|^2 \cdot 0 \;-\; 2 \cdot 0 \cdot v\Big) = 0$$

So $\ddot c(0) = 0$ (zero vector). The geodesic starts with zero acceleration at the origin — geometrically, the conformal factor $s(c) = 1 + \|c\|^2$ is at its minimum at $c = 0$ with vanishing first-order variation ($\partial s/\partial c_k|_{c=0} = 2c_k|_{c=0} = 0$), so the manifold "looks flat" there to first order and does not bend the geodesic at the origin.


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
