# Week 11 Answers: Graph Convolutions & Spectral Methods

Source questions: [Week11/exercise.md](../exercise.md)

## Theoretical Exercises

## Question A.1: Impulse response output

**Answer:**
With the impulse $x[n] = \delta[n]$ and the graph convolution

$$y[n] = \left( \sum_{k} h[k]\, D^k \right) x[n],$$

the shift acts as $D^k \delta[n] = \delta[n-k]$, so

$$y[n] = \sum_{k} h[k]\, \delta[n-k] = h[n].$$

The output equals the filter itself — the impulse response *is* $h[n]$.

## Question A.2: Causal filter convolution derivation

**Answer:**
Start from

$$y[n] = \sum_{k=-\infty}^{\infty} x[k]\, h[n-k].$$

Substitute $k \to n-k$:

$$y[n] = \sum_{k=-\infty}^{\infty} h[k]\, x[n-k].$$

Causality means $h[k] = 0$ for $k < 0$, so

$$y[n] = \sum_{k=0}^{\infty} h[k]\, x[n-k] = h[0]\,x[n] + h[1]\,x[n-1] + h[2]\,x[n-2] + \dots$$

Using the unit-delay operator $D x[n] = x[n-1]$, so $D^k x[n] = x[n-k]$:

$$y[n] = h[0]\,x[n] + h[1]\,D x[n] + h[2]\,D^2 x[n] + \dots = \left( \sum_{k=0}^{\infty} h[k]\, D^k \right) x[n].$$

## Question A.3: Constant signal graph convolution

**Answer:**
Since $h[n]$ is nonzero only for $0 \le n \le N$ (causal, finite support), by A.2:

$$y[n] = \sum_{k=0}^{N} h[k]\, D^k x[n].$$

The shift acts as $D x[n] = x[n-1]$, so for a constant signal $x[n] = x$ we have $D^k x[n] = x$ for all $k$. Therefore

$$y[n] = \left( \sum_{k=0}^{N} h[k] \right) x,$$

a constant independent of $n$. Comparing to Eq. 7.21,

$$\mathbf{Q}_h \mathbf{x} = \alpha_0 \mathbf{I}\mathbf{x} + \alpha_1 \mathbf{A}\mathbf{x} + \dots + \alpha_N \mathbf{A}^N \mathbf{x},$$

the chain-graph causal-filter form has the same structure as the general-graph spatial filter, with $h[k]$ playing the role of $\alpha_k$ and $D = \mathbf{A}$.

## Question B.1: u_k as eigenvector of cycle graph adjacency matrix

**Answer:**
On the cycle graph $C_N$, each node $n$ has exactly two neighbors, $n-1$ and $n+1$ (mod $N$), so the adjacency action at node $n$ reads off only those two entries:

$$(A u_k)_n = (u_k)_{n-1} + (u_k)_{n+1}.$$

Substitute the given form $(u_k)_n = e^{-i 2\pi k n / N}$:

$$(A u_k)_n = e^{-i 2\pi k (n-1) / N} + e^{-i 2\pi k (n+1) / N}.$$

Factor out $(u_k)_n = e^{-i 2\pi k n / N}$. Pulling $-n$ out of $-(n-1)$ leaves $+1$ in the exponent, and out of $-(n+1)$ leaves $-1$:

$$(A u_k)_n = (u_k)_n \left( e^{+i 2\pi k / N} + e^{-i 2\pi k / N} \right) = (u_k)_n \cdot 2\cos\!\left(\frac{2\pi k}{N}\right).$$

Therefore $A u_k = \lambda_k u_k$ holds for every $n$ with the same scalar

$$\lambda_k = 2\cos\!\left(\frac{2\pi k}{N}\right),$$

so $u_k$ is an eigenvector of the cycle adjacency matrix with eigenvalue $\lambda_k$.

## Question B.2: Spectral domain graph convolution derivation

**Answer:**
Start from the vertex-domain graph convolution with a causal filter:

$$\boldsymbol{y} = \sum_{k=0}^{N} h[k]\, \boldsymbol{A}^k\, \boldsymbol{x}.$$

Substitute the eigendecomposition $\boldsymbol{A} = \boldsymbol{U}\, \boldsymbol{\Lambda}\, \boldsymbol{U}^{*}$. Because the eigenvectors are orthonormal (the adjacency of an undirected graph is symmetric, so the spectral theorem applies), $\boldsymbol{U}^{*}\boldsymbol{U} = \boldsymbol{I}$. Expanding $(\boldsymbol{U}\boldsymbol{\Lambda}\boldsymbol{U}^{*})^k$ telescopes through $k-1$ copies of $\boldsymbol{U}^{*}\boldsymbol{U} = \boldsymbol{I}$, giving

$$\boldsymbol{A}^k = \boldsymbol{U}\, \boldsymbol{\Lambda}^k\, \boldsymbol{U}^{*}.$$

Substitute and factor $\boldsymbol{U}$ and $\boldsymbol{U}^{*}$ (independent of $k$) outside the sum:

$$\boldsymbol{y} = \sum_{k=0}^{N} h[k]\, \boldsymbol{U}\, \boldsymbol{\Lambda}^k\, \boldsymbol{U}^{*}\, \boldsymbol{x} = \boldsymbol{U} \left( \sum_{k=0}^{N} h[k]\, \boldsymbol{\Lambda}^k \right) \boldsymbol{U}^{*}\, \boldsymbol{x}.$$

Apply the GFT to both sides by left-multiplying with $\boldsymbol{U}^{*}$. Using $\tilde{\boldsymbol{y}} = \boldsymbol{U}^{*} \boldsymbol{y}$, $\tilde{\boldsymbol{x}} = \boldsymbol{U}^{*} \boldsymbol{x}$, and $\boldsymbol{U}^{*}\boldsymbol{U} = \boldsymbol{I}$:

$$\tilde{\boldsymbol{y}} = \boldsymbol{U}^{*} \boldsymbol{y} = (\boldsymbol{U}^{*}\boldsymbol{U}) \left( \sum_{k=0}^{N} h[k]\, \boldsymbol{\Lambda}^k \right) (\boldsymbol{U}^{*}\boldsymbol{x}) = \sum_{k=0}^{N} h[k]\, \boldsymbol{\Lambda}^k\, \tilde{\boldsymbol{x}}.$$

In the spectral domain the graph convolution becomes a sum of powers of the *diagonal* matrix $\boldsymbol{\Lambda}$ acting on $\tilde{\boldsymbol{x}}$ — i.e. a per-frequency polynomial in the eigenvalues.

## Question B.3: Computational complexity — spectral vs vertex domain

**Answer:**
**Vertex-domain cost** ($\boldsymbol{y} = \sum_{k=0}^{N} h[k]\, \boldsymbol{A}^k\, \boldsymbol{x}$). Do not materialize the matrix powers. Apply $\boldsymbol{A}$ recursively to keep a running vector $\boldsymbol{v}_k = \boldsymbol{A}\, \boldsymbol{v}_{k-1}$ with $\boldsymbol{v}_0 = \boldsymbol{x}$. Each matrix-vector product on a dense $N\times N$ matrix costs $O(N^2)$, and we need $N+1$ of them, then scalar-weighted accumulation $\sum_k h[k]\, \boldsymbol{v}_k$ (negligible $O(N^2)$ total). Net per forward pass: $O(N \cdot N^2) = O(N^3)$.

**Spectral-domain cost** ($\boldsymbol{y} = \boldsymbol{U}\, (\sum_{k=0}^{N} h[k]\, \boldsymbol{\Lambda}^k)\, \boldsymbol{U}^{*}\, \boldsymbol{x}$):
- $\boldsymbol{U}^{*}\boldsymbol{x}$: one $N\times N$ matvec — $O(N^2)$.
- $\sum_{k=0}^{N} h[k]\, \boldsymbol{\Lambda}^k$: $\boldsymbol{\Lambda}$ is diagonal, so this collapses to a diagonal matrix whose $i$-th entry is the polynomial $\sum_{k=0}^{N} h[k]\, \lambda_i^k$. Horner evaluation per eigenvalue is $O(N)$, over $N$ eigenvalues → $O(N^2)$.
- diagonal · vector: $O(N)$.
- $\boldsymbol{U} \cdot (\cdot)$: one matvec — $O(N^2)$.

Net per forward pass: $O(N^2)$ — one order of magnitude better than the vertex form.

**The catch — and why it's still a win.** Computing the eigendecomposition $\boldsymbol{A} = \boldsymbol{U}\, \boldsymbol{\Lambda}\, \boldsymbol{U}^{*}$ costs $O(N^3)$. *However*, when learning the filter $h[n]$, the graph adjacency $\boldsymbol{A}$ is fixed — only the scalar coefficients $h[0], \dots, h[N]$ are updated each gradient step. So $\boldsymbol{U}$ and $\boldsymbol{\Lambda}$ can be **precomputed once** and reused across all training iterations.

Over $T$ training iterations:
- Vertex: $T \cdot O(N^3)$.
- Spectral: $O(N^3) + T \cdot O(N^2)$ — eigendecomposition amortized.

Spectral wins as soon as $T \gg N$, which is the typical training regime. Likewise at inference time on the same graph, the precomputed $\boldsymbol{U}, \boldsymbol{\Lambda}$ keep each forward pass at $O(N^2)$.

## Programming Exercises

## Question C.1: Examine and run the script

**Answer:**

<!-- Add your answer here -->

## Question C.2: Examine the SimpleGraphConv model definition

**Answer:**

<!-- Add your answer here -->

## Question C.3: Implement spectral domain graph convolution

**Answer:**

<!-- Add your answer here -->

## Question C.4: Pre-compute eigenvalue decompositions (Optional)

**Answer:**

<!-- Add your answer here -->
