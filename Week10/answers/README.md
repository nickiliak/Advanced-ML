# Week 10 – Exercise 2: Graph Neural Networks

## Question A.1: Which of the following functions are permutation invariant?

**Answer:**

Sum, Product, and Maximum are permutation invariant — their output does not change regardless of input order. Concatenation is **not** permutation invariant, since the output vector depends on the ordering of the inputs.

## Question B.1: What will node representations converge to after many update rounds?

**Answer:**

If we assume we only use the update function, we will eventually converge according to the power iteration algorithm to $Ah / \|Ah\|^2$, which means the vector will become the eigenvector of the matrix. Since only neighbors are non-zero in the aggregation, we can compute this via dot products.

**The Convergence:**

- **What:** The unique initial features ($h^{(0)}$ values) are completely lost.
- **Why:** Repeatedly multiplying by the adjacency matrix (the AGGREGATE step) and normalizing (the UPDATE step) is the mathematical definition of Power Iteration.
- **Result:** Every node's value converges to a measure of its **eigenvector centrality**—essentially its relative importance or connectivity within the graph. This leads to the **oversmoothing problem**: all nodes become indistinguishable as they converge to the same stationary distribution.

## Question B.2: What is the total number of parameters in the GNN?

**Answer:**

For each message passing round, we need:
- $W_{\text{self}}$: a $32 \times 32$ weight matrix = $32 \times 32 = 1024$ parameters
- $W_{\text{neigh}}$: a $32 \times 32$ weight matrix = $32 \times 32 = 1024$ parameters  
- $b$: a bias vector of dimension 32 = $32$ parameters

Total per round: $1024 + 1024 + 32 = 2080$ parameters

Since we have 5 message passing rounds with unshared weight matrices:

$$5 \times (32 \times 32 + 32 \times 32 + 32) = 5 \times 2080 = \boxed{10,400 \text{ parameters}}$$

## Question C.1: Examine and run the code for loading the graph data

**Answer:**

<!-- Add your answer here -->

## Question C.2: Examine and run the code that defines the graph neural network SimpleGNN

**Answer:**

<!-- Add your answer here -->

## Question C.3: Examine and run the remaining code to fit the GNN

**Answer:**

<!-- Add your answer here -->

## Question C.4: Modify the code to achieve the best possible validation loss

**Answer:**

<!-- Add your answer here -->

## Question C.5: Save test set predictions and hand in on DTU Learn

**Answer:**

<!-- Add your answer here -->
