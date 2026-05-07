# Week 3 Exercises — Diffusion Models (DDPM)

Source: `02460_week3_exercises.pdf` (Advanced Machine Learning 02460, Feb 2026, v1.31)

Focus: denoising diffusion probabilistic model (DDPM), section 5.5.3 of Tomczak (2024) and Ho et al. (2020).

## Theoretical Exercises

### Exercise 3.1 (Limit of the noise schedule)

From equation (5.98) in Tomczak (2024),

$$q(z_t \mid x) = \mathcal{N}(z_t \mid \sqrt{\bar\alpha_t}\,x,\,(1 - \bar\alpha_t)I), \qquad \bar\alpha_t = \prod_{s=1}^{t}(1 - \beta_s).$$

Show that for any noise schedule $0 < \beta_1 < \dots < \beta_T < 1$, $q(z_T \mid x)$ becomes a standard Gaussian as $T \to \infty$:

$$q(z_T \mid x) \to \mathcal{N}(z_T \mid 0, I) \text{ as } T \to \infty.$$

### Exercise 3.2 (DDPM loss derivation — Ho et al. eq. 5)

Derive equation (5) from equation (3) in Ho et al. (2020). The derivation appears in Appendix A; explain every step from each equation to the next in (17)–(22).

### Exercise 3.3 (Closed form of the $L_{t-1}$ term)

Consider the $(t-1)$th term of the DDPM ELBO (Tomczak 5.102 / Ho et al. eq. 5):

$$L_{t-1} = \mathrm{KL}(q(z_{t-1} \mid z_t, x) \| p(z_{t-1} \mid z_t)),$$

where

$$q(z_{t-1} \mid z_t, x) = \mathcal{N}(z_{t-1} \mid \tilde\mu(z_t, x),\,\tilde\beta_t I), \qquad p(z_{t-1} \mid z_t) = \mathcal{N}(z_{t-1} \mid \mu_\theta(z_t, t),\,\sigma_t^2 I).$$

Show that

$$L_{t-1} = \frac{1}{2\sigma_t^2}\,\|\tilde\mu(z_t, x) - \mu_\theta(z_t, t)\|^2 + C,$$

where $C$ does not depend on $\theta$.

*Hint:* the KL between two $D$-dimensional multivariate Gaussians $\mathcal{N}_0(\mu_0, \Sigma_0)$ and $\mathcal{N}_1(\mu_1, \Sigma_1)$ is

$$\mathrm{KL}(\mathcal{N}_0 \| \mathcal{N}_1) = \tfrac{1}{2}\bigl(\log\det(\Sigma_1 \Sigma_0^{-1}) + (\mu_0 - \mu_1)^\top \Sigma_1^{-1}(\mu_0 - \mu_1) + \mathrm{tr}(\Sigma_1^{-1}\Sigma_0) - D\bigr),$$

(see Rasmussen and Williams 2005, eq. A.23).

## Programming Exercises

The main task is to implement the DDPM (Ho et al. 2020). Start with the toy datasets from week 2 (TwoGaussians, Chequerboard), then move to MNIST. Provided files: `ddpm.py` (incomplete DDPM for toy data), `unet.py` (U-Net for MNIST). Also need `ToyData.py` from week 2.

### Exercise 3.4 (Complete the DDPM implementation)

Complete `ddpm.py`:

- `DDPM.negative_elbo(...)` — return the negative ELBO of equation (14) in Ho et al. (2020) by implementing Algorithm 1.
- `DDPM.sample(shape)` — implement Algorithm 2. For the reverse-process covariance use $\sigma_t^2 I$ with $\sigma_t^2 = \beta_t$.

`FcNetwork.forward(x, t)` takes a batch and a time step (per element) and concatenates them; normalize the time step to $[0, 1]$.

Test on TwoGaussians and Chequerboard:

- Can you improve the fit to Chequerboard by modifying the network architecture?
- How does the DDPM qualitatively compare to the Flow model from week 2 on the two toy datasets?

### Exercise 3.5 (DDPM on MNIST)

Use the DDPM implementation from 3.4 to learn a DDPM on MNIST. Do **not** implement a discrete likelihood; instead dequantize the pixel values (as for flows) and transform them to $[-1, 1]$.

Test both a fully-connected architecture and the provided U-Net (`unet.py`):

- Can you learn a DDPM on MNIST using a fully-connected architecture?
- How do DDPM samples qualitatively compare to the VAE and Flow models from weeks 1-2?

*Hint:* batch size ~64, train ~50–100 epochs (≈15 min on a GPU).
