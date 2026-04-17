# Week 10 – Exercise 2: Graph Neural Networks

## Exercise C: Programming Exercise

In this exercise you will work with a graph neural network for graph-level classification implemented in the script `gnn_graph_classification.py`.

We will use the MUTAG dataset introduced by Debnath et al.: a collection of nitroaromatic compounds (molecular graphs) and the task is to predict their mutagenicity on Salmonella typhimurium (graph-level binary classification). Vertices represent atoms and edges represent bonds, and the 7 discrete node labels represent the atom type (one-hot encoded). There are a total of 188 graphs in the dataset.

## Question C.1: Examine and run the code for loading the graph data

- Extract a single batch from the training loader using `data_batch = next(iter(train_loader))`.
- The variable `data_batch` will then contain the following important variables which you should examine to make sure you understand:
  - `data_batch.x`: Node features
  - `data_batch.edge_index`: Edges
  - `data_batch.batch`: Index of which graph in the batch each node belongs to.

## Question C.2: Examine and run the code that defines the graph neural network SimpleGNN

- Based on the components defined in the `__init__` function and the computations carried out in the `forward` function, sketch a diagram of the graph neural network architecture.
- What are the **aggregate** and **update** functions that are implemented?
- Where and how are residual connections used?
- The messages are aggregated using a sum. To do this, the code uses the function `torch.index_add`. Make sure you understand this function, and look up its documentation if necessary. The same function is used to compute the graph-level aggregation.
- What are the dimensions and purpose of the inputs and the output of the `forward` function?

## Question C.3: Examine and run the remaining code to fit the GNN

Make sure you understand the following:
- Which loss function, optimizer, and learning rate are used?
- What does the learning rate scheduler do?
- How is the training/validation loss and accuracy computed?

After having fitted the GNN, examine the two generated plots. Does the model seem to overfit or underfit?

## Question C.4: Modify the code to achieve the best possible validation loss

Do not change the training/validation split, and do not look at the test set. You might consider the following modifications:
- Change the model hyperparameters (the state dimension and number of message passing rounds)
- Change optimizer hyperparameters (learning rate schedule and number of epochs).
- Regularize by adding weight decay or dropout layers.
- Change the model architecture, for example by introducing a GRU update.

## Question C.5: Save test set predictions and hand in on DTU Learn

Using the provided code, save your test set predictions in a file `test_predictions.pt`, and hand it in on DTU Learn. The lowest test loss will be honored as the class winner.
