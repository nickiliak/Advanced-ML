# Week 7 — Stuck Points

- [Concept: pullback metric] Blocked on definition — could not write (φ*g)_p(v, w) — revisit: differential dφ_p as a linear map T_p M → T_{φ(p)} N and how to compose it with g.
- [Q 7.1] Confused matrix form Jᵀ G_N J — put function values f(x), σ(x) in the middle instead of ambient metric G_N — revisit: G_N is the metric tensor of the target space (identity for Euclidean ℝᴰ), not the function output.
- [Q 7.1] Guessed middle matrix as "P(h)" — revisit: Euclidean inner product u·v = uᵀ I v, so the middle matrix is the identity I.
- [Q 7.2] Wrote Euclidean distance as √(x₁²−x₂² + y₁²−y₂²) — revisit: it's √((x₁−x₂)² + (y₁−y₂)²); subtract components first, then square.
- [Q 7.2.2] Picked smallest-distance parametrization as "more natural" — revisit: naturalness ≠ smaller number; a natural metric must be invariant to reparametrization (Fisher / pullback metric), so under Euclidean none is more natural.
- [Q 7.2.3] Confused parametrizing a family of normals with the standard normal — answered "0 and 1" — revisit: for N(μ, σ²) the mean function is μ and the noise function is σ; these vary across the family.
- [Q 7.2.3] Wrote Jacobian as function values, not partial derivatives — revisit: J of f(μ,σ)=μ is the row [∂f/∂μ, ∂f/∂σ] = [1, 0].
- [Q 7.2.3] Mixed J_fᵀJ_f + J_σᵀJ_σ into a cross-term J_fᵀJ_σ — revisit: each summand uses the same Jacobian twice (outer product of column with row), then sum.
- [Q 7.3] Unfamiliar with "positive homogeneity of ReLU" — revisit: ReLU(αx) = α·ReLU(x) for α ≥ 0, the property that lets scalars be pulled out across ReLU.
- [Q 7.3] Log identity gap: forgot log(ab) = log a + log b — revisit: log turns products into sums, iterated gives log(∏ θ_l) = Σ log θ_l.
- [Q 7.3] Tried to distribute log through multiplication: wrote (∏ θ_l)·ReLU(x) → (Σ log θ_l)·ReLU(x) — revisit: log applies to the whole side, not to one factor; cancel ReLU(x) first, then log the product.
- [Q 7.4] Forgot the derivative of ReLU — revisit: ReLU'(u) = 1 if u > 0, else 0 (i.e. the indicator 1_{u>0}); at u=0 it's a subgradient.
- [Q 7.4] Repeated outer-product mistake: tried to sum products inside entries — revisit: for v vector, vᵀv has entry (i,j) = v_i · v_j (single product, not a sum); the sum-of-products only appears in inner products.
