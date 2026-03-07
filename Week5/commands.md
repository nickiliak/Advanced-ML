# Week 5 Commands

## Generate VAE Checkpoint (from Week 1 model)

This command trains a VAE with 2D latent dimension for use in Exercise 5.6:

```bash
uv run Week1/vae.py train normal --dataset binary --decoder bernoulli --device cpu --latent-dim 2 --epochs 10 --batch-size 128 --model Week5/ckpts/model_2d.pt
```

## Outputs
- Models: `Week5/ckpts/`
- Notebooks: Jupyter notebooks (`evaluate_len_curve.ipynb`, `evaluate_vae_curve.py`)

## Notes
- Exercise 5.5: Use `evaluate_len_curve.ipynb` for basic curve length evaluation
- Exercise 5.6: Use `evaluate_vae_curve.py` (or notebook) with the 2D VAE model to compute latent vs output curve lengths
- `--latent-dim 2` is important for visualization and geometric exploration
