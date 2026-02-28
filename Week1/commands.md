# Week 1 Commands

## Training with Gaussian Prior (Binary MNIST + Bernoulli Decoder)
```bash
uv run Week1/vae.py train normal --dataset binary --decoder bernoulli --device cpu --latent-dim 10 --epochs 5 --batch-size 128 --model Week1/ckpts/model.pt
```

## Training with Gaussian Prior (Continuous MNIST + Multivariate Gaussian Decoder)
```bash
uv run Week1/vae.py train normal --dataset continuous --decoder gaussian --device cpu --latent-dim 10 --epochs 5 --batch-size 128 --model Week1/ckpts/model_gaussian.pt
```

## Training with Mixture of Gaussians Prior
```bash
uv run Week1/vae.py train mixture --dataset binary --decoder bernoulli --device cpu --latent-dim 10 --epochs 5 --batch-size 128 --model Week1/ckpts/model_mog.pt
```

## Sampling
```bash
uv run Week1/vae.py sample normal --dataset binary --decoder bernoulli --device cpu --latent-dim 10 --model Week1/ckpts/model.pt --samples Week1/samples/samples.png
```

## Evaluation
```bash
uv run Week1/vae.py eval normal --dataset binary --decoder bernoulli --device cpu --latent-dim 10 --model Week1/ckpts/model.pt
```

## Parameters
- `mode`: `train`, `sample`, or `eval` - Operation mode (default: train)
- `prior`: `normal` or `mixture` - Prior distribution type (default: normal)
- `--dataset`: `binary` or `continuous` - MNIST dataset type: binary (thresholded at 0.5) or continuous (raw pixel values) (default: binary)
- `--decoder`: `bernoulli` or `gaussian` - Decoder type: bernoulli (for binary data) or gaussian (multivariate for continuous data) (default: bernoulli)
- `--device`: `cpu`, `cuda`, `mps` - Torch device (default: cpu)
- `--latent-dim`: Latent space dimension (default: 32)
- `--epochs`: Training epochs (default: 10)
- `--batch-size`: Batch size (default: 32)
- `--model`: Model checkpoint path (default: model.pt)
- `--samples`: Output samples path (default: samples.png)
