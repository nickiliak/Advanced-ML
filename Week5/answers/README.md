# Week 5 - Manifold Learning & Latent Geometry

## Programming Exercises

### Question 5.5: Curve Length Evaluation

Consider the curve c:[0,1]→R² defined in Eq. 17.

1. Write a computer program that evaluates the length of the curve c using Eq. 4.2 in the LMLG book.
2. If you have completed exercise 5.3:
   - (a) Did the numerical and the analytical results agree?
   - (b) Use the analytic expression for ||ċt|| to write a computer program that evaluates the length of the curve using Eq. 4.5 in the LMLG book. Note that you need to approximate the integral with a sum.

**Answer:**

Yes, the numerical and analytical results agree. The computed curve length is approximately **2.29**. 

The implementation evaluates:
- **Part 1 (Numerical, Eq. 4.2)**: Using finite differences, computing differences between consecutive curve points and summing distances.
- **Part 2(b) (Analytical, Eq. 4.5)**: Using the analytical derivative norm and integrating with the trapezoidal rule.

Both methods converge to the same result, confirming the accuracy of our implementation. See `evaluate_len_curve.ipynb` for the full code.


### Question 5.6: VAE Latent Curve Length

Consider the Bernoulli VAE that you worked on in Week 1. Train this with a two-dimensional latent space (for ease of plotting).

1. Write a computer program that evaluates the length of any latent second-order polynomial curve c using Eq. 4.2 in the LMLG book. It is recommended that you write the code to support any callable curve c.

**Answer:**

<!-- Add your answer here -->
