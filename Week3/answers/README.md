# Week 3 - Diffusion Models (DDPM)

Source questions: [Week3/exercise.md](../exercise.md)

## Theoretical Exercises

## Question 3.1: $q(z_T \mid x) \to \mathcal{N}(0, I)$ as $T \to \infty$

For any noise schedule $0 < \beta_1 < \dots < \beta_T < 1$, show that $q(z_T \mid x)$ approaches a standard Gaussian.

**Answer:**

<!-- Add your answer here -->


## Question 3.2: Derive Ho et al. (2020) eq. 5 from eq. 3

Reproduce Appendix A of Ho et al. (2020) — explain every step from equations (17) through (22).

**Answer:**

<!-- Add your answer here -->


## Question 3.3: Closed-form $L_{t-1} = \tfrac{1}{2\sigma_t^2}\|\tilde\mu - \mu_\theta\|^2 + C$

Apply the multivariate-Gaussian KL formula to $L_{t-1} = \mathrm{KL}(q(z_{t-1} \mid z_t, x)\,\|\,p(z_{t-1}\mid z_t))$.

**Answer:**

<!-- Add your answer here -->


## Programming Exercises

## Question 3.4: Complete the DDPM implementation

Complete the DDPM implementation (ddpm.py), by implementing the following parts:

- DDPM.negative_elbo(...) should return the negative ELBO of equation (14) by Ho et al. (2020) by implementing Algorithm 1 in the paper.
- DDPM.sample(shape) should implement Algorithm 2 in the paper by Ho et al. (2020). For the covariance matrix of the reverse process use σ²ₜI with σ²ₜ = βₜ.

Test the implementation on both the TwoGaussians and Chequerboard datasets and answer the following questions:

- Can you improve the fit to the Chequerboard dataset by modifying the network architecture?
- How does the DDPM qualitatively compare to the Flow model from week 2 on the two toy datasets?

**Answer:**

<!-- Add your answer here -->

## Question 3.5: Use the DDPM implementation to learn on MNIST

Use the DDPM implementation from exercise 3.4 to learn a DDPM on MNIST. You do not need to implement a discrete likelihood function for the DDPM as suggested in section 3.3 by Ho et al. (2020). Instead, dequantize the pixel values and transform them to [-1, 1].

You should both test a fully connected architecture and the provided U-Net architecture (in unet.py). Please answer the following questions:

- Can you learn a DDPM on MNIST using a fully connected architecture?
- How do the samples from the DDPM qualitatively compare to the VAE and Flow models from week 1 and 2?

**Answer:**

<!-- Add your answer here -->
