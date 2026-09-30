"""Render paired-data scaling from the supplied experiment results."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, FixedFormatter, NullLocator

fractions = [0, 1, 5, 25, 100]
positions = list(range(len(fractions)))
visual = [10.27, 68.26, 72.95, 77.36, 78.50]
latent = [5.73, 13.105, 24.40, 28.43, 36.29]
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11, "svg.fonttype": "none", "axes.spines.top": False})
fig, left = plt.subplots(figsize=(7.1, 4.6), facecolor="white")
right = left.twinx()
blue, orange = "#287bb5", "#cc762f"
left.set_xlim(-.25, 4.25)
left.set_ylim(0, 100); right.set_ylim(0, 40)
left.set_yticks([0, 20, 40, 60, 80, 100]); right.set_yticks([0, 10, 20, 30, 40])
left.xaxis.set_major_locator(FixedLocator(positions))
left.xaxis.set_major_formatter(FixedFormatter(["0", "1", "5", "25", "100"]))
left.xaxis.set_minor_locator(NullLocator())
left.set_xlabel("Paired data fraction (%)", labelpad=12)
left.set_ylabel("Visual avg R@1 (%)", color=blue, labelpad=10)
right.set_ylabel("Latent action avg R@1 (%)", color=orange, labelpad=10)
left.tick_params(axis="y", colors=blue); right.tick_params(axis="y", colors=orange)
left.tick_params(axis="x", length=0, pad=8, colors="#586b7c")
left.grid(axis="y", color="#e4eaf0", linewidth=.8)
left.set_axisbelow(True)
a, = left.plot(positions, visual, color=blue, lw=2.5, marker="o", markersize=6, label="Visual")
b, = right.plot(positions, latent, color=orange, lw=2.5, marker="s", markersize=5.5, label="Latent action")
for ax, values, color, dy in [(left, visual, blue, 10), (right, latent, orange, -19)]:
 for x, y in zip(positions, values):
  offset = (-19 if ax is left else 10) if x in [0, 4] else dy
  label = "13.105" if y == 13.105 else f"{y:.2f}"
  ax.annotate(label, (x, y), xytext=(4 if x==0 else 0, offset), textcoords="offset points", ha="left" if x==0 else "center", fontsize=9, color=color)
for ax in [left, right]:
 for spine in ax.spines.values(): spine.set_color("#d8e2ea")
 ax.spines["top"].set_visible(False)
fig.legend(handles=[a,b], loc="upper center", ncol=2, frameon=False, bbox_to_anchor=(.5,1.0))
fig.subplots_adjust(left=.12, right=.87, bottom=.19, top=.86)
out=Path(__file__).resolve().parents[1]/"assets"
fig.savefig(out/"paired-data-scaling.svg", metadata={"Date": None})
fig.savefig(out/"paired-data-scaling.png", dpi=180)

svg = out / "paired-data-scaling.svg"
svg.write_text("\n".join(line.rstrip() for line in svg.read_text().splitlines()) + "\n")
