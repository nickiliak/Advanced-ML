# Week 11 — Stuck Points

- [Q A.3] Confused graph shift D **x**[n] = **A x**[n−1] with scalar shift D x[n] = x[n−1]; dropped the **A** factor when applying D^k — revisit graph neighborhood shift operator definition vs scalar unit-delay.
- [Q B.1] Got that (A u_k)_n = λ_k (u_k)_n must hold component-wise and only 2 entries of row n are 1, but couldn't write the surviving 2 terms explicitly — revisit which 2 nodes are neighbors of node n on the cycle graph (n−1 and n+1 mod N).
- [Q B.1] Got stuck on factoring e^{−i 2π k (n±1)/N} — forgot exponent rule e^{a+b} = e^a · e^b for separating the n part from the ±1 part. Revisit exponent algebra.
- [Q B.2] Didn't know: symmetric/Hermitian matrices have an orthonormal eigenbasis ⇒ U is unitary ⇒ U*U = UU* = I. This is what makes (UΛU*)^k telescope to U Λ^k U*. Revisit spectral theorem.
- [Q B.2] Didn't see GFT as an operational tool: to convert any vertex-domain equation to spectral, left-multiply both sides by U*. By definition ỹ = U* y, x̃ = U* x. Remember: applying U* on the left = "go to frequency domain".
- [Q B.3] Over-counted vertex-domain complexity: tried to count both A^k self-multiplications AND vector multiplication separately. The trick is to NOT compute A^k explicitly — recursively apply v_k = A·v_{k−1} for one matrix-vector product (O(N²)) per term, N+1 terms → O(N³) total. Don't materialize matrix powers.
