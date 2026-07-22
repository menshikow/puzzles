# Kaggle

[Kaggle](https://www.kaggle.com/) — Data science & machine learning competitions.

## Getting Started

1. Install the Kaggle CLI:
   ```bash
   pip install kaggle
   ```
2. Download your API token from `kaggle.com/<username>/account` → Create API Token → place `kaggle.json` in `~/.kaggle/`
3. Download competition data:
   ```bash
   kaggle competitions download -c <competition-name> -p kaggle/<competition-name>/data/
   ```

## Structure

```
kaggle/
  <competition-name>/
    sol.ipynb       # Solution notebook
    notes.md        # Approach, learnings, reflections
    data/           # Datasets (gitignored — download via Kaggle CLI)
```

## Conventions

- Solutions are **Jupyter notebooks** (`.ipynb`).
- Datasets go in `data/` and are **gitignored** (use Kaggle CLI to download).
- Each competition gets its own directory named after the Kaggle slug.
- Include a `notes.md` with feature engineering decisions, model choices, and key takeaways.
