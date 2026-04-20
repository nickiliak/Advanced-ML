# Week 11: Exercise 3 — Theory and Generative Models

Source: `Exercise_3.pdf`

## Exercise A: Graph Convolutions

A discrete-time signal is given as a sequence of values x[n], where n is an integer time index. The convolution between two discrete signals x[n] and h[n] is defined as:

y[n] = (x ⋆ h)[n] = Σ x[k]h[n−k]

The neighborhood shift operator on graphs is defined as Dx[n] = Ax[n−1], giving the graph convolution:

y[n] = (x ⋆_G h)[n] = (Σ h[k] D^k) x[n]

### Question A.1
Consider the following input signal x[n] = 1 if n=0, 0 otherwise (impulse). What is the resulting output of the filter?

### Question A.2
Show that the convolution of a signal with a causal filter can be written as:

y[n] = h[0]x[n] + h[1]Dx[n] + h[2]D²x[n] + ... = (Σ_{k=0}^∞ h[k] D^k) x[n]

### Question A.3
Assume that the filter h[n] is only nonzero for 0 ≤ n ≤ N, and apply a constant signal x[n] = x. What is the value of the signal y[n]? (Hint: It is a constant independent of n.) Compare your result with Eq. 7.21 in the book.

---

## Exercise B: Graph Fourier Transform

The Graph Fourier Transform (GFT) is defined using the eigendecomposition A = UΛU*, with GFT: x̃ = U*x and inverse GFT: x = Ux̃.

The vector u_k has components (u_k)_n = e^{-i2πkn/N} (complex exponential, normalized frequency k).

### Question B.1
Show that u_k is an eigenvector of the adjacency matrix of the cycle graph, Au_k = λu_k. (Hint: show that (Au_k)_n = λ_k(u_k)_n for some λ_k.)

### Question B.2
Show that the graph convolution of a signal with a causal filter can be written in the spectral domain as:

ỹ = Σ_{k=0}^∞ h[k] Λ^k x̃

### Question B.3
Is there an advantage of the spectral approach in terms of computational complexity? Consider the necessary operations and their computational complexity (as they scale with the graph size). Consider what might be pre-computed when learning the filter h[n].

---

## Exercise C: Programming Exercise

In this exercise you will work with a graph convolution model for graph-level classification implemented in `graph_convolution.py`. The dataset is MUTAG (188 molecular graphs, binary classification of mutagenicity).

### Question C.1
Examine and run the script. Go through each code block to remind yourself about the structure of the script. The script is very similar to last week's script, except for the model definition.

### Question C.2
Examine the model definition in `SimpleGraphConv`, and go through the details in the `__init__` and `forward` functions.
- Notice how the graph filter is defined and initialized: h[0] = 1 and h[k] for k > 1 are small random numbers. Why might this be a reasonable initialization?
- Make sure you understand the role and function of `to_dense_adj` and `to_dense_batch`. How do they handle graphs with different numbers of nodes?
- Examine the for-loop that computes the graph convolution. Match it up against the formulas in the theoretical exercises and the book.
- Notice how the output filter is defined. What is its role and dimensions?

### Question C.3
Modify the implementation of the graph convolution so that it is computed in the spectral domain, rather than in the vertex domain. Change from:

y = Σ_{k=0}^N h[k] A^k x

to:

y = U (Σ_{k=0}^N h[k] Λ^k) U* x

Hint: Use `torch.linalg.eigh` for eigenvalue decomposition (ensures real results). The two implementations should give identical results (except for small numerical differences).

### Question C.4 (Optional)
Modify the implementation so that the eigenvalue decompositions are pre-computed and given as input to the forward function. Additionally, pre-compute the dense matrices from `to_dense_batch` and `to_dense_adj`. This should significantly speed up training.
