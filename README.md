# tool-mofa2

Explores trained MOFA models and exports latent factors, feature weights, and ranked features.

## Runtime inputs

Supply the trained model at `data/models/pbmc10k.hdf5` before running the exporter.

## Inputs and outputs

### Inputs

No fields are declared.

### Outputs

| Name | Type | Description |
| --- | --- | --- |
| `factors` | CSV | Exported factor matrix (Z). |
| `weights` | CSV | Exported weights/loadings matrix (W). |
| `top_features` | CSV | Ranked top features per factor based on absolute weight. |
| `report` | HTML | HTML summary report of the explored model. |
| `weights_plot` | IMAGE | PNG heatmap of MOFA weights. |

## Configuration

| Name | Default | Description |
| --- | --- | --- |
| `n_top_features` | `20` | Number of top absolute-weight features to export per factor. |
| `export_weights` | `True` | Export the factor loadings matrix. |
| `export_factors` | `True` | Export the factor values matrix. |
| `export_top_features` | `True` | Export ranked top features per factor. |

## Development

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
cp .env.example .env
# Set APP_ID and platform URLs before connecting.
python main.py
```

The Docker base image provides the FL-Net API. `requirements.txt` lists additional
runtime dependencies; `requirements-dev.txt` includes the API for local development.
Runtime datasets and trained models must be supplied separately; see `data/README.md`.

Build with `docker build -t tool-mofa2 .`.
