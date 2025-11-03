# Adaptive Coherence Framework (ACF v1.3 RC-B)

**Research preprint and reference implementation for decentralized stability in multi‑agent systems.**

**DOI:** [10.5281/zenodo.17515313](https://doi.org/10.5281/zenodo.17515313)  
**Preprint:** [`/docs/ACF_v1.3_RCB_Preprint.pdf`](docs/ACF_v1.3_RCB_Preprint.pdf)  
**License:** CC‑BY‑4.0

## Abstract
ACF v1.3 models adaptive oscillator coupling with state‑dependent feedback laws. It introduces five stabilizing mechanisms — refractory gating, grace damping, adaptive sensitivity, stochastic coupling, and weak long‑range bridging — that jointly sustain coherence under adversarial stress. Tested across four stress regimes (noise, whiplash, over‑coupling, fragmentation), ACF reduces collapse frequency by ≈6.5× relative to the unpatched baseline.

## Contributors
- Domagoj Kobeščak (Author)  
- Lexy The VoidCat (AI collaborative system)  
- Grok LLM, Claude 3.5, Anima Pro Cluster (contributors)

## Quick Start (illustrative)
```bash
python acf_core.py --demo
```

## Files
- `acf_core.py` — minimal, commented skeleton of the five stabilizers.  
- `acf_validation.csv` — example metrics table used in the preprint.  
- `docs/ACF_v1.3_RCB_Preprint.pdf` — archived preprint corresponding to the DOI.

## Citation
If you use this work, please cite:
```
Kobeščak, D. (2025). Adaptive Coherence Framework (ACF v1.3 RC-B). Zenodo. https://doi.org/10.5281/zenodo.17515313
```

---
GitHub: https://github.com/bloodtemplar1337/Adaptive-Coherence-Framework  
Zenodo: https://doi.org/10.5281/zenodo.17515313
