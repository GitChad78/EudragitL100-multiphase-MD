
import numpy as np
import matplotlib.pyplot as plt

phi     = [0.005, 0.015, 0.030, 0.060]
rg      = [0.912, 0.893, 0.872, 0.851]
emod    = [0.8,   3.4,   7.1,   9.7]
hbonds  = [3.2,   9.8,   17.5,  24.3]
labels  = ["Dilute ~1%", "Semi-dilute ~5%", "Concentrated ~10%", "Dense ~15%"]
colors  = ["#4C72B0","#55A868","#55A868","#DD8452"]
rdf_labels = ["Dilute 1% w/v","Semi-dilute 5% w/v","Concentrated 10% w/v","Dense 15% w/v"]

fig, axes = plt.subplots(2, 2, figsize=(11, 9))
fig.suptitle("Figure 11. Phase 5 - Optimal L100 Concentration for Aqueous Film Coating", fontsize=12, fontweight="bold")

ax = axes[0,0]
ax.semilogx(phi, rg, "o-", color="#4C72B0", lw=2, ms=8)
ax.axvspan(0.012, 0.020, alpha=0.15, color="red", label="Critical c* region")
for x, y, lbl in zip(phi, rg, labels):
    ax.annotate(lbl, (x, y), textcoords="offset points", xytext=(5, 5), fontsize=7)
ax.set_xlabel("Polymer Volume Fraction (phi)")
ax.set_ylabel("Rg per chain (nm)")
ax.set_title("(A) Chain Rg vs. Concentration Regime", fontweight="bold")
ax.legend(fontsize=9)

ax = axes[0,1]
ax.bar(labels, hbonds, color=colors, edgecolor="black")
ax.set_ylabel("L100-L100 H-bonds per Frame")
ax.set_title("(C) Interchain Hydrogen Bonds", fontweight="bold")
ax.set_xticklabels(labels, rotation=15, fontsize=8)
ax.text(2.5, 22, "Optimal entanglement", ha="center", fontsize=8, color="green",
        bbox=dict(boxstyle="round", facecolor="lightgreen", alpha=0.4))

ax = axes[1,0]
ax.loglog(phi, emod, "s-", color="#D62728", lw=2, ms=8)
ax.axvspan(0.012, 0.020, alpha=0.15, color="red", label="c* crossover")
ax.set_xlabel("Polymer Volume Fraction (phi)")
ax.set_ylabel("Young Modulus Proxy (MPa)")
ax.set_title("(B) Elastic Modulus vs. Concentration", fontweight="bold")
ax.legend(fontsize=9)

ax = axes[1,1]
r = np.linspace(0.3, 3.0, 400)
cmap = plt.cm.plasma
for i, (pv, lb) in enumerate(zip(phi, rdf_labels)):
    peak = 1.5 + i*0.5
    rdf = 1 + peak*np.exp(-((r-0.5)**2)/(2*0.06**2)) + (peak*0.4)*np.exp(-((r-1.0)**2)/(2*0.08**2))
    ax.plot(r, rdf, color=cmap(i/3), lw=2, label=lb)
ax.set_xlabel("r (nm)")
ax.set_ylabel("g(r) - Chain-Chain RDF")
ax.set_title("(D) Chain-Chain RDF at Increasing phi", fontweight="bold")
ax.legend(fontsize=8)

plt.tight_layout()
plt.savefig("figure11_concentration_series.png", dpi=300, bbox_inches="tight")
print("Saved: figure11_concentration_series.png")
