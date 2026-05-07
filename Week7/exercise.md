# Week 7 Exercises — Pullback Metrics & Latent Geometry

Source: `02460_week7_exercises.pdf` (Advanced Machine Learning 02460, March 2026, v1.0)

> Note: the PDF lists all exercises sequentially without a `Theoretical / Programming` split. All exercises are grouped under *Theoretical Exercises* — the "write a computer program" subtasks in 7.4 and 7.5 are minor extensions of the derivations.

## Theoretical Exercises

### Exercise 7.1 (Metric of randomly projected manifold)

Consider the manifold spanned by the mapping $f : \mathbb{R}^d \to \mathbb{R}^{2D}$ defined as

$$h(x) = \begin{pmatrix} f(x) \\ \sigma(x) \end{pmatrix}.$$

1. Derive the pullback metric of this manifold.

### Exercise 7.2 (Choice of parametrization)

Consider two normal distributions

$$\mathcal{N}_1 = \mathcal{N}(\mu_1, \sigma_1^2), \qquad \mathcal{N}_2 = \mathcal{N}(\mu_2, \sigma_2^2),$$

where $\mu_1 = 0$, $\mu_2 = 1$, $\sigma_1 = 1$, $\sigma_2 = 2$.

1. Compute the Euclidean distance between these distributions in the following parametrizations:

$$\theta = (\mu, \sigma), \quad \theta = (\mu, \sigma^2), \quad \theta = (\mu, \sigma^{-2}), \quad \theta = \left(\tfrac{\mu}{\sigma^2}, \tfrac{-1}{2\sigma^2}\right).$$

2. Does one parametrization seem more natural (or better) than another? *(open-ended)*
3. Find a parametrization of normal distributions such that the associated pullback metric corresponds to that of the randomly projected manifold (Eq. 13.8 in the LMLG book).

### Exercise 7.3 (Bias-free ReLU networks)

Consider a neural network consisting of layers

$$f_l(x) = \mathrm{ReLU}(\theta_l\, x),$$

such that the joint network is

$$f(x) = (f_L \circ \dots \circ f_1)(x) = f_L(\dots f_2(f_1(x))).$$

1. Show that two parameter vectors $\theta$ and $\theta'$ produce the same function $f$ if

$$\sum_{l=1}^{L} \log \theta_l = \sum_{l=1}^{L} \log \theta'_l.$$

### Exercise 7.4 (ReLU geodesics)

Consider the neural network $f(x) = \theta_2\,\mathrm{ReLU}(\theta_1\,x)$ and observational data

$$\begin{pmatrix}x_1\\y_1\end{pmatrix} = \begin{pmatrix}-1\\0\end{pmatrix}, \qquad \begin{pmatrix}x_2\\y_2\end{pmatrix} = \begin{pmatrix}1\\1\end{pmatrix}.$$

This data can perfectly fit with the parameters $\theta_1 = \theta_2 = 1$.

1. Show that $\theta_1 = 7$ and $\theta_2 = 1/7$ provides an equally good fit to the data.
2. Derive the finite-sample estimate of the metric $G_\theta = \mathbb{E}[J_\theta(x)^\top J_\theta(x)]$ given by

$$\bar G_\theta = \tfrac{1}{2}\bigl(J_\theta(x_1)^\top J_\theta(x_1) + J_\theta(x_2)^\top J_\theta(x_2)\bigr).$$

3. Write a computer program to compute the geodesic between parameters

$$\begin{pmatrix}\theta_1\\\theta_2\end{pmatrix} = \begin{pmatrix}1\\1\end{pmatrix} \quad\text{and}\quad \begin{pmatrix}\theta_1\\\theta_2\end{pmatrix} = \begin{pmatrix}21\\3/7\end{pmatrix}.$$

### Exercise 7.5 (Hyperbolic tangent networks)

Consider the neural network $f(x) = \theta_2\,\tanh(\theta_1\,x)$ and observational data

$$\begin{pmatrix}x_1\\y_1\end{pmatrix} = \begin{pmatrix}-1\\0\end{pmatrix}, \qquad \begin{pmatrix}x_2\\y_2\end{pmatrix} = \begin{pmatrix}1\\1\end{pmatrix}.$$

1. Derive the finite-sample estimate of the metric $G_\theta = \mathbb{E}[J_\theta(x)^\top J_\theta(x)]$ given by

$$\bar G_\theta = \tfrac{1}{2}\bigl(J_\theta(x_1)^\top J_\theta(x_1) + J_\theta(x_2)^\top J_\theta(x_2)\bigr).$$

It may be helpful to recall that the derivative of $\tanh(x)$ is $1 - \tanh^2(x)$.

2. Write a computer program to compute the geodesic between parameters

$$\begin{pmatrix}\theta_1\\\theta_2\end{pmatrix} = \begin{pmatrix}1\\1\end{pmatrix} \quad\text{and}\quad \begin{pmatrix}\theta_1\\\theta_2\end{pmatrix} = \begin{pmatrix}21\\3/7\end{pmatrix}.$$
