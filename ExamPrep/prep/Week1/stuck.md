# Week 1 — Stuck Points

- [Q 1.1] Unsure how to write the log-likelihood from the marginal p(x) = 𝒩(x | b, C) — didn't recall the general multivariate-Gaussian log-density. Revisit: log pdf of 𝒩(x | μ, Σ) and its constant/quadratic/log-det decomposition.
- [Q 1.1] After being given the Gaussian log-pdf template, still substituted symbolically (`ln p(xₙ | b, WWᵀ+σ²I)`) instead of expanding into constant + log-det + quadratic. Revisit: "expand" means write the three explicit pieces, not just rename the distribution.
- [Q 1.1] Tried scalar chain rule on ∂/∂b of (xₙ−b)ᵀ C⁻¹ (xₙ−b). Forgot the exercise's own hint = matrix-calculus identity ∂/∂b (x−b)ᵀW(x−b) = −2W(x−b) for symmetric W. Drill: when you see (·)ᵀ M (·), reach for matrix-calculus identities (Petersen-Pedersen cookbook), not chain rule.
- [Q 1.1] After ∂/∂b of one summand → C⁻¹(xₙ−b), dropped Σₙ and concluded C⁻¹ = 0. Two errors: (i) the sum stays from the iid log-likelihood; (ii) when A is invertible and Av = 0, conclude v = 0 (not A = 0). Drill: positive-definite covariance ⇒ invertible ⇒ kernel trivial.

- [Q 1.2] Did not recall the definition of KL divergence. Drill: KL[q‖p] = ∫ q(z) ln(q(z)/p(z)) dz = 𝔼_{z∼q}[ln(q(z)/p(z))]. It's an expectation **under q** of the **log ratio q/p** (q on top because the divergence is asymmetric and we measure deviation of q from p).
- [Q 1.2] Did not recall the univariate Gaussian log-pdf. Drill: ln 𝒩(z|μ,σ²) = −½ ln(2π) − ln σ − (z−μ)²/(2σ²). One-dim case of the multivariate formula (Q1.1).
- [Q 1.2] Confused E_q[(z−μ₁)²] (= σ₁², variance) with E_q[(z−μ₂)²] (= σ₁² + (μ₁−μ₂)², variance + squared bias). Drill: when z ~ q has mean μ₁, subtracting μ₁ gives plain variance; subtracting any other point μ₂ gives variance + (μ₁−μ₂)² (bias-variance identity).
- [Q 1.2] Confused E_q[z] with E_q[z²] for z ~ 𝒩(μ₁, σ₁²). Drill: E[z] = μ₁ only (mean — variance doesn't enter); E[z²] = σ₁² + μ₁² (second moment — variance + mean²). Variance only enters when you square z, because squaring amplifies spread. Concrete: z ~ 𝒩(10, 4) ⇒ E[z]=10, E[z²]=104.
- [Q 1.3] Confused ln p(x) with ELBO. Drill: ln p(x) ≥ ELBO(x); gap = KL[q(z|x) ‖ p(z|x)] (KL to **true posterior**, not prior). Equality only when q matches the true posterior. ELBO = "Evidence Lower BOund".
- [Q 1.2] Sign-flip when subtracting a log-pdf: writing `ln q − ln p` where both expand to `−½ ln(2πσ²) − …` produces `−½ ln(2πσ₁²) + ½ ln(2πσ₂²) − (z−μ₁)²/(2σ₁²) + (z−μ₂)²/(2σ₂²)` — the minus distributes into a plus. Got this wrong twice before fixing. Drill: minus-of-minus = plus. Write parentheses first, distribute second.
- [Q 1.2] Combining two log terms into a ratio + ½-cancellation: `½ ln(2πσ₂²) − ½ ln(2πσ₁²) = ½ ln(2πσ₂²/2πσ₁²) = ½ ln(σ₂²/σ₁²) = ln(σ₂/σ₁)`. Final simplification stuck on this. Drill: `½ ln(a²/b²) = ln(a/b)`; cancel common factors (here 2π) before rewriting.

- [Q 1.3] Jensen's inequality conditions: convex φ ⇒ φ(E[X]) ≤ E[φ(X)]; concave φ ⇒ flips to ≥. For ELBO, φ = ln is concave (2nd derivative −1/x² < 0). Equality iff X constant a.s. under the averaging measure (or φ linear). For ELBO equality: requires p(x,z)/q(z|x) constant in z ⇒ q(z|x) ∝ p(x,z) ⇒ q = true posterior p(z|x).
- [Q 1.3] "Doesn't depend on z₂" ≠ "drop the term from the expectation". Drill: every term inside E_Q is averaged under Q. If the term has no z₂, the inner ∫q(z₂|z₁)dz₂ = 1, so E_Q **collapses to** E_{q(z₁|x)} — but the term *stays*. Same rule in reverse: E_{q(z₁|x)}[f(z₁)] = E_Q[f(z₁)] **for free** (no integrand change) — used to rebundle Form 1 → eq (5.82).
- [Q 1.3] Term-grouping before scope reduction: split the ELBO integrand `ln(p(x|z₁) p(z₁|z₂) p(z₂) / q(z₂|z₁) q(z₁|x))` into 3 natural groups by variable-dependence: (A) z₁-only `ln p(x|z₁)`, (B) both `ln(q(z₁|x)/p(z₁|z₂))`, (C) z₂-given-z₁ `ln(q(z₂|z₁)/p(z₂))`. Then apply per-group: A collapses to E_{q(z₁|x)}, B stays E_Q, C → factor Q = q(z₁|x)·q(z₂|z₁), inner z₂ integral = KL.
- [Q 1.3] KL-spotting pattern: `∫ q(z₂|z₁) ln(q(z₂|z₁)/p(z₂)) dz₂` (density·log-ratio integrated over the variable) **is** KL[q(z₂|z₁) ‖ p(z₂)] by definition. Whenever you see this pattern inside a larger expectation, name it as a KL — don't re-derive.

## Q1.1 — recap (drill targets)
- Multivariate Gaussian log-pdf (memorize): `ln 𝒩(x|μ,Σ) = −(D/2)ln(2π) − (1/2)ln|Σ| − (1/2)(x−μ)ᵀΣ⁻¹(x−μ)`. Three pieces: const + log-det + quadratic. Reused for σ² and W.
- Linear-Gaussian → marginal stays Gaussian (eq 5.5 → 5.6). C := WWᵀ + σ²I = low-rank + isotropic noise (PPCA signature).
- iid product → sum of logs: ln ∏ₙ p(xₙ) = Σₙ ln p(xₙ). Σₙ stays until ∂/∂b kills non-b terms.
- Why Σ ambiguous: same glyph for summation and covariance. Rename covariance C to free up Σ.
- ML for Gaussian mean = sample mean whenever covariance doesn't depend on the mean. Generalises beyond PPCA.

## Q1.2 — recap (drill targets)
- KL definition (memorize): `KL[q‖p] = ∫ q(z) ln(q(z)/p(z)) dz = 𝔼_{z∼q}[ln q(z) − ln p(z)]`. Average under q, log-ratio q/p, asymmetric.
- Univariate Gaussian log-pdf (memorize): `ln 𝒩(z|μ,σ²) = −½ ln(2π) − ln σ − (z−μ)²/(2σ²)`. One-dim case.
- For z ~ q = 𝒩(μ₁, σ₁²): E_q[z] = μ₁; E_q[z²] = σ₁² + μ₁²; E_q[(z−μ₁)²] = σ₁² (variance); E_q[(z−μ₂)²] = σ₁² + (μ₁−μ₂)² (variance + squared bias).
- Strategy: substitute univariate log-pdfs into KL definition → distribute minus → linearity of E (constants out, quadratics take E) → plug variance identities → combine logs into ratio → simplify.
- Closed-form result: `KL[𝒩(μ₁,σ₁²)‖𝒩(μ₂,σ₂²)] = ln(σ₂/σ₁) + (σ₁² + (μ₁−μ₂)²)/(2σ₂²) − ½`. Generalises to multivariate (use trace and log-det).

## Q1.3 — recap (drill targets)
- ELBO is a **lower bound** on ln p(x). Gap = KL[q(z|x) ‖ p(z|x)] to the **true posterior**.
- ELBO derivation move (memorize): multiply-and-divide by q (or Q) inside the integral, recognise `∫ Q·f = E_Q[f]`, apply Jensen (concave ln flips ≥). Universal across vanilla / amortized / hierarchical VAEs.
- Hierarchical VAE recipe: bottom-up Q(z₁,z₂|x) = q(z₁|x)·q(z₂|z₁). Same multiply-divide-Jensen trick; difference is the joint Q over (z₁, z₂).
- Two equivalent ELBO forms for two-level VAE: **Form 1** has 3 terms each with their minimal-scope expectation (reconstruction under q(z₁|x), middle ratio under Q, KL under q(z₁|x)). **Form 2 (eq 5.82)** bundles everything under one E_Q. Free conversion both ways because integrands without z₂ are scope-invariant.
- Pattern reuse: any nested expectation of `density · log(density/other)` collapses to a KL — name it, don't re-derive.
