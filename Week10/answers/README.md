# Week 10 – Exercise 2: Graph Neural Networks

Source questions: [Week10/exercise.md](../exercise.md)

## Theoretical Exercises

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

## Programming Exercises

## Question C.1: Examine and run the code for loading the graph data

**Answer:**

The DataBatch contains:
- **edge_index [2, 3936]**: 3936 edges in edge-list format. Row 0 = source nodes, Row 1 = destination nodes. Each column is one directed edge.
- **x [1784, 7]**: 1784 nodes total across 100 graphs, each with 7 atom-type features (one-hot encoded).
- **edge_attr [3936, 4]**: Each edge has 4 features representing bond types (single/double/triple/aromatic).
- **y [100]**: One binary label per graph (100 molecules).
- **batch [1784]**: Maps each node to its graph index (0–99) for aggregation.
- **ptr [101]**: Cumulative node pointers defining graph boundaries.

## Question C.2: Examine and run the code that defines the graph neural network SimpleGNN

**Answer:**

- **Aggregate function**: Sums all incoming messages from neighboring nodes.
- **Update function**: Updates each node's state by adding the processed aggregated neighbor messages: `state = state + update_net[r](aggregated)`.
- **Residual connection**: The `state = state + update_net[r](aggregated)` line is the residual connection — the original state is preserved and the aggregated neighborhood info is added on top, preventing information loss across rounds.
- **`torch.index_add`**: `aggregated.index_add(0, edge_index[1], message[edge_index[0]])` — for each edge, takes the message from the source node (`edge_index[0]`) and adds it into the destination node's position (`edge_index[1]`) in the aggregated tensor. The same pattern is used for graph-level aggregation (summing all node states per graph).
- **Forward function dimensions**: Inputs are `x` (num_nodes × 7), `edge_index` (2 × num_edges), `batch` (num_nodes). Output is `(num_graphs,)` — one scalar prediction per graph, produced by flattening `output_net(graph_state)` of shape `(num_graphs, 1)`.

## Question C.3: Examine and run the remaining code to fit the GNN

**Answer:**

- **Loss function**: Binary cross-entropy (`BCEWithLogitsLoss`).
- **Optimizer**: Adam with learning rate `1e-2`.
- **Learning rate scheduler**: `ExponentialLR` with `gamma=0.995` — multiplies the lr by 0.995 each epoch, slowly decreasing it over training so the model takes smaller steps as it converges.
- **Accuracy**: `(out > 0) == data.y` — predicted class is positive if output > 0, compared to true label. Summed and divided by dataset length.
- **Loss**: Computed per batch, weighted by `batch_size / dataset_length` and summed to get the epoch-level average.
- **Overfit/Underfit**: The model overfits — training loss/accuracy improves while validation diverges.

## Question C.4: Modify the code to achieve the best possible validation loss

**Answer:**

The following modifications were made to improve validation performance:

- **GRU update**: Replaced the simple residual `update_net` (Linear + ReLU) with `torch.nn.GRUCell` — the GRU gates better control how much prior state to retain vs. update each round.
- **More message passing rounds**: Increased from 4 → 7 to capture longer-range structure in molecular graphs.
- **Weight decay**: Added `weight_decay=1e-3` to Adam to regularize and reduce overfitting.
- **Faster lr decay**: Changed `gamma` from 0.995 → 0.992 to decrease the learning rate more aggressively.
- **Fewer epochs**: Reduced from 500 → 370 to stop before overfitting worsens.

## Question C.5: Save test set predictions and hand in on DTU Learn

**Answer:**

Test set predictions saved to `test_predictions.pt` using the provided code and handed in on DTU Learn.
