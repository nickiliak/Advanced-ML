# Week 11 Answers: Graph Convolutions & Spectral Methods

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

<!-- Add your answer here -->

## Question B.3: Computational complexity — spectral vs vertex domain

**Answer:**

<!-- Add your answer here -->

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
