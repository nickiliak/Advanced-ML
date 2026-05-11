# Week 7 — Answers

Topic: Pullback metrics, parametrization, latent geometry of neural networks.
Source questions: [Week7/exercise.md](../exercise.md)

## Theoretical Exercises

## Question 7.1: Pullback metric of randomly projected manifold

Manifold spanned by $f : \mathbb{R}^d \to \mathbb{R}^{2D}$ with $h(x) = (f(x);\,\sigma(x))$.

1. Derive the pullback metric.

**Answer:**

The ambient space $\mathbb{R}^{2D}$ carries the standard Euclidean metric, so its metric matrix is the identity $I_{2D}$. The pullback metric of a smooth map $\varphi : \mathbb{R}^d \to \mathbb{R}^N$ into Euclidean $\mathbb{R}^N$ is

$$G_\varphi(x) = J_\varphi(x)^\top \, I \, J_\varphi(x) = J_\varphi(x)^\top J_\varphi(x).$$

For $h(x) = \begin{pmatrix} f(x) \\ \sigma(x) \end{pmatrix}$, the Jacobian block-stacks:

$$J_h(x) = \begin{pmatrix} J_f(x) \\ J_\sigma(x) \end{pmatrix}.$$

Therefore

$$G_h(x) = J_h(x)^\top J_h(x) = \begin{pmatrix} J_f(x)^\top & J_\sigma(x)^\top \end{pmatrix} \begin{pmatrix} J_f(x) \\ J_\sigma(x) \end{pmatrix} = J_f(x)^\top J_f(x) + J_\sigma(x)^\top J_\sigma(x).$$


## Question 7.2: Choice of parametrization

Normals $\mathcal{N}_1 = \mathcal{N}(0, 1^2)$, $\mathcal{N}_2 = \mathcal{N}(1, 2^2)$.

1. Compute Euclidean distance under parametrizations $(\mu,\sigma)$, $(\mu,\sigma^2)$, $(\mu,\sigma^{-2})$, $(\mu/\sigma^2,\,-1/(2\sigma^2))$.
2. Does one parametrization seem more natural? *(open-ended)*
3. Parametrization whose pullback metric matches the randomly-projected manifold (Eq. 13.8 LMLG).

**Answer:**

**1. Euclidean distances under each parametrization.**

| Parametrization θ | θ₁ | θ₂ | ‖θ₁ − θ₂‖ |
|---|---|---|---|
| (μ, σ) | (0, 1) | (1, 2) | √2 |
| (μ, σ²) | (0, 1) | (1, 4) | √10 |
| (μ, σ⁻²) | (0, 1) | (1, 1/4) | 5/4 |
| (μ/σ², −1/(2σ²)) | (0, −1/2) | (1/4, −1/8) | √13/8 |

**2. Naturalness.** The same two distributions give four wildly different Euclidean distances, so the Euclidean metric on parameter space is parametrization-dependent. A natural metric on the family of distributions must be invariant under reparametrization (e.g. Fisher information / pullback metric). Under the bare Euclidean criterion, no parametrization is intrinsically more natural — the choice is conventional.

**3. Parametrization matching Eq 13.8.** Take θ = (μ, σ) and set the mean function f(θ) = μ and the noise function σ(θ) = σ — i.e. h(θ) = (μ; σ). Then

J_f = [1, 0],   J_σ = [0, 1],

so

J_fᵀ J_f = [[1, 0], [0, 0]],   J_σᵀ J_σ = [[0, 0], [0, 1]],

and

G_θ = J_fᵀ J_f + J_σᵀ J_σ = I₂.

The pullback metric is the identity, exactly the form of Eq 13.8 with trivial Jacobians.


## Question 7.3: Bias-free ReLU networks — function equivalence

$f_l(x) = \mathrm{ReLU}(\theta_l x)$, $f = f_L \circ \dots \circ f_1$.

1. Show that $\theta$ and $\theta'$ produce the same $f$ if $\sum_l \log\theta_l = \sum_l \log\theta'_l$.

**Answer:**

Assume θ_l > 0 for all l (implicit, since the conclusion uses log θ_l).

**Positive homogeneity of ReLU.** For α ≥ 0: ReLU(αx) = max(0, αx) = α · max(0, x) = α · ReLU(x).

**Collapse the composition.** Apply the identity layer by layer:

f_2(f_1(x)) = ReLU(θ_2 · ReLU(θ_1 x))
            = θ_2 · ReLU(ReLU(θ_1 x))
            = θ_2 · ReLU(θ_1 · ReLU(x))
            = θ_2 · θ_1 · ReLU(ReLU(x))
            = θ_1 · θ_2 · ReLU(x)        (since ReLU(ReLU(x)) = ReLU(x))

Iterating through all L layers:

f(x) = (∏_{l=1}^{L} θ_l) · ReLU(x).

**Equate two parametrizations.** f_θ = f_θ' as functions iff for all x:

(∏_l θ_l) · ReLU(x) = (∏_l θ'_l) · ReLU(x).

Cancel ReLU(x) (pick any x with ReLU(x) ≠ 0):

∏_l θ_l = ∏_l θ'_l.

**Take log.** Using log(ab) = log a + log b iteratively, log(∏_l θ_l) = Σ_l log θ_l, so

Σ_{l=1}^{L} log θ_l = Σ_{l=1}^{L} log θ'_l. ∎


## Question 7.4: ReLU geodesics

$f(x) = \theta_2\,\mathrm{ReLU}(\theta_1 x)$, data $(x_1,y_1)=(-1,0)$, $(x_2,y_2)=(1,1)$.

1. Show that $(\theta_1,\theta_2)=(7,1/7)$ fits equally well as $(1,1)$.
2. Derive $\bar G_\theta = \tfrac{1}{2}(J_\theta(x_1)^\top J_\theta(x_1) + J_\theta(x_2)^\top J_\theta(x_2))$.
3. Compute the geodesic between $(\theta_1,\theta_2) = (1,1)$ and $(21,\,3/7)$.

**Answer:**

**1. Equally good fit at (θ_1, θ_2) = (7, 1/7).**

f(x_1) = f(−1) = (1/7) · ReLU(7 · (−1)) = (1/7) · ReLU(−7) = (1/7) · 0 = 0 = y_1.
f(x_2) = f(+1) = (1/7) · ReLU(7 · 1) = (1/7) · 7 = 1 = y_2.

Both data points fit exactly, same as (θ_1, θ_2) = (1, 1).

**2. Finite-sample metric estimate G̅_θ.**

Jacobian of f(θ, x) = θ_2 · ReLU(θ_1 x) wrt θ = (θ_1, θ_2), using ReLU'(u) = 1_{u > 0} and chain rule:

J_θ(x) = [∂f/∂θ_1, ∂f/∂θ_2] = [θ_2 · 1_{θ_1 x > 0} · x,  ReLU(θ_1 x)].

Assume θ_1 > 0. Evaluate at the two data points:

- At x_1 = −1: θ_1 x_1 = −θ_1 < 0 ⇒ indicator = 0, ReLU(−θ_1) = 0. So J(x_1) = [0, 0].
- At x_2 = +1: θ_1 x_2 = θ_1 > 0 ⇒ indicator = 1, ReLU(θ_1) = θ_1. So J(x_2) = [θ_2, θ_1].

Outer products (each is 2×2; entry (i,j) = column_i · row_j, single product since inner dim = 1):

J(x_1)ᵀ J(x_1) = [[0, 0], [0, 0]],

J(x_2)ᵀ J(x_2) = [[θ_2², θ_1 θ_2], [θ_1 θ_2, θ_1²]].

Therefore

G̅_θ = ½ (J(x_1)ᵀ J(x_1) + J(x_2)ᵀ J(x_2)) = ½ [[θ_2², θ_1 θ_2], [θ_1 θ_2, θ_1²]].

**3. (Programming subpart — geodesic computation — deferred.)**

$f(x) = \theta_2\,\tanh(\theta_1 x)$, same data as 7.4.

1. Derive $\bar G_\theta$. Hint: $\tfrac{d}{dx}\tanh(x) = 1 - \tanh^2(x)$.
2. Compute the geodesic between $(\theta_1,\theta_2) = (1,1)$ and $(21,\,3/7)$.

**Answer:**

**1. Finite-sample metric estimate G̅_θ.**

Jacobian of f(θ, x) = θ_2 · tanh(θ_1 x) wrt θ = (θ_1, θ_2), using $\tfrac{d}{du}\tanh(u) = 1 - \tanh^2(u)$ and the chain rule:

$$J_\theta(x) = \bigl[\, \theta_2 \cdot (1 - \tanh^2(\theta_1 x)) \cdot x, \;\; \tanh(\theta_1 x) \,\bigr].$$

Evaluate at the two data points. Using $\tanh(-u) = -\tanh(u)$ and $\tanh^2(-u) = \tanh^2(u)$, write $s := 1 - \tanh^2(\theta_1)$ and $t := \tanh(\theta_1)$:

- At $x_1 = -1$: $J(x_1) = [\, \theta_2 \cdot s \cdot (-1), \; -t \,] = [-\theta_2 s, \, -t]$.
- At $x_2 = +1$: $J(x_2) = [\, \theta_2 \cdot s \cdot 1, \; t \,] = [\theta_2 s, \, t]$.

So $J(x_1) = -J(x_2)$.

Outer products (each is 2×2; entry $(i,j) = J_i \cdot J_j$). Signs cancel under squaring, so both products are equal:

$$J(x_1)^\top J(x_1) = J(x_2)^\top J(x_2) = \begin{pmatrix} \theta_2^2 s^2 & \theta_2 \, s \, t \\ \theta_2 \, s \, t & t^2 \end{pmatrix}.$$

Average:

$$\bar G_\theta = \tfrac{1}{2}\bigl(J(x_1)^\top J(x_1) + J(x_2)^\top J(x_2)\bigr) = \begin{pmatrix} \theta_2^2 s^2 & \theta_2 \, s \, t \\ \theta_2 \, s \, t & t^2 \end{pmatrix}.$$

Substituting back $s = 1 - \tanh^2(\theta_1)$, $t = \tanh(\theta_1)$:

$$\bar G_\theta = \begin{pmatrix} \theta_2^2 (1-\tanh^2(\theta_1))^2 & \theta_2 \, (1-\tanh^2(\theta_1)) \, \tanh(\theta_1) \\ \theta_2 \, (1-\tanh^2(\theta_1)) \, \tanh(\theta_1) & \tanh^2(\theta_1) \end{pmatrix}.$$

Unlike the ReLU case (7.4), $J(x_1)$ is non-zero — tanh has no dead region, so both data points contribute. Symmetry of the data ($x_1 = -x_2$) plus oddness of tanh make the two outer products identical, so the ½ factor cancels with the duplicate.

**2. (Programming subpart — geodesic computation — deferred.)**
