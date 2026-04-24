# Week 11 Answers: Graph Convolutions & Spectral Methods

## Question A.1: Impulse response output

**Answer:**
The output is the filter itself, i.e. y[n] = h[n]. With impulse x[n]=δ[n], applying y = Σ_k h[k] D^k x shifts the impulse by k at each term, so y[n] = Σ_k h[k] δ[n-k] = h[n] (impulse response equals filter).

## Question A.2: Causal filter convolution derivation

**Answer:**
From the definition y[n] = Σ_{k=-∞}^{∞} x[k]h[n−k], rewrite by substituting k → n−k to get y[n] = Σ_k x[n−k]h[k]. Causal filter means h[k] = 0 for k < 0, so the sum reduces to y[n] = Σ_{k=0}^{∞} h[k] x[n−k] = h[0]x[n] + h[1]x[n−1] + h[2]x[n−2] + .... Using the unit-delay operator Dx[n] = x[n−1] (so D^k x[n] = x[n−k]), this becomes y[n] = h[0]x[n] + h[1]Dx[n] + h[2]D²x[n] + ... = (Σ_{k=0}^{∞} h[k] D^k) x[n].

## Question A.3: Constant signal graph convolution

**Answer:**

<!-- Add your answer here -->

## Question B.1: u_k as eigenvector of cycle graph adjacency matrix

**Answer:**

<!-- Add your answer here -->

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
