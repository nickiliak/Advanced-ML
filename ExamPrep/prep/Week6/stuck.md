# Week 6 — Stuck Points

- [Q 6.1] Confused base-point `x` with tangent vector `v` in the local norm — plugged components of `x` into the quadratic form instead of `v` — Revisit: Riemannian norm `||v||_G = sqrt(v^T G v)` is a quadratic form in `v`, with `G` evaluated at the base point.

- [Q 6.1] Computed v₁ᵀv₂ = 1 instead of 0 for the standard basis vectors v₁=(1,0), v₂=(0,1) — Revisit: dot product of orthogonal standard basis vectors is 0, not 1.
- [Q 6.1] Did not recall the angle formula under a Riemannian metric (only the Euclidean version u·v / (‖u‖‖v‖)) — Revisit: cos θ = ⟨u,v⟩_G / (‖u‖_G · ‖v‖_G), where ⟨u,v⟩_G = uᵀGv. Conformal metrics (G = s(x)·I) preserve Euclidean angles since the scalar cancels.
- [Q 6.2] Did not see how to evaluate Christoffel symbols Γᵐⱼₖ when G = I — Revisit: every entry of I is constant (1s and 0s, no dependence on c), so ∂[G]ᵢⱼ/∂[c]ₖ = 0 → numerator inside Eq. 7.20 vanishes → Γᵐⱼₖ ≡ 0.
- [Q 6.2] Did not see why solving the geodesic ODE with boundary conditions was needed — Revisit: a geodesic ODE alone has infinitely many solutions; "geodesic connecting x₁ and x₂" specifies a boundary-value problem c(0)=x₁, c(1)=x₂, which selects the unique curve. Alternative IVP form: c(0)=x₀, ċ(0)=v.
- [Q 6.2] Did not grasp role of Christoffel coefficients Γᵐⱼₖ vs the acceleration c̈ — initially thought Γ = c̈ — Revisit: Γ are scalar coefficients (Eq. 7.20) that multiply ċⱼ·ċₖ inside the RHS of Eq. 7.19; they encode how the metric varies. Flat metric → ∂G = 0 → Γ = 0 → c̈ = 0 → straight-line geodesics. Curved metric → Γ ≠ 0 → geodesics bend.
- [Q 6.3] Confused about how to invert a diagonal matrix — thought inverse swaps onto the counter-diagonal — Revisit: inverse of diagonal matrix diag(d₁,d₂,...,dₙ) is diag(1/d₁,1/d₂,...,1/dₙ); zeros stay zero. For G = s(c)·I, [G⁻¹]ₘᵢ = (1/s(c))·δₘᵢ.
- [Q 6.3] Did not know how to collapse a sum involving a Kronecker delta — Revisit: Σᵢ aᵢ·δₘᵢ = aₘ. Mechanical recipe: wherever i appears in the rest of the term, replace it with m; the sum disappears. Used to collapse Σᵢ in Eq. 7.20 once [G⁻¹]ₘᵢ = (1/s)δₘᵢ.

---

## Cheatsheet candidates (lift to final 3-page sheet)

Compact rules that came up via stuck-points and are worth carrying into the exam:

**Riemannian norm / inner product / angle (any metric G_x):**
- ‖v‖_G = √(vᵀ G v)
- ⟨u, v⟩_G = uᵀ G v
- cos θ_G = ⟨u, v⟩_G / (‖u‖_G · ‖v‖_G)
- Conformal metric G = s(x)·I → angles same as Euclidean (scalar cancels); lengths scale by √s(x).

**Diagonal matrix inverse:**
- diag(d₁,…,dₙ)⁻¹ = diag(1/d₁,…,1/dₙ); zeros stay zero.
- G = s(c)·I ⇒ G⁻¹ = (1/s)·I, i.e. [G⁻¹]ₘᵢ = (1/s)δₘᵢ.

**Index gymnastics:**
- Kronecker collapse: Σᵢ aᵢ · δₘᵢ = aₘ. Replace every i with m, drop the sum.
- ∂/∂c_k (c₁²+…+c_d²) = 2c_k.
- For G_{ij} = s(c)·δ_{ij} with s = 1+‖c‖²:  ∂G_{ab}/∂c_c = 2c_c · δ_{ab}.

**Geodesic pipeline (Hauberg LMLG, p.64):**
- Eq. 7.20 — Christoffel: Γᵐⱼₖ = ½ Σᵢ [G⁻¹]ₘᵢ (2 ∂G_{ij}/∂c_k − ∂G_{jk}/∂c_i).
- Eq. 7.19 — ODE: [c̈]ₘ = − Σⱼₖ Γᵐⱼₖ [ċ]ⱼ [ċ]ₖ.
- Flat metric (G=I): ∂G=0 → Γ=0 → c̈=0 → straight-line geodesics.
- BVP: c(0)=x₁, c(1)=x₂ (parametrize over [0,1]) selects unique geodesic.
- IVP: c(0)=x₀, ċ(0)=v selects unique geodesic.
- [Q 6.3] Did not see how a double sum factors into two independent single sums when the summand factors by index — Revisit: if summand = f(j)·g(k) (j-stuff times k-stuff, no cross-terms), then Σⱼₖ f(j)·g(k) = (Σⱼ f(j))·(Σₖ g(k)). Recognize ⟨c,ċ⟩ = Σₖ cₖ ċₖ and ‖ċ‖² = Σⱼ ċⱼ² as standard sum forms.
- [Q 6.3] Index gymnastics fatigue — Christoffel derivation requires several layered manipulations (diagonal G⁻¹, partial of G_{ij}, Σᵢ collapse via δ, double-sum factoring, δ_{jk} merge collapse, vectorization back from [c̈]ₘ) — Revisit: the structural pipeline (G → ∂G → Γ via Eq. 7.20 → ODE via Eq. 7.19 → vector form → BVP/IVP) is reusable; the per-step manipulation is rote once the rules in exercises.md §1–5 are memorized.
- [Q 6.3] Missed that the initial conditions $c(0)=0$, $\dot c(0)=v$ were given in the question — felt like they came from nowhere — Revisit: when a question says "geodesic starting at... with initial velocity..." those ARE the IVP boundary conditions. Read the question for $c(0)$, $\dot c(0)$ before plugging into the ODE.
- [Q 6.3] Confused indexed expression with product of values — wrote 2c_k as "2c₁ · 2c₂" — Revisit: an indexed expression like 2c_k is a SINGLE quantity parametrized by k (k=1 → 2c₁; k=2 → 2c₂). Keep k symbolic; do NOT enumerate-and-multiply.
- [Q 6.3] Tripped on what ∂/∂c_k means with multiple components — thought the derivative gave a product across k=1 and k=2 — Revisit: ∂/∂c_k means partial w.r.t. ONE component (others held constant). The k is a free index labeling which equation; one expression per k, not a product over all k.
- [Q 6.3] Component-form to vector-form transition was unclear — needed explicit unrolling to m=1, m=2 to see how the stack into a vector worked — Revisit: write [c̈]ₘ for each m=1,…,d, observe identical shape, stack the m-indexed pieces into vectors (ċₘ → ċ, cₘ → c) and let scalars (⟨c,ċ⟩, ‖ċ‖², s(c)) pull out unchanged.
- [Q 6.3] Mixed up prefactors: used 1/2 instead of 1/s after the factor of 2 had been pulled out of Eq. 7.20 — Revisit: track which version of Γ you are using. Eq. 7.20 raw has 1/(2s); after pulling out the 2 from inside the parens, the prefactor becomes 1/s. Do not lose factors during substitution.
