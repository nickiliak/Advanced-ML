# Week 5 - Manifold Learning & Latent Geometry

Source questions: [Week5/exercise.md](../exercise.md)

## Theoretical Exercises

## Question 5.1: PPCA — rotational equivalence preserves distances and angles

For $\hat x = R x$, $\hat A = A R^\top$ with $R$ a rotation matrix:

1. Show $\|x_i - x_j\| = \|\hat x_i - \hat x_j\|$.
2. Show $\angle(x_i - x_j,\, x_k - x_j) = \angle(\hat x_i - \hat x_j,\, \hat x_k - \hat x_j)$.

**Answer:**

Rotation matrix property: $R^\top R = I$. Norm-squared identity for column vectors: $\|v\|^2 = v^\top v$.

**Part 1 — distances.** With $\hat x_i = R x_i$:

$$
\|\hat x_i - \hat x_j\|^2
= (\hat x_i - \hat x_j)^\top (\hat x_i - \hat x_j)
= \big(R(x_i - x_j)\big)^\top \big(R(x_i - x_j)\big)
= (x_i - x_j)^\top R^\top R\, (x_i - x_j)
= (x_i - x_j)^\top (x_i - x_j)
= \|x_i - x_j\|^2.
$$

Taking the (non-negative) square root: $\|\hat x_i - \hat x_j\| = \|x_i - x_j\|$. $\square$

**Part 2 — angles.** Let $u = x_i - x_j$, $w = x_k - x_j$; then $\hat u = R u$, $\hat w = R w$. Angle definition:

$$
\cos \theta = \frac{u \cdot w}{\|u\|\,\|w\|}.
$$

Numerator under rotation:

$$
\hat u \cdot \hat w = (Ru)^\top (Rw) = u^\top R^\top R\, w = u^\top w = u \cdot w.
$$

Denominator under rotation: $\|\hat u\|\,\|\hat w\| = \|u\|\,\|w\|$ by Part 1. Therefore

$$
\cos \hat\theta = \frac{\hat u \cdot \hat w}{\|\hat u\|\,\|\hat w\|} = \frac{u \cdot w}{\|u\|\,\|w\|} = \cos \theta,
$$

so $\angle(\hat x_i - \hat x_j,\, \hat x_k - \hat x_j) = \angle(x_i - x_j,\, x_k - x_j)$. $\square$


## Question 5.2: Generative model — Jacobian and manifold properties

For $f(x_1, x_2) = (2x_1^2 + x_2^2,\, x_1,\, x_2)^\top$:

1. Derive the Jacobian.
2. Show the model spans an *immersed* manifold.
3. Show the model spans an *embedded* manifold.

**Answer:**

**Part 1 — Jacobian.** $f: \mathbb{R}^2 \to \mathbb{R}^3$, so $J_f$ has shape $3 \times 2$ (rows = outputs, cols = inputs), with entry $(i,j) = \partial f_i / \partial x_j$:

$$
J_f(x_1, x_2) =
\begin{bmatrix}
4 x_1 & 2 x_2 \\
1 & 0 \\
0 & 1
\end{bmatrix}.
$$

**Part 2 — immersed manifold.** $f$ is an immersion iff $J_f$ has full rank $= n = 2$ at every point of the domain. The bottom $2 \times 2$ sub-matrix of $J_f$ is the identity $I_2$, with $\det I_2 = 1 \neq 0$ for every $(x_1, x_2) \in \mathbb{R}^2$. Hence $\operatorname{rank} J_f = 2$ everywhere, the two columns are linearly independent everywhere, and $f$ is an immersion. Its image is therefore an **immersed manifold** in $\mathbb{R}^3$.

**Part 3 — embedded manifold.** Need: immersion (done) + injective + homeomorphism onto image (i.e. $f^{-1}$ continuous on the image).

*Injectivity.* Suppose $f(x) = f(y)$, i.e. $(2x_1^2 + x_2^2,\, x_1,\, x_2) = (2y_1^2 + y_2^2,\, y_1,\, y_2)$. Components 2 and 3 give $x_1 = y_1$ and $x_2 = y_2$ directly, so $x = y$. Hence $f$ is injective.

*Continuity of $f^{-1}$.* From components 2 and 3 of the defining equation, $x_1 = y_2$ and $x_2 = y_3$, so

$$
f^{-1}(y_1, y_2, y_3) = (y_2, y_3),
$$

which is the coordinate projection $\pi: \mathbb{R}^3 \to \mathbb{R}^2$ that drops $y_1$. Every linear map between finite-dimensional normed spaces is continuous; in particular $\pi$ is continuous. Hence $f^{-1}$ is continuous on the image.

*Conclusion.* $f$ is a smooth (hence continuous) injective immersion with continuous inverse on its image — a homeomorphism onto its image. Therefore $f$ is an **embedding**, and its image is an **embedded manifold** in $\mathbb{R}^3$. $\square$


## Question 5.3: Curve $c(t) = (2t + 1,\, -t^2)^\top$ — speed and length

1. Derive $t \mapsto \|\dot c_t\|$.
2. Compute the Euclidean length of the curve. *Hint:* $\int \sqrt{1+t^2}\,dt = \tfrac{1}{2}(\sqrt{1+t^2}\,t + \sinh^{-1}(t)) + C$.

**Answer:**

**Part 1 — speed.** Differentiate component-wise:

$$
\dot c(t) = \frac{d}{dt}\begin{pmatrix} 2t + 1 \\ -t^2 \end{pmatrix} = \begin{pmatrix} 2 \\ -2t \end{pmatrix}.
$$

Take the Euclidean norm:

$$
\|\dot c_t\| = \sqrt{2^2 + (-2t)^2} = \sqrt{4 + 4 t^2} = 2\sqrt{1 + t^2}.
$$

**Part 2 — length.** Arc length formula on $[0, 1]$:

$$
L = \int_0^1 \|\dot c_t\|\, dt = \int_0^1 2\sqrt{1 + t^2}\, dt = 2 \int_0^1 \sqrt{1 + t^2}\, dt.
$$

Apply the hint $\int \sqrt{1+t^2}\,dt = \tfrac{1}{2}\bigl(\sqrt{1+t^2}\,t + \sinh^{-1}(t)\bigr) + C$. The factor $2$ outside cancels the $\tfrac{1}{2}$ from the antiderivative:

$$
L = \Bigl[\sqrt{1 + t^2}\,t + \sinh^{-1}(t)\Bigr]_0^1
= \bigl(\sqrt{2} \cdot 1 + \sinh^{-1}(1)\bigr) - \bigl(\sqrt{1} \cdot 0 + \sinh^{-1}(0)\bigr)
= \sqrt{2} + \sinh^{-1}(1).
$$

Numerically, $L \approx 1.4142 + 0.8814 \approx 2.296$, matching the numerical value $\sim 2.29$ obtained in Q5.5.


## Question 5.4: Unit-sphere parametrization — pullback metric and positive definiteness

For $f(x_1, x_2) = (\sin x_1 \cos x_2,\, \sin x_1 \sin x_2,\, \cos x_1)^\top$:

1. Derive the Jacobian.
2. Derive the metric via Eq. 5.21 (LMLG).
3. Show the metric is positive definite.

**Answer:**

**Part 1 — Jacobian.** $f: \mathbb{R}^2 \to \mathbb{R}^3$, so $J_f$ is $3 \times 2$ with entry $(i,j) = \partial f_i / \partial x_j$:

$$
J_f(x_1, x_2) =
\begin{bmatrix}
\cos x_1 \cos x_2 & -\sin x_1 \sin x_2 \\
\cos x_1 \sin x_2 & \phantom{-}\sin x_1 \cos x_2 \\
-\sin x_1 & 0
\end{bmatrix}.
$$

**Part 2 — pullback metric.** LMLG Eq. 5.21 expresses angles via the inner product $\langle v_1, v_2 \rangle_x = v_1^\top J_f^\top J_f\, v_2$, so the pullback metric tensor is

$$
M(x) = J_f(x)^\top J_f(x), \qquad \text{shape } 2 \times 2 \text{ (symmetric)}.
$$

Compute the three distinct entries via $M_{ij} = (\text{col } i \text{ of } J) \cdot (\text{col } j \text{ of } J)$ and simplify with $\sin^2 + \cos^2 = 1$:

$$
\begin{aligned}
M_{11} &= \cos^2 x_1 \cos^2 x_2 + \cos^2 x_1 \sin^2 x_2 + \sin^2 x_1 = \cos^2 x_1 + \sin^2 x_1 = 1, \\
M_{22} &= \sin^2 x_1 \sin^2 x_2 + \sin^2 x_1 \cos^2 x_2 + 0 = \sin^2 x_1, \\
M_{12} &= -\cos x_1 \sin x_1 \cos x_2 \sin x_2 + \cos x_1 \sin x_1 \cos x_2 \sin x_2 + 0 = 0.
\end{aligned}
$$

By symmetry $M_{21} = M_{12} = 0$. Therefore

$$
\boxed{\, M(x_1, x_2) = \begin{bmatrix} 1 & 0 \\ 0 & \sin^2 x_1 \end{bmatrix}. \,}
$$

This is the standard round-sphere metric in spherical coordinates ($ds^2 = dx_1^2 + \sin^2 x_1\, dx_2^2$).

**Part 3 — positive definiteness.** $M$ is diagonal, so its eigenvalues are exactly the diagonal entries: $\lambda_1 = 1$ and $\lambda_2 = \sin^2 x_1$. A symmetric matrix is positive definite iff all eigenvalues are strictly positive.

- $\lambda_1 = 1 > 0$ trivially.
- $\lambda_2 = \sin^2 x_1 > 0$ for every $x_1 \in (0, \pi)$, since $\sin x_1 > 0$ strictly on this open interval (it vanishes only at $x_1 = 0$ and $x_1 = \pi$, the endpoints, which are excluded).

Both eigenvalues strictly positive on the entire domain, so $M(x_1, x_2)$ is positive definite for all $(x_1, x_2) \in (0, \pi) \times [0, 2\pi)$. $\square$

*Remark.* The domain choice $x_1 \in (0, \pi)$ is not arbitrary: at the poles $x_1 \in \{0, \pi\}$ we would have $\sin^2 x_1 = 0$, making $M$ singular and the parametrization degenerate (every value of $x_2$ maps to the same pole point — longitude becomes meaningless there).


## Programming Exercises

## Question 5.5: Curve Length Evaluation

Consider the curve c:[0,1]→R² defined in Eq. 17.

1. Write a computer program that evaluates the length of the curve c using Eq. 4.2 in the LMLG book.
2. If you have completed exercise 5.3:
   - (a) Did the numerical and the analytical results agree?
   - (b) Use the analytic expression for ||ċt|| to write a computer program that evaluates the length of the curve using Eq. 4.5 in the LMLG book. Note that you need to approximate the integral with a sum.

**Answer:**

Yes, the numerical and analytical results agree. The computed curve length is approximately **2.29**. 

The implementation evaluates:
- **Part 1 (Numerical, Eq. 4.2)**: Using finite differences, computing differences between consecutive curve points and summing distances.
- **Part 2(b) (Analytical, Eq. 4.5)**: Using the analytical derivative norm and integrating with the trapezoidal rule.

Both methods converge to the same result, confirming the accuracy of our implementation. See `evaluate_len_curve.ipynb` for the full code.


## Question 5.6: VAE Latent Curve Length

Consider the Bernoulli VAE that you worked on in Week 1. Train this with a two-dimensional latent space (for ease of plotting).

1. Write a computer program that evaluates the length of any latent second-order polynomial curve c using Eq. 4.2 in the LMLG book. It is recommended that you write the code to support any callable curve c.

2. (Continued in notebook) Evaluate how the VAE decoder transforms curves in latent space to output space.

**Answer:**

The implementation in `evaluate_vae_curve.ipynb` evaluates curve lengths in both latent and output (pixel) space:

**Latent Space:** 
- Curve: z₁(t) = t, z₂(t) = t² (second-order polynomial)
- Evaluated using Eq. 4.2 (sum of consecutive distances)
- **Length: 1.4789**

**Output Space:**
- Same polynomial curve passed through VAE decoder
- Decoder outputs 28×28 MNIST digit images
- **Length: 67.5504** (flattened pixel distance)

**Key Finding:** The VAE decoder causes **45.68× expansion** of curve length (4467.5% distortion). This demonstrates that:
- The decoder transformation is highly non-linear
- Distances in pixel space are much larger than latent space distances
- Different regions of latent space may have different local "expansion factors"

See `evaluate_vae_curve.ipynb` for visualization of latent curve and sample decoded images.
