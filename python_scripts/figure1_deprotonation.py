
import numpy as np
import matplotlib.pyplot as plt

labels = ["Baseline","dep01","dep025","dep035","dep045","dep075","dep10"]
rg     = [0.7950, 0.8657, 0.7662, 0.9200, 0.7746, 0.8226, 1.1698]
sasa   = [18.42,  19.51,  18.65,  19.79,  16.82,  18.62,  20.08]
deprot = [0, 1, 2.5, 3.5, 4.5, 7.5, 10]

drg   = [(r - rg[0])/rg[0]*100 for r in rg]
dsasa = [(s - sasa[0])/sasa[0]*100 for s in sasa]

fig, axes = plt.subplots(2, 2, figsize=(11, 9))
fig.suptitle("Figure 1. Conformational Response of Eudragit L100 to Progressive MAA Deprotonation",
             fontsize=12, fontweight="bold")

ax = axes[0,0]
sc = ax.scatter(deprot, rg, c=rg, cmap="coolwarm", s=100, zorder=3)
ax.plot(deprot, rg, "k--", lw=0.8, alpha=0.5)
for i, lbl in enumerate(labels):
    ax.annotate(lbl, (deprot[i], rg[i]), textcoords="offset points", xytext=(5,4), fontsize=7)
ax.set_xlabel("MAA Deprotonation Level (%)")
ax.set_ylabel("Radius of Gyration (nm)")
ax.set_title("(A) Radius of Gyration vs. Deprotonation Level", fontweight="bold")
plt.colorbar(sc, ax=ax, label="Rg (nm)")

ax = axes[0,1]
sc2 = ax.scatter(deprot, sasa, c=sasa, cmap="coolwarm", s=100, zorder=3)
ax.plot(deprot, sasa, "k--", lw=0.8, alpha=0.5)
for i, lbl in enumerate(labels):
    ax.annotate(lbl, (deprot[i], sasa[i]), textcoords="offset points", xytext=(5,4), fontsize=7)
ax.set_xlabel("MAA Deprotonation Level (%)")
ax.set_ylabel("SASA (nm^2)")
ax.set_title("(B) SASA vs. Deprotonation Level", fontweight="bold")
plt.colorbar(sc2, ax=ax, label="SASA (nm^2)")

ax = axes[1,0]
x = np.arange(len(labels))
w = 0.35
ax.bar(x - w/2, drg,   w, label="DRg (%)",   color="#4C72B0", edgecolor="black")
ax.bar(x + w/2, dsasa, w, label="DSASA (%)", color="#DD8452", edgecolor="black")
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=20, fontsize=8)
ax.set_ylabel("Change from Baseline (%)")
ax.set_title("(C) Relative Changes from Baseline", fontweight="bold")
ax.legend()
ax.axhline(0, color="black", lw=0.8)

ax = axes[1,1]
sc3 = ax.scatter(rg, sasa, c=deprot, cmap="viridis", s=100, zorder=3)
for i, lbl in enumerate(labels):
    ax.annotate(lbl, (rg[i], sasa[i]), textcoords="offset points", xytext=(5,4), fontsize=7)
m, b = np.polyfit(rg, sasa, 1)
xfit = np.linspace(min(rg), max(rg), 100)
ax.plot(xfit, m*xfit + b, "r--", lw=1.2, label="Linear fit")
ax.set_xlabel("Radius of Gyration (nm)")
ax.set_ylabel("SASA (nm^2)")
ax.set_title("(D) Rg-SASA Correlation (r = 0.720)", fontweight="bold")
plt.colorbar(sc3, ax=ax, label="Deprotonation (%)")

plt.tight_layout()
plt.savefig("figure1_deprotonation.png", dpi=300, bbox_inches="tight")
print("Saved: figure1_deprotonation.png")
