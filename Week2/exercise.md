# Week 2 Exercises — Normalizing Flows

Source: `02460_week2_exercises.pdf` (Advanced Machine Learning 02460, Feb 2026, v1.31)

## Theoretical Exercises

### Exercise 2.1 (Volume-preserving linear transformation)

Consider a linear transformation $f : \mathbb{R}^D \to \mathbb{R}^D$ given by $f(x) = -x + a$ for some $a \in \mathbb{R}^D$. Show that this transformation is *volume-preserving* (cf. section 4.1.1 of Tomczak 2024).

### Exercise 2.2 (Inverse of a composition)

Let $F(x) = f_K \circ f_{K-1} \circ \dots \circ f_2 \circ f_1(x)$, where $f_k : \mathbb{R}^D \to \mathbb{R}^D$ for $k = 1, \dots, K$ are invertible. Show that

$$F^{-1}(z) = f_1^{-1} \circ f_2^{-1} \circ \dots \circ f_{K-1}^{-1} \circ f_K^{-1}(z).$$

*Hint:* show $(F^{-1} \circ F)(x) = x$ and $(F \circ F^{-1})(z) = z$ via induction — first $K = 2$, then $K > 2$ assuming the $K-1$ case.

### Exercise 2.3 (Determinant of composed Jacobians)

Consider $h = g \circ f$ with $f, g : \mathbb{R}^D \to \mathbb{R}^D$. Show that $|\det J_h| = |\det J_g|\,|\det J_f|$.

1. Show $J_h = J_g J_f$:
   - (a) Use the chain rule for $\partial h_i / \partial x_j$.
   - (b) Use the definition of matrix multiplication for the $(i,j)$ entry of $J_g J_f$.
2. Use that the determinant distributes over multiplication.

*Hint:* the chain rule is $\partial h_i / \partial x_j = \nabla g_i(f(x)) \cdot \partial f / \partial x_j$.

## Programming Exercises

The main task is to implement the **masked coupling layer** from Real NVP (Dinh et al. 2017). Provided files: `flow.py` (incomplete flow implementation), `ToyData.py` (toy data generators).

The masked coupling layer is

$$z' = b \odot z + (1 - b) \odot (z \odot \exp(s(b \odot z)) + t(b \odot z)),$$

with inverse

$$z = b \odot z' + (1 - b) \odot ((z' - t(b \odot z')) \odot \exp(-s(b \odot z'))),$$

and log-determinant $\log|\det J_T(z)| = \sum_d (1 - b_d)\, s_d(b \odot z)$.

### Exercise 2.4 (Masked Coupling Layer Implementation)

In `flow.py`, the class `MaskedCouplingLayer` is missing forward, inverse and log-det. Complete:

- `MaskedCouplingLayer.forward(...)` returns $T(z)$ and $\log|\det J_T(z)|$.
- `MaskedCouplingLayer.inverse(...)` returns $T^{-1}(z')$ and $\log|\det J_{T^{-1}}(z')|$.

Test on the TwoGaussians dataset; tune the number of coupling layers and the network architecture for a good qualitative fit. Make the implementation work for $D > 2$.

*Optional:* fit a flow to the Chequerboard dataset (hard).

### Exercise 2.5 (Flow on dequantized MNIST)

Train a flow on dequantized MNIST. Each pixel is rescaled to $[0,1]$, dequantized, and the image is flattened to dimension $784$. For stability, add `tanh` at the end of the scale network.

Implement two masking strategies:
- Random mask, freshly initialised per layer (saved in `MaskedCouplingLayer`).
- Chequerboard mask, inverted at each layer.

Save samples from the flow and qualitatively assess sample quality.

### Exercise 2.6 (VAE with flow prior)

Extend the Bernoulli VAE from week 1 to use a flow prior based on the model from exercise 2.4.

- Evaluate the test-set ELBO. Better performance?
- Plot samples from the approximate posterior and from the prior. Do they match well?

*Hint:* use the same ELBO formulation as for the MoG prior.
