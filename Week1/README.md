# Week 1 - Deep Latent Variable Models

## Programming Exercises

### Question 1.4: VAE Implementation Inspection

Inspect the code in vae_bernoulli.py and answer the following questions:
- How is the reparametrisation trick handled in the code?
- Consider the implementation of the ELBO. What is the dimension of self.decoder(z).log_prob(x) and of td.kl_divergence(q, self.prior.distribution)?
- The implementation of the prior, encoder and decoder classes all make use of td.Independent. What does this do?
- What is the purpose of using the function torch.chunk in GaussianEncoder.forward?

**Answer:**

The reparameterization trick is implemented using `q.rsample()` in the ELBO computation. Instead of using `sample()` which breaks gradient flow, `rsample()` performs a reparameterized sample that allows backpropagation through the sampling operation. Mathematically, it samples from a standard normal distribution and transforms it using the learned parameters: z = μ + σ * ε, where ε ~ N(0,1), making this transformation differentiable and enabling gradient flow through the encoder.

For the ELBO implementation:
- The dimension of `self.decoder(z).log_prob(x)` is `(batch_size,)`, where each entry is the total log probability for one image in the batch. This is because `td.Independent` sums the log probabilities over all pixels for each sample.
- The dimension of `td.kl_divergence(q, self.prior())` is also `(batch_size,)`, as the KL divergence is computed independently for each sample in the batch.

Both terms return a vector with one value per sample, not per pixel, because the distribution objects aggregate over the image dimensions.

`td.Independent` creates a distribution where each variable (e.g., pixel or latent dimension) is treated as independent. In the code, this means the prior, encoder, and decoder model each pixel or latent variable as independent, and the log probabilities are aggregated (summed) across all those dimensions for each sample.

The function `torch.chunk` in `GaussianEncoder.forward` splits the output of the encoder network into two tensors along the last dimension: one for the mean and one for the standard deviation of the Gaussian distribution. This is necessary because the encoder network outputs both parameters concatenated together, and they need to be separated to define the Gaussian distribution for the latent variables.


### Question 1.5: VAE with Bernoulli Output - Extensions

Add the following functionality to the implementation (vae_bernoulli.py) of the VAE with Bernoulli output distributions:
- Evaluate the ELBO on the binarised MNIST test set.
- Plot samples from the approximate posterior and colour them by their correct class label for each datapoint in the test set (i.e., samples from the aggregate posterior).
- Implement it such that for latent dimensions larger than two (M > 2), do PCA and project the sample onto the first two principal components (e.g., using scikit-learn).

**Answer:**

<!-- Add your answer here -->


### Question 1.6: VAE with Mixture of Gaussian Prior

Extend the VAE with Bernoulli output distributions (vae_bernoulli.py) to use a mixture of Gaussian prior (MoG). For your implementation:
- Evaluate the test set ELBO. Do you see better performance?
- Plot the samples from the approximate posterior. How does it differ from the model with the Gaussian prior? Do you see better clustering?

**Answer:**

<!-- Add your answer here -->


### Question 1.7: VAE with Continuous Output Distributions

Consider the pixel values in MNIST as continuous and experiment with different output distributions. Implement a multivariate Gaussian output distribution. You should experiment with learning the variance of each pixel and having a fixed variance for all pixels:
- How is the qualitative sample quality?
- Rather than sampling from p(x|z), try to sample z ∼ p(z) and then show the mean of the output distribution, p(x|z). Does the mean qualitatively look better?

Optional: You can also try the Continuous Bernoulli output distribution.

**Answer:**

<!-- Add your answer here -->


### Question 1.8: VAE with CNN-Based Architecture (Optional)

Extend the VAE with Bernoulli output distributions (vae_bernoulli.py) to use a CNN-based encoder and decoder. For your new implementation:
- When sampling from a trained model, do you see a qualitative improvement in sample quality?
- Evaluate the test set ELBO. Do you see better performance?

**Answer:**

<!-- Add your answer here -->
