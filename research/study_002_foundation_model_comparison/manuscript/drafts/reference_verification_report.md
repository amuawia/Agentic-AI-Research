# Study 002 Reference Verification Report

This public-safe report documents the reference-verification pass performed before creating `study002_manuscript_v02.md`.

## Verification approach

- Started from `study002_manuscript_v01_2.md`.
- Checked whether all IEEE citation markers have matching reference entries.
- Checked whether all reference entries are cited in the manuscript.
- Used Crossref metadata lookup as a supporting check, but did not blindly accept noisy Crossref matches.
- Added DOI metadata only where the match was high-confidence from exact title/known source.

## Verified additions in v02

- [13] Park et al., “Generative Agents: Interactive Simulacra of Human Behavior” — DOI added: `10.1145/3586183.3606763`.
- [20] Kamoi et al., “When Can LLMs Actually Correct Their Own Mistakes?” — DOI added: `10.1162/tacl_a_00713`.
- [26] Strubell et al., “Energy and Policy Considerations for Deep Learning in NLP” — DOI added: `10.18653/v1/P19-1355`.
- [28] Ali (2026) Study 001 Zenodo DOI retained: `10.5281/zenodo.20606084`.

## Notes

Many AI/LLM references in the manuscript are arXiv, OpenReview, conference, technical-report, or model-card sources. Crossref returned noisy or unrelated matches for several titles, so DOI fields were not added unless the match was reliable. This avoids introducing incorrect DOI metadata into the public manuscript.

## Remaining pre-submission checks

Before final journal submission, check the selected venue's required reference format and replace arXiv/preprint entries with formal venue metadata where available.
