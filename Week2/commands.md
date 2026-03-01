# Week 2 Commands

## Train
```bash
uv run Week2/flow.py train --epochs 100 --batch-size 10000 --lr 1e-3 --data tg --model Week2/ckpts/flow_model.pt --device cpu
```

## Sample
```bash
uv run Week2/flow.py sample --model Week2/ckpts/flow_model.pt --samples Week2/samples/flow_samples.png --data tg --device cpu
```

## Parameters
- `--data`: toy dataset to use {`tg`: two Gaussians, `cb`: chequerboard} (default: `tg`)
- `--model`: file to save model to or load model from (default: `model.pt`)
- `--samples`: file to save samples in (default: `samples.png`)
- `--device`: torch device {`cpu`, `cuda`, `mps`} (default: `cpu`)
- `--batch-size`: batch size for training (default: `10000`)
- `--epochs`: number of epochs to train (default: `1`)
- `--lr`: learning rate for training (default: `1e-3`)
