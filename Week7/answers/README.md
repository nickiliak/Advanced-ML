# Week 7 — Answers

Topic: Pullback metrics, parametrization, latent geometry of neural networks.
Source questions: [Week7/exercise.md](../exercise.md)

## Theoretical Exercises

## Question 7.1: Pullback metric of randomly projected manifold

Manifold spanned by $f : \mathbb{R}^d \to \mathbb{R}^{2D}$ with $h(x) = (f(x);\,\sigma(x))$.

1. Derive the pullback metric.

**Answer:**

<!-- Add your answer here -->


## Question 7.2: Choice of parametrization

Normals $\mathcal{N}_1 = \mathcal{N}(0, 1^2)$, $\mathcal{N}_2 = \mathcal{N}(1, 2^2)$.

1. Compute Euclidean distance under parametrizations $(\mu,\sigma)$, $(\mu,\sigma^2)$, $(\mu,\sigma^{-2})$, $(\mu/\sigma^2,\,-1/(2\sigma^2))$.
2. Does one parametrization seem more natural? *(open-ended)*
3. Parametrization whose pullback metric matches the randomly-projected manifold (Eq. 13.8 LMLG).

**Answer:**

<!-- Add your answer here -->


## Question 7.3: Bias-free ReLU networks — function equivalence

$f_l(x) = \mathrm{ReLU}(\theta_l x)$, $f = f_L \circ \dots \circ f_1$.

1. Show that $\theta$ and $\theta'$ produce the same $f$ if $\sum_l \log\theta_l = \sum_l \log\theta'_l$.

**Answer:**

<!-- Add your answer here -->


## Question 7.4: ReLU geodesics

$f(x) = \theta_2\,\mathrm{ReLU}(\theta_1 x)$, data $(x_1,y_1)=(-1,0)$, $(x_2,y_2)=(1,1)$.

1. Show that $(\theta_1,\theta_2)=(7,1/7)$ fits equally well as $(1,1)$.
2. Derive $\bar G_\theta = \tfrac{1}{2}(J_\theta(x_1)^\top J_\theta(x_1) + J_\theta(x_2)^\top J_\theta(x_2))$.
3. Compute the geodesic between $(\theta_1,\theta_2) = (1,1)$ and $(21,\,3/7)$.

**Answer:**

<!-- Add your answer here -->


## Question 7.5: Hyperbolic-tangent networks — geodesic

$f(x) = \theta_2\,\tanh(\theta_1 x)$, same data as 7.4.

1. Derive $\bar G_\theta$. Hint: $\tfrac{d}{dx}\tanh(x) = 1 - \tanh^2(x)$.
2. Compute the geodesic between $(\theta_1,\theta_2) = (1,1)$ and $(21,\,3/7)$.

**Answer:**

<!-- Add your answer here -->
