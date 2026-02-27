# Week 1 Commands

## Training with Gaussian Prior
```bash
uv run Week1/vae_bernoulli.py train normal --device cpu --latent-dim 10 --epochs 5 --batch-size 128 --model Week1/ckpts/model.pt
```

## Training with Mixture of Gaussians Prior
```bash
uv run Week1/vae_bernoulli.py train mixture --device cpu --latent-dim 10 --epochs 5 --batch-size 128 --model Week1/ckpts/model_mog.pt
```

## Sampling
```bash
uv run Week1/vae_bernoulli.py sample normal --device cpu --latent-dim 10 --model Week1/ckpts/model.pt --samples Week1/samples/samples.png
```

## Evaluation
```bash
uv run Week1/vae_bernoulli.py eval normal --device cpu --latent-dim 10 --model Week1/ckpts/model.pt
```

## Parameters
- `prior`: `normal` or `mixture` - Prior distribution type (default: normal)
- `--device`: cpu, cuda, mps (default: cpu)
- `--latent-dim`: Latent space dimension (default: 32)
- `--epochs`: Training epochs (default: 10)
- `--batch-size`: Batch size (default: 32)
- `--model`: Model checkpoint path (default: model.pt)
- `--samples`: Output samples path (default: samples.png)
