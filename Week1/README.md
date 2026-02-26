# Week 1 - Deep Latent Variable Models

## Programming Exercises

### Question 1.4: VAE Implementation Inspection

Inspect the code in vae_bernoulli.py and answer the following questions:
- How is the reparametrisation trick handled in the code?
- Consider the implementation of the ELBO. What is the dimension of self.decoder(z).log_prob(x) and of td.kl_divergence(q, self.prior.distribution)?
- The implementation of the prior, encoder and decoder classes all make use of td.Independent. What does this do?
- What is the purpose of using the function torch.chunk in GaussianEncoder.forward?

**Answer:**

<!-- Add your answer here -->


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
