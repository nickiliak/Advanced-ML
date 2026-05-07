# Week 2 - Normalizing Flows

Source questions: [Week2/exercise.md](../exercise.md)

## Theoretical Exercises

## Question 2.1: Linear transformation $f(x) = -x + a$ is volume-preserving

Show that the linear transformation $f(x) = -x + a$ is volume-preserving (cf. section 4.1.1 of Tomczak 2024).

**Answer:**

<!-- Add your answer here -->


## Question 2.2: Inverse of a composition of invertible functions

For $F = f_K \circ \dots \circ f_1$ with each $f_k$ invertible, show $F^{-1} = f_1^{-1} \circ \dots \circ f_K^{-1}$.

**Answer:**

<!-- Add your answer here -->


## Question 2.3: $|\det J_{g \circ f}| = |\det J_g|\,|\det J_f|$

For $h = g \circ f$:

1. Show $J_h = J_g J_f$ via the chain rule and matrix multiplication.
2. Use the determinant's multiplicativity to conclude.

**Answer:**

<!-- Add your answer here -->


## Programming Exercises

## Question 2.4: Masked Coupling Layer Implementation

In the provided code (flow.py), the class MaskedCouplingLayer implements the masked coupling layer from Real NVP (Dinh et al. 2017), but it does not implement the forward transformation, the inverse transformation and the corresponding calculations of the log determinant of the Jacobian.

Complete the following two functions such that:
- `MaskedCouplingLayer.forward(...)` returns $T(z)$ and $\log \det J_T(z)$
- `MaskedCouplingLayer.inverse(...)` returns $T^{-1}(z')$ and $\log \det J_{T^{-1}}(z')$

Use the TwoGaussians dataset for testing the model. Adjust the number of coupling layers and the architecture of the networks to get a good fit to the density (by qualitative assessment). 

Optional: Can you also fit a flow to the Chequerboard dataset? It is difficult to find an architecture that gives a good fit.

**Answer:**

<!-- Add your answer here -->


## Question 2.5: Training a Normalizing Flow on MNIST

Use the flow implementation from exercise 2.4 to train a flow on dequantized MNIST. You do not need to implement a dequantization layer, as you can perform this transformation on MNIST when you load it.

**Answer:**

<!-- Add your answer here -->


## Question 2.6: VAE with Flow Prior

Extend the VAE with Bernoulli output (vae_bernoulli.py) from week 1 to use a flow prior based on the model from exercise 2.4. For your implementation of the VAE with the flow prior:
- Evaluate the test set ELBO. Do you see better performance?
- Compare the results with the VAE using a standard Gaussian prior and a mixture of Gaussians prior.

**Answer:**

<!-- Add your answer here -->
