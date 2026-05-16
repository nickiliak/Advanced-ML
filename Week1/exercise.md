# Week 1 Exercises — Deep Latent Variable Models

Source: `02460_week1_exercises.pdf` (Advanced Machine Learning 02460, Feb 2026, v1.51)

## Theoretical Exercises

### Exercise 1.1 (PPCA — ML estimate of $b$)

Consider probabilistic principal component analysis (PPCA), as described in section 5.2 of the textbook (Tomczak 2024). The PPCA model has three parameters $\sigma^2 \in \mathbb{R}_+$, $b \in \mathbb{R}^D$ and $W \in \mathbb{R}^{D\times M}$. Given a data set $\mathcal{D} = \{x_1, \dots, x_N\}$, show that the maximum likelihood estimate of $b$ is the mean of the data set, i.e. $\hat b = \bar x$. Do this by following the steps:

Equation (5.6) — marginal in closed form:

$$p(x) = \int \mathcal{N}(x \mid Wz + b, \sigma^2 I)\, \mathcal{N}(z \mid 0, I)\, dz = \mathcal{N}(x \mid b, WW^\top + \sigma^2 I).$$

1. Based on equation (5.6), write the log-likelihood function $\ell(\sigma^2, b, W) = \ln p(\mathcal{D} \mid \sigma^2, b, W) = \sum_{n=1}^N \ln p(x_n \mid \sigma^2, b, W)$.
2. Set the derivative of the log-likelihood with respect to $b$ equal to zero.

*Hint:* For a symmetric matrix $W$ and vectors $x$ and $b$,

$$\frac{\partial}{\partial b}(x-b)^\top W(x-b) = -2W(x-b),$$

(see Petersen and Pedersen 2012, eq. 86).

### Exercise 1.2 (KL form of ELBO)

Equation (5.17) — amortized ELBO:

$$\ln p(x) \geq \mathbb{E}_{z \sim q_\phi(z\mid x)}[\ln p(x\mid z)] - \mathbb{E}_{z \sim q_\phi(z\mid x)}[\ln q_\phi(z\mid x) - \ln p(z)].$$

The second term of the ELBO in equation (5.17) of Tomczak (2024) can be written as a KL divergence:

$$\mathrm{ELBO}(x) = \mathbb{E}_{z \sim q_\phi(z\mid x)}[\ln p(x\mid z)] - \mathbb{E}_{z \sim q_\phi(z\mid x)}[\ln q_\phi(z\mid x) - \ln p(z)] = \mathbb{E}_{z \sim q_\phi(z\mid x)}[\ln p(x\mid z)] - \mathrm{KL}[q_\phi(z\mid x) \| p(z)].$$

1. Show that the two ELBO expressions are equivalent, i.e. $\mathbb{E}_{z \sim q_\phi(z\mid x)}[\ln q_\phi(z\mid x) - \ln p(z)] = \mathrm{KL}[q_\phi(z\mid x) \| p(z)]$.
2. Show that the KL divergence between two univariate Gaussians is

$$\mathrm{KL}[\mathcal{N}(\mu_1, \sigma_1^2) \| \mathcal{N}(\mu_2, \sigma_2^2)] = \ln\frac{\sigma_2}{\sigma_1} + \frac{\sigma_1^2 + (\mu_1 - \mu_2)^2}{2\sigma_2^2} - \frac{1}{2}.$$

### Exercise 1.3 (Two-level hierarchical VAE — ELBO)

Consider the two-level hierarchical VAE (section 5.5 of Tomczak 2024). The log marginal is

$$\ln p(x) = \ln \iint p(x \mid z_1)\, p(z_1 \mid z_2)\, p(z_2)\, dz_1\, dz_2.$$

First, show that the ELBO can be written as

$$\mathrm{ELBO}(x) = \mathbb{E}_{z_1 \sim q(z_1\mid x)}[\ln p(x\mid z_1)] - \mathbb{E}_{z_1, z_2 \sim Q(z_1, z_2 \mid x)}\!\left[\ln \tfrac{q(z_1\mid x)}{p(z_1\mid z_2)}\right] - \mathbb{E}_{z_1 \sim q(z_1\mid x)}[\mathrm{KL}[q(z_2 \mid z_1) \| p(z_2)]],$$

assuming a bottom-up variational distribution $Q(z_1, z_2 \mid x) = q(z_2 \mid z_1)\, q(z_1 \mid x)$.

Second, reorganize the expectations to reach equation (5.82) of the textbook:

$$\mathrm{ELBO}(x) = \mathbb{E}_{z_1, z_2 \sim Q(z_1, z_2 \mid x)}\!\left[\ln p(x\mid z_1) - \ln \tfrac{q(z_1\mid x)}{p(z_1\mid z_2)} - \mathrm{KL}[q(z_2\mid z_1) \| p(z_2)]\right].$$

## Programming Exercises

In this week's programming exercise, you will work with VAEs on a binarised version of MNIST. The provided file `vae_bernoulli.py` contains a modular implementation of a VAE with a Gaussian prior, product-of-Bernoulli likelihood and fully-connected encoder/decoder.

### Exercise 1.4 (Inspect the VAE code)

Inspect the code in `vae_bernoulli.py` and answer:

- How is the reparametrisation trick handled?
- Consider the ELBO. What is the dimension of `self.decoder(z).log_prob(x)` and of `td.kl_divergence(q, self.prior.distribution)`?
- The prior, encoder and decoder all use `td.Independent`. What does this do?
- What is the purpose of `torch.chunk` in `GaussianEncoder.forward`?

### Exercise 1.5 (VAE extensions — ELBO, posterior, PCA)

Add the following to `vae_bernoulli.py`:

- Evaluate the ELBO on the binarised MNIST test set.
- Plot samples from the approximate posterior, coloured by class label (aggregate posterior).
- For latent dimensions $M > 2$, do PCA and project samples onto the first two principal components.

### Exercise 1.6 (VAE with Mixture-of-Gaussians prior)

Extend the VAE to use a mixture-of-Gaussians prior (recommended: `MixtureSameFamily`).

- Evaluate the test-set ELBO. Better performance?
- Plot samples from the approximate posterior. How does it differ from the Gaussian-prior model? Better clustering?

### Exercise 1.7 (Continuous output distributions)

Treat MNIST pixel values as continuous. Implement a multivariate Gaussian output distribution; experiment with learning per-pixel variance and with a fixed shared variance.

- How is the qualitative sample quality?
- Rather than sampling from $p(x\mid z)$, sample $z \sim p(z)$ and show the mean of $p(x\mid z)$. Does the mean look better?

*Optional:* Try the Continuous Bernoulli output distribution.

### Exercise 1.8 *(Optional)* — CNN-based VAE

Extend the VAE to use a CNN-based encoder and decoder.

- Qualitative improvement in sample quality?
- Test-set ELBO — better performance?
