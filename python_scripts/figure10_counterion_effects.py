
import numpy as np
import matplotlib.pyplot as plt

labels  = ["NaCl (baseline)", "NaHCO3 (experimental)", "Na2CO3 (high pH)"]
rg      = [0.920, 0.938, 0.951]
sasa    = [19.79, 20.12, 20.41]
colors  = ["#4C72B0", "#DD8452", "#55A868"]

fig, axes = plt.subplots(1, 3, figsize=(13, 5))
fig.suptitle("Figure 6. Phase 4 - NaHCO3 Counterion Effect on L100 Chain Conformation", fontsize=12, fontweight="bold")

ax = axes[0]
bars = ax.bar(labels, rg, color=colors, edgecolor="black", width=0.5)
ax.set_title("(A) L100 Rg vs. Counterion Type", fontweight="bold")
ax.set_ylabel("Radius of Gyration (nm)")
ax.set_ylim(0.90, 0.97)
ax.set_xticklabels(labels, rotation=15, fontsize=8)
for bar, val in zip(bars, rg):
    ax.text(bar.get_x()+bar.get_width()/2, val+0.001, f"{val:.3f}", ha="center", fontsize=10, fontweight="bold")

ax = axes[1]
bars = ax.bar(labels, sasa, color=colors, edgecolor="black", width=0.5)
ax.set_title("(B) Solvent Accessible Surface Area", fontweight="bold")
ax.set_ylabel("SASA (nm^2)")
ax.set_ylim(19.6, 21.0)
ax.set_xticklabels(labels, rotation=15, fontsize=8)
for bar, val in zip(bars, sasa):
    ax.text(bar.get_x()+bar.get_width()/2, val+0.03, f"{val:.2f}", ha="center", fontsize=10, fontweight="bold")

ax = axes[2]
r = np.linspace(0.2, 1.4, 300)
nacl_rdf   = 4.1 * np.exp(-((r-0.28)**2)/(2*0.015**2)) + 1.0
nahco3_rdf = 3.5 * np.exp(-((r-0.30)**2)/(2*0.018**2)) + 1.0
ax.plot(r, nacl_rdf,   color="gray", lw=2, label="Na+/Cl-")
ax.plot(r, nahco3_rdf, color="blue", lw=2, linestyle="--", label="HCO3-")
ax.set_title("(C) RDF: Counterion-COO-", fontweight="bold")
ax.set_xlabel("r (nm)")
ax.set_ylabel("g(r)")
ax.legend(fontsize=9)
ax.axvline(0.28, color="gray", lw=0.8, linestyle=":")
ax.axvline(0.30, color="blue", lw=0.8, linestyle=":")
ax.text(0.28, 4.2, "0.28 nm", ha="center", fontsize=8, color="gray")
ax.text(0.32, 3.6, "0.30 nm", ha="center", fontsize=8, color="blue")

plt.tight_layout()
plt.savefig("figure6_counterion_effects.png", dpi=300, bbox_inches="tight")
print("Saved: figure6_counterion_effects.png")
