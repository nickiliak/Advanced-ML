# Week 9: Graphs and Node Embeddings

Advanced Machine Learning — Module 3, Exercise 1.

## Exercise A: Node Level Statistics

Consider the following 7-node graph:

```
>>> print(A)
[[0. 0. 1. 1. 0. 1. 0.]
 [0. 0. 0. 0. 1. 1. 1.]
 [1. 0. 0. 1. 0. 1. 0.]
 [1. 0. 1. 0. 0. 1. 0.]
 [0. 1. 0. 0. 0. 1. 1.]
 [1. 1. 1. 1. 1. 0. 1.]
 [0. 1. 0. 0. 1. 1. 0.]]

>>> lambda, E = np.linalg.eig(A)
>>> print(np.round(lambda, 3))
[ 3.646  2.    -1.646 -1.    -1.    -1.    -1.  ]

>>> print(np.round(E, 3))
[[-0.339 -0.408 -0.228 -0.816  0.004 -0.084  0.126]
 [-0.339  0.408 -0.228 -0.    -0.374  0.69  -0.255]
 [-0.339 -0.408 -0.228  0.408  0.511  0.114 -0.493]
 [-0.339 -0.408 -0.228  0.408 -0.515 -0.03   0.367]
 [-0.339  0.408 -0.228  0.    -0.176 -0.709 -0.377]
 [-0.558 -0.     0.83  -0.     0.    -0.    -0.   ]
 [-0.339  0.408 -0.228  0.     0.55   0.019  0.632]]
```

Largest eigenvalue $\lambda_1 = 3.646$; its eigenvector is the first column of $E$.

**Question A.1:** Determine the eigenvector centrality for each node in the graph.

**Question A.2:** Determine the clustering coefficient for each node in the graph.

---

## Exercise B: Random Walks

**Question B.1:** Given a graph with adjacency matrix $A$ and a starting node chosen randomly according to a discrete distribution $\mathbf{p}$, what is the final node's probability distribution after taking a single step from the starting node along an edge chosen uniformly at random?

**Question B.2:** Given a graph with adjacency matrix $A$, how many distinct paths of length $t$ can we find starting from a specific node (say node 1)?

*Hint: represent the initial state as a one-hot vector. A single step is a matrix–vector product. Generalize to $t$ steps.*

---

## Exercise C: Shallow Embeddings

Let $S_{u,v} \in \{0, 1\}$ denote a binary feature corresponding to a non-edge / edge between nodes $u$ and $v$ (i.e. the $S_{u,v}$ are the elements of the adjacency matrix). Let

$$
P_{u,v} \;=\; P(S_{u,v} = 1 \mid \mathbf{z}_u, \mathbf{z}_v, b) \;=\; \sigma\!\left(\mathbf{z}_u^\top \mathbf{z}_v + b\right)
$$

denote the predicted probability that the edge is present, given the latent node embeddings $\mathbf{z}_u, \mathbf{z}_v$ and bias $b$.

Decoder:

$$
\mathrm{DEC}(\mathbf{z}_u, \mathbf{z}_v) \;=\; \sigma\!\left(\mathbf{z}_u^\top \mathbf{z}_v + b\right), \qquad \sigma(x) = \frac{1}{1 + e^{-x}}.
$$

**Question C.1:** Show that $1 - \sigma(x) = \sigma(-x)$. Can you spot a typo in eq. 3.12 on page 37 in the book?

**Question C.2:** Write the cross-entropy loss for the single observation $S_{u,v}$ (in terms of $P_{u,v}$ and $S_{u,v}$).

**Question C.3:** If $\mathbf{z}_u$ and $\mathbf{z}_v$ are orthogonal ($\mathbf{z}_u^\top \mathbf{z}_v = 0$) and bias $b = 0$, what is the probability of an edge between node $u$ and $v$?

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
