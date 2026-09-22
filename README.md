# HARP-VLA project website

[Code](https://github.com/PuzhenYuan/HARP-VLA) · [Checkpoint](https://huggingface.co/ypz21/HARP_VLA_calvin) · [Project website](https://puzhenyuan.github.io/HARP-VLA-website/)

Static project page with paper figures, redrawn result charts, 25 CALVIN clips (five sequences × five steps), and three real-world demonstrations per task with camera switching.

## Local preview

```bash
python -m http.server 8000
```

Open http://localhost:8000. No build system or external CDN is required.

`results.json` transcribes Tables 1–6 of the supplied paper. `media.json` describes the displayed demonstrations. Result SVGs are generated from these paper values. The gallery uses the five supplied successful sequences.

GitHub Pages publishes the root of the `main` branch at https://puzhenyuan.github.io/HARP-VLA-website/ The source repository remains private.

To regenerate the result charts, install `matplotlib` and run `python scripts/render_charts.py`.
