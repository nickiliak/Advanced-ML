# Week 5 Exercises — Manifold Learning & Latent Geometry

Source: `02460_week5_exercises.pdf` (Advanced Machine Learning 02460, March 2026, v1.0)

## Theoretical Exercises

### Exercise 5.1 (PPCA — rotational equivalence)

Probabilistic PCA can be equivalently expressed as

$$p(y \mid x) = \mathcal{N}(y \mid Ax + b,\,\sigma^2 I) \quad \text{or} \quad p(y \mid \hat x) = \mathcal{N}(y \mid \hat A \hat x + b,\,\sigma^2 I),$$

with latent variables $\hat x = R x$ and $\hat A = A R^\top$, where $R$ is a rotation matrix. The two latent representations $x$ and $\hat x$ are clearly different (for $R \ne I$). Show that

1. Euclidean distances between points are identical in the two representations: $\|x_i - x_j\| = \|\hat x_i - \hat x_j\|$.
2. Angles between points are identical: $\angle(x_i - x_j,\,x_k - x_j) = \angle(\hat x_i - \hat x_j,\,\hat x_k - \hat x_j)$.

### Exercise 5.2 (Generative model — manifold properties)

Consider $y = f(x)$ with $x = (x_1, x_2) \in \mathbb{R}^2$, $y = (y_1, y_2, y_3) \in \mathbb{R}^3$, and

$$f(x) = \begin{pmatrix} 2x_1^2 + x_2^2 \\ x_1 \\ x_2 \end{pmatrix}.$$

1. Derive the Jacobian matrix of $f$.
2. Show that the generative model spans an *immersed* manifold.
3. Show that the generative model spans an *embedded* manifold.

### Exercise 5.3 (Curve speed and arc length)

Consider the curve $c : [0, 1] \to \mathbb{R}^2$ defined as

$$c(t) = \begin{pmatrix} 2t + 1 \\ -t^2 \end{pmatrix}.$$

1. Derive an expression for the speed function $t \mapsto \|\dot c_t\|$.
2. Compute the Euclidean length of the curve.

*Hint:* $\int \sqrt{1 + t^2}\,dt = \tfrac{1}{2}(\sqrt{1 + t^2}\,t + \sinh^{-1}(t)) + C$.

### Exercise 5.4 (Sphere — pullback metric, positive definiteness)

Let $x_1 \in (0, \pi)$ and $x_2 \in [0, 2\pi)$ be the latent coordinates of the manifold spanned by

$$f(x_1, x_2) = \begin{pmatrix} \sin(x_1)\cos(x_2) \\ \sin(x_1)\sin(x_2) \\ \cos(x_1) \end{pmatrix},$$

which spans the unit sphere.

1. Derive the Jacobian matrix of $f$.
2. Derive the metric associated with $f$ via Eq. 5.21 in the LMLG book.
3. Show that the metric is positive definite.

*Hint:* recall $\cos^2(x) + \sin^2(x) = 1$.

> **LMLG Eq. 5.21 (context).** Angle between curves on the manifold via the pullback inner product:
>
> $$\theta = \cos^{-1}\!\left( \frac{v_1^\top J_x^\top J_x\, v_2}{\|J_x v_1\| \cdot \|J_x v_2\|} \right).$$
>
> The pullback inner product on the latent space is $\langle v_1, v_2 \rangle_x = v_1^\top J_x^\top J_x\, v_2$. So the **pullback metric tensor** at $x$ is the $n \times n$ symmetric matrix
> $$M(x) = J_f(x)^\top J_f(x).$$
> This is the matrix to derive in part 2.

## Programming Exercises

### Exercise 5.5 (Curve Length — numerical and analytic)

Consider the curve $c : [0, 1] \to \mathbb{R}^2$ defined in Eq. 17 above.

1. Write a computer program that evaluates the length of $c$ using Eq. 4.2 in the LMLG book.
2. If you have completed exercise 5.3:
   - (a) Did the numerical and analytical results agree?
   - (b) Use the analytic expression for $\|\dot c_t\|$ to write a program that evaluates the length using Eq. 4.5 in the LMLG book (approximate the integral with a sum).

### Exercise 5.6 (VAE latent curve length)

Consider the Bernoulli VAE from Week 1. Train it with a two-dimensional latent space (for ease of plotting).

1. Write a program that evaluates the length of any latent second-order polynomial curve $c$ using Eq. 4.2 in the LMLG book. It is recommended to support any callable curve $c$.
2. Evaluate how the VAE decoder transforms latent-space curves into output (pixel) space.
