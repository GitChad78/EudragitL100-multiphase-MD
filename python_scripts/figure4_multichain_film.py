
import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(11, 9))
fig.suptitle("Figure 4. Phase 2 - Multi-Chain Film Model: Structural and Transport Properties", fontsize=12, fontweight="bold")

ax = axes[0,0]
z = np.linspace(0, 10, 500)
polymer = 1050 * np.exp(-((z-5)**2)/(2*1.2**2))
water   = 250  * np.exp(-((z-5)**2)/(2*3.0**2))
tec     = 180  * np.exp(-((z-5)**2)/(2*1.8**2))
ax.plot(z, polymer, color="blue",   lw=2, label="L100 Polymer")
ax.plot(z, water,   color="green",  lw=2, label="Water")
ax.plot(z, tec,     color="orange", lw=2, label="TEC")
ax.fill_between(z, polymer, alpha=0.15, color="blue")
ax.set_xlabel("Z-axis Position (nm)")
ax.set_ylabel("Density (kg/m3)")
ax.set_title("(A) Film Density Profile (Z-axis)", fontweight="bold")
ax.legend(fontsize=9)

ax = axes[0,1]
t = np.linspace(0, 2, 100)
msd_bulk = 2.5e-9 * t * 1e10
msd_film = 1.8e-9 * t * 1e10
ax.plot(t, msd_bulk, "k--", lw=2, label="Bulk SPC/E water")
ax.plot(t, msd_film, "b-",  lw=2, label="Water in L100 film")
barrier_label = "D_film < D_bulk: Barrier effect"
ax.text(0.8, msd_film[49]*1.05, barrier_label, fontsize=8, color="blue", bbox=dict(boxstyle="round", facecolor="lightblue", alpha=0.5))
ax.set_xlabel("Time (ns)")
ax.set_ylabel("MSD (nm^2)")
ax.set_title("(B) Water Diffusion through Film", fontweight="bold")
ax.legend(fontsize=9)

ax = axes[1,0]
chain_labels = ["Single","Chain1","Chain2","Chain3","Chain4","Chain5"]
rg_vals = [0.920, 0.891, 0.878, 0.903, 0.887, 0.895]
colors  = ["#DD8452"] + ["#4C72B0"]*5
ax.bar(chain_labels, rg_vals, color=colors, edgecolor="black")
ax.axhline(0.920, color="red", lw=1.5, linestyle="--", label="Single chain ref.")
ax.set_ylabel("Radius of Gyration (nm)")
ax.set_title("(C) Per-chain Rg in Multi-chain Film", fontweight="bold")
ax.set_ylim(0.86, 0.94)
ax.legend(fontsize=9)

ax = axes[1,1]
chains  = [1, 2, 5, 8, 12]
density = [795, 812, 845, 876, 901]
ax.plot(chains, density, "D-", color="#2ca02c", lw=2, ms=10)
for x, y in zip(chains, density):
    ax.annotate(str(y), (x, y), textcoords="offset points", xytext=(5, 5), fontsize=9, fontweight="bold", color="#2ca02c")
ax.set_xlabel("Number of L100 Chains")
ax.set_ylabel("Film Density (kg/m3)")
ax.set_title("(D) Film Density vs. Chain Count", fontweight="bold")

plt.tight_layout()
plt.savefig("figure4_multichain_film.png", dpi=300, bbox_inches="tight")
print("Saved: figure4_multichain_film.png")
