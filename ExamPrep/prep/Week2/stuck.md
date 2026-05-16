# Week 2 — Stuck Points

- [Q 2.2] Composition order in G ∘ F got scrambled and proof targeted "invertible" instead of "equals identity" — revisit: (g ∘ f)(x) = g(f(x)) means apply f first; to prove inverse, show G ∘ F = id by collapsing inner f_k⁻¹ ∘ f_k = id pairs.
- [Q 2.2] Inductive step for K: kept writing "F⁻¹ ∘ H" — circular, since F⁻¹ is the target — revisit: split F = f_K ∘ H where H = f_{K−1} ∘ ... ∘ f_1, apply K=2 base case (reverse + invert) to get F⁻¹ = H⁻¹ ∘ f_K⁻¹, then apply IH to H⁻¹.
- [Q 2.2] Proof template — "property of K-fold composition": split off ONE factor (F = f_K ∘ H), prove K=2 base case directly, then induct by applying base case to (f_K ∘ H) and IH to H. Same skeleton works for: inverse of composition, det of composed Jacobians (Q 2.3), log-density of flow, derivative chain.
- [Q 2.2] Notation hygiene: never let the target symbol (F⁻¹, det J_F, …) appear on the RHS while it's still the thing being proved on the LHS — that's circular. Always re-express the target purely in terms of building blocks (f_k, f_k⁻¹, J_{f_k}, …).
