# Week 11: Exercise 3 — Theory and Generative Models

Source: `02460_week11_exercises.pdf`

## Exercise A: Graph Convolutions

A discrete-time signal is given as a sequence of values $x[n]$, where $n$ is an integer time index. The convolution between two discrete signals $x[n]$ and $h[n]$ is defined as:

$$y[n] = (x \star h)[n] = \sum_{k=-\infty}^{\infty} x[k]\, h[n-k]$$

The convolution is a linear operation performed on two discrete-time signals to produce a third signal. In filtering, $x[n]$ is the input signal, $h[n]$ is the filter (impulse response), and $y[n] = (x \star h)[n]$ is the output signal. Depending on $h[n]$, the operation can amplify or attenuate different frequency components.

### Question A.1

Consider the following input signal

$$x[n] = \begin{cases} 1 & n = 0 \\ 0 & \text{otherwise} \end{cases}$$

which is known as an **impulse**. What is the resulting output of the filter?

---

The impulse response of the filter $h[n]$ tells us how the system responds across time to a signal applied at time $n=0$. We usually have $h[n] = 0\ \forall\, n < 0$ so that the system does not respond before the input signal is applied. This is called a **causal** filter.

Let us define the **unit delay operator** $D$:

$$D\, x[n] = x[n-1]$$

When applied to a signal, $D$ shifts (delays) it one unit in time.

### Question A.2

Show that the convolution of a signal with a causal filter can be written as

$$
\begin{aligned}
y[n] &= h[0]\, x[n] + h[1]\, D\, x[n] + h[2]\, D^{2}\, x[n] + \dots \\
     &= \left( \sum_{k=0}^{\infty} h[k]\, D^{k} \right) x[n]
\end{aligned}
$$

---

Now consider **graph convolutions**: a signal $\boldsymbol{x}[n]$ is defined on the nodes of a graph, where each component is a time-varying scalar node signal that propagates from nodes to their neighbors. On a graph, the signal at each node spreads to its neighbors at each time step, written as matrix multiplication with the adjacency matrix followed by a time delay. Thus, the **neighborhood shift operator** is

$$D\, \boldsymbol{x}[n] = \boldsymbol{A}\, \boldsymbol{x}[n-1]$$

With this operator, the graph convolution of a signal with a causal filter is

$$\boldsymbol{y}[n] = (\boldsymbol{x} \star_{\mathcal{G}} h)[n] = \left( \sum_{k=0}^{\infty} h[k]\, D^{k} \right) \boldsymbol{x}[n]$$

This describes how the signal spreads in space (across the graph) and in time.

### Question A.3

Assume the filter $h[n]$ is only nonzero for $0 \le n \le N$, and apply a constant signal $\boldsymbol{x}[n] = \boldsymbol{x}$. What is the value of the signal $\boldsymbol{y}[n]$? *(Hint: it is a constant independent of $n$.)* Compare with Eq. 7.21 in the book:

$$\boldsymbol{Q}_h\, \boldsymbol{x} = \alpha_0\, \boldsymbol{I}\, \boldsymbol{x} + \alpha_1\, \boldsymbol{A}\, \boldsymbol{x} + \alpha_2\, \boldsymbol{A}^2\, \boldsymbol{x} + \dots + \alpha_N\, \boldsymbol{A}^N\, \boldsymbol{x}$$

---

## Exercise B: Graph Fourier Transform

The **discrete Fourier transform (DFT)** is a mathematical operation that converts a finite-length sequence (signal) $x[n]$ into a sequence of complex numbers $\tilde{x}[k]$, representing the signal's frequency content. The DFT is widely used in signal processing for analyzing and manipulating signals in the frequency domain. Given a sequence $x[n]$ of length $N$, the DFT is defined as:

$$\tilde{x}[k] = \sum_{n=0}^{N-1} x[n]\, e^{-i\, \tfrac{2\pi k}{N}\, n}$$

The DFT computes the inner product of $x[n]$ with complex exponentials, each representing a different frequency component.

Consider a **cycle graph** with $N$ vertices: each vertex is connected to its two adjacent vertices. Formally, $\mathcal{V} = \{0, 1, \dots, N-1\}$ and $\mathcal{E} = \{(0,1), (1,2), \dots, (N-2, N-1), (N-1, 0)\}$. For $N=6$ the adjacency matrix is

$$
\boldsymbol{A} =
\begin{bmatrix}
0 & 1 & 0 & 0 & 0 & 1 \\
1 & 0 & 1 & 0 & 0 & 0 \\
0 & 1 & 0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 & 0 & 1 \\
1 & 0 & 0 & 0 & 1 & 0
\end{bmatrix}
$$

Consider a vector $\boldsymbol{u}_k$ with components

$$(\boldsymbol{u}_k)_n = e^{-i\, \tfrac{2\pi k}{N}\, n}$$

This is a complex exponential — a sinusoid where the integer $k$ is the normalized frequency.

### Question B.1

Show that $\boldsymbol{u}_k$ is an eigenvector of the adjacency matrix of the cycle graph: $\boldsymbol{A}\, \boldsymbol{u}_k = \lambda_k\, \boldsymbol{u}_k$.

*Hint: show the relation holds component-wise, i.e. $(\boldsymbol{A}\, \boldsymbol{u}_k)_n = \lambda_k\, (\boldsymbol{u}_k)_n$ for some $\lambda_k$.*

---

Since the complex exponential $\boldsymbol{u}_k$ is an eigenvector of the adjacency matrix for any integer frequency $k$, the eigendecomposition of the adjacency matrix of the cycle graph yields the DFT basis. We generalize this to define the **graph Fourier basis** for any graph as the eigenvectors of the adjacency matrix.

Given the eigendecomposition

$$\boldsymbol{A} = \boldsymbol{U}\, \boldsymbol{\Lambda}\, \boldsymbol{U}^{*}$$

the **graph Fourier transform (GFT)** of a signal $\boldsymbol{x}$ is

$$\tilde{\boldsymbol{x}} = \boldsymbol{U}^{*}\, \boldsymbol{x}, \qquad \text{(inverse GFT: } \boldsymbol{x} = \boldsymbol{U}\, \tilde{\boldsymbol{x}}\text{)}$$

### Question B.2

Show that the graph convolution of a signal with a causal filter can be written in the spectral domain as

$$\tilde{\boldsymbol{y}} = \sum_{k=0}^{\infty} h[k]\, \boldsymbol{\Lambda}^{k}\, \tilde{\boldsymbol{x}}$$

We now have two ways to compute the graph convolution with a finite-length filter — directly in the vertex domain, and in the spectral domain:

$$\boldsymbol{y} = \sum_{k=0}^{N} h[k]\, \boldsymbol{A}^{k}\, \boldsymbol{x} = \boldsymbol{U} \left( \sum_{k=0}^{N} h[k]\, \boldsymbol{\Lambda}^{k} \right) \boldsymbol{U}^{*}\, \boldsymbol{x} \tag{1}$$

### Question B.3

Is there an advantage of the spectral approach in terms of computational complexity? Consider the necessary operations and their complexity (as they scale with graph size). Consider what might be pre-computed when learning the filter $h[n]$.

---

## Exercise C: Programming Exercise

In this exercise you will work with a graph convolution model for graph-level classification implemented in `graph_convolution.py`.

We will use the **MUTAG dataset** (Debnath et al.): a collection of nitroaromatic compounds (molecular graphs); the task is graph-level binary classification (mutagenicity on *Salmonella typhimurium*). Vertices represent atoms, edges represent bonds, and the 7 discrete node labels are atom types (one-hot encoded). 188 graphs total.

### Question C.1

Examine and run the script. Go through each code block to remind yourself of the structure. The script is very similar to last week's, except for the model definition.

### Question C.2

Examine the model definition in `SimpleGraphConv`, and go through the details in `__init__` and `forward`.

- Notice how the graph filter is defined and initialized: $h[0] = 1$ and $h[k]$ for $k > 1$ are small random numbers. Think about what a graph convolution does when only $h[0] = 1$ and the remaining coefficients are zero. Why might this be a reasonable initialization?
- Understand the role of `to_dense_adj` and `to_dense_batch`. Look up their documentation. How do they handle graphs of different sizes?
- Examine the for-loop that computes the graph convolution. Match it up against the formulas in the theoretical exercises and the book.
- Notice how the output filter is defined. What is its role and dimensions?

### Question C.3

Modify the implementation so that the graph convolution is computed in the **spectral domain** rather than in the vertex domain. The current implementation is based on:

$$\boldsymbol{y} = \sum_{k=0}^{N} h[k]\, \boldsymbol{A}^{k}\, \boldsymbol{x}$$

and your task is to change the implementation to:

$$\boldsymbol{y} = \boldsymbol{U} \left( \sum_{k=0}^{N} h[k]\, \boldsymbol{\Lambda}^{k} \right) \boldsymbol{U}^{*}\, \boldsymbol{x}$$

*Hint: compute the eigenvalue decomposition with `torch.linalg.eigh` (real-valued result — easier to implement).*

The two implementations should give identical results (up to small numerical differences). Test your implementation against the original.

### Question C.4 (Optional)

Modify the implementation so that the eigenvalue decompositions are **pre-computed** and passed as input to the `forward` function. Additionally, pre-compute the dense matrices from `to_dense_batch` and `to_dense_adj`. This should significantly speed up training.
