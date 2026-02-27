# Week Commands Generator - Reference

## File Organization

- Root `commands.md`: Index linking to weekly commands
- `WeekN/commands.md`: Commands for that specific week (executed from root)

## Example Output

### Week1/commands.md Structure
```markdown
# Week 1 Commands

## Training
\`\`\`bash
uv run Week1/vae_bernoulli.py train --device cpu --latent-dim 10 --epochs 5 --batch-size 128 --model Week1/ckpts/model.pt
\`\`\`

## Sampling
\`\`\`bash
uv run Week1/vae_bernoulli.py sample --device cpu --latent-dim 10 --model Week1/ckpts/model.pt --samples Week1/samples/samples.png
\`\`\`

## Parameters
- `--device`: cpu, cuda, mps (default: cpu)
- `--latent-dim`: Latent space dimension (default: 32)
- `--epochs`: Training epochs (default: 10)
- `--batch-size`: Batch size (default: 32)
- `--model`: Model checkpoint path (default: model.pt)
- `--samples`: Output samples path (default: samples.png)
```

## Generation Rules

1. **One command per mode** - Show typical usage, not all variants
2. **Use relative paths from root** - e.g., `uv run WeekN/script.py`
3. **Parameters table only** - List main parameters with defaults, no prose
4. **Concise and practical** - Skip explanations, keep it scannable
5. **No custom variants** - Just show the primary use case

## Preservation

- Update `WeekN/commands.md` only, never modify root `commands.md` structure
- Root `commands.md` is just an index

