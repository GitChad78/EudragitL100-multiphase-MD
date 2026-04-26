
import numpy as np
import matplotlib.pyplot as plt

tec_pct = [10, 20, 30, 40]
rg      = [0.862, 0.891, 0.920, 0.934]
msd     = [1.21,  0.98,  0.72,  1.09]
freevol = [8.2,   11.4,  14.8,  16.3]
hbonds  = [1.2,   1.8,   2.1,   2.4]

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle("Figure 5. Phase 1 - TEC Plasticizer Concentration on L100 Properties", fontsize=12, fontweight="bold")

ax = axes[0,0]
ax.plot(tec_pct, rg, "o-", color="#4C72B0", lw=2, ms=8)
ax.axvspan(27, 33, alpha=0.15, color="green", label="Optimal 30%")
ax.axvline(30, color="red", lw=1.5, linestyle="--")
ax.set_xlabel("TEC Concentration (% w/w)")
ax.set_ylabel("Rg of L100 (nm)")
ax.set_title("(A) L100 Chain Expansion with TEC", fontweight="bold")
ax.legend(fontsize=9)

ax = axes[0,1]
bar_colors = ["#DD8452","#DD8452","#55A868","#DD8452"]
ax.bar(tec_pct, msd, color=bar_colors, edgecolor="black", width=6)
ax.axvline(30, color="red", lw=1.5, linestyle="--", label="Optimal: lowest mobility")
ax.set_xlabel("TEC Concentration (% w/w)")
ax.set_ylabel("TEC MSD (nm^2/ns)")
ax.set_title("(B) TEC Plasticizer Mobility (MSD)", fontweight="bold")
ax.legend(fontsize=9)

ax = axes[1,0]
ax.fill_between(tec_pct, freevol, alpha=0.3, color="teal")
ax.plot(tec_pct, freevol, "s-", color="teal", lw=2, ms=8)
ax.axvline(30, color="red", lw=1.5, linestyle="--")
ax.annotate("Optimal at 30%", xy=(30, 14.8), xytext=(32, 13), fontsize=8, color="red", arrowprops=dict(arrowstyle="->", color="red"))
ax.set_xlabel("TEC Concentration (% w/w)")
ax.set_ylabel("Free Volume (%)")
ax.set_title("(C) Free Volume Increase with TEC", fontweight="bold")

ax = axes[1,1]
ax.bar(tec_pct, hbonds, color=["#9467BD"]*4, edgecolor="black", width=6)
ax.axvline(30, color="red", lw=1.5, linestyle="--")
ax.set_xlabel("TEC Concentration (% w/w)")
ax.set_ylabel("TEC-COO- H-bonds per Frame")
ax.set_title("(D) TEC-Carboxylate Interactions", fontweight="bold")

plt.tight_layout()
plt.savefig("figure05_TEC_concentration.png", dpi=300, bbox_inches="tight")
print("Saved: figure05_TEC_concentration.png")
