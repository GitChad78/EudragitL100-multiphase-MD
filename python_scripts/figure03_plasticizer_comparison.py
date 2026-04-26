
import numpy as np
import matplotlib.pyplot as plt

labels   = ["L100 + PEG400", "L100 + TEC"]
energy   = [-36119.6, -37940.7]
energy_e = [313.5, 313.5]
rg       = [2.177, 2.187]
rg_e     = [0.009, 0.009]
hbonds   = [303.7, 2.1]
density  = [798.6, 795.0]
density_e= [5.7, 5.7]
colors   = ["#4C72B0", "#DD8452"]

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle("Figure 3. MD Simulation Comparison of PEG400 and TEC as Plasticizers for Eudragit L100 (50 ns)",
             fontsize=12, fontweight="bold")

ax = axes[0,0]
bars = ax.bar(labels, energy, yerr=energy_e, capsize=5, color=colors, edgecolor="black", width=0.5)
ax.set_title("(A) System Potential Energy", fontweight="bold")
ax.set_ylabel("Potential Energy (kJ/mol)")
for bar, val in zip(bars, energy):
    ax.text(bar.get_x()+bar.get_width()/2, val-400, f"{val:,.1f}",
            ha="center", va="top", fontsize=9, fontweight="bold", color="white")
ax.annotate("", xy=(1,-37500), xytext=(0,-37500),
            arrowprops=dict(arrowstyle="<->", color="red", lw=1.5))
ax.text(0.5, -37300, "dE = 1821 kJ/mol", ha="center", fontsize=8, color="red")

ax = axes[0,1]
bars = ax.bar(labels, rg, yerr=rg_e, capsize=5, color=colors, edgecolor="black", width=0.5)
ax.set_title("(B) L100 Chain Radius of Gyration", fontweight="bold")
ax.set_ylabel("Radius of Gyration (nm)")
ax.set_ylim(2.10, 2.26)
for bar, val, err in zip(bars, rg, rg_e):
    ax.text(bar.get_x()+bar.get_width()/2, val+err+0.003,
            f"{val:.3f}+/-{err:.3f}", ha="center", fontsize=9, fontweight="bold")

ax = axes[1,0]
ax.bar(labels, hbonds, color=colors, edgecolor="black", width=0.5)
ax.set_yscale("log")
ax.set_title("(C) L100-Plasticizer Hydrogen Bonds", fontweight="bold")
ax.set_ylabel("Mean H-bonds per Frame")
ax.text(0.97, 0.95, "~145x difference", transform=ax.transAxes,
        ha="right", va="top", fontsize=9, color="green",
        bbox=dict(boxstyle="round", facecolor="lightgreen", alpha=0.5))
for i, val in enumerate(hbonds):
    ax.text(i, val*1.3, f"{val}", ha="center", fontsize=9, fontweight="bold")

ax = axes[1,1]
bars = ax.bar(labels, density, yerr=density_e, capsize=5, color=colors, edgecolor="black", width=0.5)
ax.set_title("(D) System Density (IPA Solution, 298 K)", fontweight="bold")
ax.set_ylabel("System Density (kg/m3)")
ax.set_ylim(780, 815)
for bar, val, err in zip(bars, density, density_e):
    ax.text(bar.get_x()+bar.get_width()/2, val+err+0.3,
            f"{val:.1f}+/-{err:.1f}", ha="center", fontsize=9, fontweight="bold")

plt.tight_layout()
plt.savefig("figure2_plasticizer_comparison.png", dpi=300, bbox_inches="tight")
print("Saved: figure2_plasticizer_comparison.png")
