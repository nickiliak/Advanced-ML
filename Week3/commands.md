# Week 3 Commands

## Train

### Toy Datasets
```bash
# Two Gaussians
uv run Week3/scripts/ddpm.py train --data tg --epochs 1 --batch-size 10000 --lr 1e-3 --device cpu --model Week3/ckpts/model.pt

# Chequerboard
uv run Week3/scripts/ddpm.py train --data cb --epochs 1 --batch-size 10000 --lr 1e-3 --device cpu --model Week3/ckpts/model_cb.pt
```

### MNIST
```bash
# MNIST with Fully Connected Network
uv run Week3/scripts/ddpm.py train --data mnist --network fc --epochs 1 --batch-size 128 --lr 1e-3 --device cpu --model Week3/ckpts/model_mnist_fc.pt

# MNIST with U-Net
uv run Week3/scripts/ddpm.py train --data mnist --network unet --epochs 1 --batch-size 128 --lr 1e-3 --device cpu --model Week3/ckpts/model_mnist_unet.pt
```

## Sample

### Toy Datasets
```bash
# Two Gaussians
uv run Week3/scripts/ddpm.py sample --data tg --model Week3/ckpts/model.pt --samples Week3/samples/samples.png --device cpu

# Chequerboard
uv run Week3/scripts/ddpm.py sample --data cb --model Week3/ckpts/model_cb.pt --samples Week3/samples/samples_cb.png --device cpu
```

### MNIST
```bash
# MNIST with Fully Connected Network
uv run Week3/scripts/ddpm.py sample --data mnist --network fc --model Week3/ckpts/model_mnist_fc.pt --samples Week3/samples/samples_mnist_fc.png --device cpu

# MNIST with U-Net
uv run Week3/scripts/ddpm.py sample --data mnist --network unet --model Week3/ckpts/model_mnist_unet.pt --samples Week3/samples/samples_mnist_unet.png --device cpu
```

## Outputs
- Training logs: `Week3/outputs/elbo.txt`
- Samples array (toy datasets): `Week3/outputs/samples.txt`
- Samples images (MNIST): `Week3/samples/samples_mnist_*.png`

## Parameters
- `mode`: what to do when running the script (`train`, `sample`, `test`) (default: `train`)
- `--data`: dataset to use {`tg`: two Gaussians, `cb`: chequerboard, `mnist`} (default: `tg`)
- `--network`: network architecture to use {`fc`: fully connected, `unet`} (default: `fc`)
- `--model`: file to save model to or load model from (default: `Week3/ckpts/model.pt`)
- `--samples`: file to save samples in (default: `Week3/samples/samples.png`)
- `--device`: torch device (`cpu`, `cuda`, `mps`) (default: `cpu`)
- `--batch-size`: batch size for training (default: `10000`)
- `--epochs`: number of epochs to train (default: `1`)
- `--lr`: learning rate for training (default: `1e-3`)
