# Week 10 – Exercise 2: Graph Neural Networks

Source: `02460_week10_exercises.pdf` (Advanced Machine Learning — Module 3, Exercise 2)

## Theoretical Exercises

### Exercise A: Invariant Aggregation Functions

In a graph neural network, when aggregating information from neighbors or when aggregating from all nodes for a graph-level prediction, the aggregation function must not depend on the order of the inputs.

**Question A.1:** Which of the following functions on $(x_1, x_2, \dots, x_N)$ are permutation invariant?

1. **Sum:** $g\!\left(\sum_{n=1}^N f(x_n)\right) = g(f(x_1) + f(x_2) + \dots + f(x_N))$
2. **Product:** $g\!\left(\prod_{n=1}^N f(x_n)\right) = g(f(x_1) \cdot f(x_2) \cdots f(x_N))$
3. **Maximum:** $g\!\left(\max_{n=1}^N f(x_n)\right) = g(\max(f(x_1), f(x_2), \dots, f(x_N)))$
4. **Concatenation:** $g\!\left(\bigsqcup_{n=1}^N f(x_n)\right) = g([f(x_1), f(x_2), \dots, f(x_N)])$

for arbitrary $f(\cdot)$ and $g(\cdot)$.

---

### Exercise B: Simple Graph Neural Networks

Consider a GNN defined as

$$\textbf{aggregate:}\quad m_{N(u)}^{(k)} = \sum_{v \in N(u)} h_v^{(k)}$$

$$\textbf{update:}\quad h_u^{(k+1)} = \frac{m_{N(u)}^{(k)}}{\sqrt{\sum_{v \in V} (m_{N(v)}^{(k)})^2}}$$

where node representations are scalar and initialized randomly.

**Question B.1:** Assuming a large number of update rounds is computed, what will the node representations converge to?

*Hint:* Consider the basic GNN, where each round is

$$h_u^{(k)} = \sigma\!\left(W_{\text{self}}^{(k)} h_u^{(k-1)} + W_{\text{neigh}}^{(k)} \sum_{v \in N(u)} h_v^{(k-1)} + b^{(k)}\right).$$

**Question B.2:** If $|V| = 10$, the node-representation dimension is $D = 32$ (i.e. $h_u^{(k)} \in \mathbb{R}^{32}$), the GNN performs $5$ message-passing rounds, and weight matrices are not shared between rounds, what is the total number of parameters?

## Programming Exercises

### Exercise C: Programming Exercise

In this exercise you will work with a graph neural network for graph-level classification implemented in `gnn_graph_classification.py`.

We will use the MUTAG dataset (Debnath et al.): a collection of nitroaromatic compounds (molecular graphs); the task is graph-level binary classification (mutagenicity on Salmonella typhimurium). Vertices are atoms, edges are bonds, and 7 discrete node labels are atom types (one-hot). 188 graphs total.

**Question C.1:** Examine and run the code for loading the graph data.

- Extract a single batch via `data_batch = next(iter(train_loader))`.
- Examine these variables:
  - `data_batch.x` — node features
  - `data_batch.edge_index` — edges
  - `data_batch.batch` — index of which graph in the batch each node belongs to

**Question C.2:** Examine and run the code that defines the graph neural network `SimpleGNN`.

- Based on the `__init__` and `forward` functions, sketch the GNN architecture.
- What are the **aggregate** and **update** functions implemented?
- Where and how are residual connections used?
- The messages are aggregated using a sum via `torch.index_add`. Make sure you understand this function. The same function is used for graph-level aggregation.
- What are the dimensions and purpose of the inputs and the output of `forward`?

**Question C.3:** Examine and run the remaining code to fit the GNN. Make sure you understand:

- Which loss function, optimizer, and learning rate are used?
- What does the learning rate scheduler do?
- How is the training/validation loss and accuracy computed?

After fitting, examine the two generated plots — does the model overfit or underfit?

**Question C.4:** Modify the code to achieve the best possible validation loss. Do not change the training/validation split, and do not look at the test set. Consider:

- Model hyperparameters (state dimension, number of message-passing rounds).
- Optimizer hyperparameters (lr schedule, number of epochs).
- Regularization (weight decay or dropout).
- Architecture changes (e.g. GRU update).

**Question C.5:** Save your test set predictions in `test_predictions.pt` and hand it in on DTU Learn. The lowest test loss will be honored as the class winner.
