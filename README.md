# HARP-VLA project website

[![Project Page](https://img.shields.io/badge/Project-Page-blue)](https://puzhenyuan.github.io/HARP-VLA-website/) [![arXiv](https://img.shields.io/badge/arXiv-2605.31234-b31b1b)](https://arxiv.org/abs/2605.31234) [![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Checkpoint-yellow)](https://huggingface.co/ypz21/HARP_VLA_calvin) [![Code](https://img.shields.io/badge/GitHub-Code-181717?logo=github)](https://github.com/PuzhenYuan/HARP-VLA)

Static project page with paper figures, redrawn result charts, 25 CALVIN clips (five sequences × five steps), and three real-world demonstrations per task with camera switching.

## Local preview

```bash
python -m http.server 8000
```

Open http://localhost:8000. No build system or external CDN is required.

`results.json` transcribes Tables 1–6 of the supplied paper. `media.json` describes the displayed demonstrations. Result SVGs are generated from these paper values. The gallery uses the five supplied successful sequences.

GitHub Pages publishes the root of the `main` branch at https://puzhenyuan.github.io/HARP-VLA-website/ The source repository remains private.

To regenerate the result charts, install `matplotlib` and run `python scripts/render_charts.py`.
