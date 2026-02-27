# Week 1 Commands

## Training
```bash
uv run Week1/vae_bernoulli.py train --device cpu --latent-dim 10 --epochs 5 --batch-size 128 --model Week1/ckpts/model.pt
```

## Sampling
```bash
uv run Week1/vae_bernoulli.py sample --device cpu --latent-dim 10 --model Week1/ckpts/model.pt --samples Week1/samples/samples.png
```

## Evaluation
```bash
uv run Week1/vae_bernoulli.py eval --device cpu --latent-dim 10 --model Week1/ckpts/model.pt
```

## Parameters
- `--device`: cpu, cuda, mps (default: cpu)
- `--latent-dim`: Latent space dimension (default: 32)
- `--epochs`: Training epochs (default: 10)
- `--batch-size`: Batch size (default: 32)
- `--model`: Model checkpoint path (default: model.pt)
- `--samples`: Output samples path (default: samples.png)
