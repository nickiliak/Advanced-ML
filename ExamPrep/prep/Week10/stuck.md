# Week 10 — Stuck Points

- [Q B.1] Confused L2-normalized neighbor-sum update with classical oversmoothing ("all values same") — this specific aggregate-then-normalize rule is power iteration on the adjacency matrix; the limit is the dominant eigenvector (eigenvector centrality), not a constant vector.
- [Q B.1] Forgot what power iteration converges to — revisit: write h⁽⁰⁾ in the eigenbasis of A, apply Aᵏ, normalize; the term with the largest |λ| dominates ⇒ dominant eigenvector.
- [Q B.1] Confused about what λ and v mean here — they belong to the adjacency matrix A (Aᵥ=λv), not to h. A is fixed graph structure; h decomposes in A's eigenbasis. Power iteration just amplifies the v₁ component.
- [Q B.1] Couldn't translate per-node GNN equations into matrix form — drill: Σ_{v∈N(u)} h_v = (Ah)_u where A is adjacency matrix; L2-normalized aggregate becomes h ← Ah/‖Ah‖₂. Practice rewriting other aggregate/update rules in matrix notation.
- [Q B.2] Parameter counting checklist for GNNs (cheatsheet target): (i) per round = W_self (D×D) + W_neigh (D×D) + b (D); (ii) |V| never enters — params depend on hidden dim D, not graph size; (iii) check "shared vs unshared weights across rounds" — unshared ⇒ multiply by K rounds.
