# Week 9 Answers: Graphs and Node Embeddings

## Question A.1: Eigenvector centrality for each node

**Answer:**

Eigenvector centrality for each node is given by the components of the principal eigenvector (corresponding to the largest eigenvalue λ₁ = 3.646).

By examining the adjacency matrix, all nodes have degree 3 except node 6 (0-indexed) which has degree 6 — identifying it as the central hub. The remaining nodes are symmetric and must share the same centrality.

The centralities are read directly from the first column of the eigenvector matrix E. Since eigenvectors are not unique in sign and centralities must be positive, we flip the sign of the (all-negative) principal eigenvector:

- **Nodes 0–4 and 6** (degree-3 nodes): centrality ≈ **0.339**
- **Node 5** (degree-6 hub): centrality ≈ **0.558**

## Question A.2: Clustering coefficient for each node

**Answer:**

Local clustering coefficient: Cᵢ = 2Lᵢ / (kᵢ(kᵢ − 1)), where kᵢ = degree, Lᵢ = edges among neighbors.

From the graph structure:
- **Nodes 0–4 and 6** (degree-3 nodes): each node's 3 neighbors form a triangle (fully connected), so Lᵢ = 3.  
  Cᵢ = 2·3 / (3·2) = **1**
- **Node 5** (hub, degree 6): 6 neighbors split into two fully-connected triplets, so L₅ = 3 + 3 = 6.  
  C₅ = 2·6 / (6·5) = 12/30 = **0.4**

## Question B.1: Final node probability distribution after one random walk step

**Answer:**

<!-- Add your answer here -->

## Question B.2: Number of distinct paths of length t from node 1

**Answer:**

<!-- Add your answer here -->

## Question C.1: Show 1 − σ(x) = σ(−x) and spot the typo in eq. 3.12

**Answer:**

<!-- Add your answer here -->

## Question C.2: Cross entropy loss for single observation S_{u,v}

**Answer:**

<!-- Add your answer here -->

## Question C.3: Edge probability when embeddings are orthogonal and b = 0

**Answer:**

<!-- Add your answer here -->

## Question D.1: Examine and run graph data loading code

**Answer:**

<!-- Add your answer here -->

## Question D.2: Examine and run the Shallow class implementation

**Answer:**

<!-- Add your answer here -->

## Question D.3: Fit model on entire graph, experiment with max_step and embedding dimensions

**Answer:**

<!-- Add your answer here -->

## Question D.4: Modify code to use train/validation split

**Answer:**

<!-- Add your answer here -->

## Question D.5: Hand in predictions (link_probabilities.pt)

**Answer:**

<!-- Add your answer here -->
