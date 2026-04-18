# Week 9: Graphs and Node Embeddings

Advanced Machine Learning — Module 3, Exercise 1.

## Exercise A: Node Level Statistics

Consider a 7-node graph with adjacency matrix A (provided in PDF). Eigendecomposition gives largest eigenvalue λ₁ = 3.646.

**Question A.1:** Determine the eigenvector centrality for each node in the graph.

**Question A.2:** Determine the clustering coefficient for each node in the graph.

---

## Exercise B: Random Walks

**Question B.1:** Given a graph with adjacency matrix A and a starting node chosen randomly according to a discrete distribution p, what is the final node's probability distribution after taking a single step from the starting node along an edge chosen uniformly at random?

**Question B.2:** Given a graph with adjacency matrix A, how many distinct paths of length t can we find starting from a specific node (say node 1)?

*Hint: Represent initial state as a one-hot vector. Single step = matrix-vector product. Generalize to t steps.*

---

## Exercise C: Shallow Embeddings

Decoder: DEC(z_u, z_v) = σ(z_u^⊤ z_v + b), where σ(x) = 1/(1+e^{-x}).

**Question C.1:** Show that 1 − σ(x) = σ(−x). Can you spot a typo in eq. 3.12 on page 37 in the book?

**Question C.2:** Write the cross entropy loss for the single observation S_{u,v} (in terms of P_{u,v} and S_{u,v}).

**Question C.3:** If z_u and z_v are orthogonal (dot product = 0) and bias b = 0, what is the probability of an edge between node u and v?

---

## Exercise D: Programming Exercise (shallow_embedding.py)

**Question D.1:** Examine and run the code for loading the graph data.
- Understand how the graph is represented as a matrix and as index pairs with target values.
- Visualize the adjacency matrix.

**Question D.2:** Examine and run the `Shallow` class implementation.
- Understand `torch.nn.Embedding` for node embeddings.
- Understand what the forward function computes. What is the role of `rx` and `tx`?

**Question D.3:** Examine and run the model fitting code (loss on entire graph, no splits).
- Experiment with different `max_step` values.
- Experiment with different embedding dimensions. How does embedding dimension influence training loss?

**Question D.4:** Modify the code to use a train/validation split.
- Random 80/20 split of node pairs.
- Train on training data only.
- Compute validation loss.
- What is the optimal embedding dimension on the validation set?

**Question D.5:** Hand in predictions.
- Use train/validation procedure to compute best predicted link probabilities.
- Save predictions to `link_probabilities.pt` and hand in on DTU Learn.
