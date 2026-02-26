# Advanced Machine Learning (02460)

DTU Course: Advanced Machine Learning

## Project Structure

```
Advanced-ML/
├── main.py
├── pyproject.toml
├── README.md
├── Projects/
│   └── Deep-Generative-Modeling/   # Submodule
├── Week1/
├── Week2/
└── Week3/
```

## Setup

1. Initialize submodules:
```bash
git submodule update --init --recursive
```

2. Install dependencies with `uv`:
```bash
uv sync
```

3. Run the project:
```bash
uv run python main.py
```
