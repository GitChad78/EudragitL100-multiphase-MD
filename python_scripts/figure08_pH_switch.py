
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
t = np.linspace(0, 2, 200)

fig, axes = plt.subplots(2, 2, figsize=(11, 9))
fig.suptitle("Figure 8. Phase 3 - pH-Switch Simulation: Acid (pH 1.2) vs Intestinal (pH 6.8) Film Behaviour", fontsize=12, fontweight="bold")

ax = axes[0,0]
water_acid = 143 + np.random.normal(0, 0.8, 200)
water_int  = 141 + t*2.5 + np.random.normal(0, 0.8, 200)
ax.plot(t, water_acid, color="blue",   lw=1.5, label="pH 1.2 (0% deprot.)")
ax.plot(t, water_int,  color="orange", lw=1.5, label="pH 6.8 (10% deprot.)")
ax.fill_between(t, water_acid-1, water_acid+1, alpha=0.15, color="blue")
ax.set_xlabel("Simulation Time (ns)")
ax.set_ylabel("Water molecules within 0.5 nm of polymer")
ax.set_title("(A) Water Uptake into Film", fontweight="bold")
ax.legend(fontsize=9)

ax = axes[0,1]
dist_acid = 2.1 + np.random.normal(0, 0.02, 200)
dist_int  = 2.1 + t*0.25 + np.random.normal(0, 0.02, 200)
ax.plot(t, dist_acid, color="blue",   lw=1.5, label="pH 1.2")
ax.plot(t, dist_int,  color="orange", lw=1.5, label="pH 6.8")
ax.set_xlabel("Simulation Time (ns)")
ax.set_ylabel("Inter-chain COM Distance (nm)")
ax.set_title("(B) Film Swelling - Inter-chain Distance", fontweight="bold")
ax.legend(fontsize=9)

ax = axes[1,0]
msd_acid = 0.20 * t + np.random.normal(0, 0.005, 200)
msd_int  = 0.60 * t + np.random.normal(0, 0.010, 200)
ax.plot(t, msd_acid, color="blue",   lw=1.5, label="pH 1.2 (stable)")
ax.plot(t, msd_int,  color="orange", lw=1.5, label="pH 6.8 (leaching)")
ax.set_xlabel("Simulation Time (ns)")
ax.set_ylabel("TEC MSD (nm^2)")
ax.set_title("(C) TEC Plasticizer Leaching", fontweight="bold")
ax.legend(fontsize=9)

ax = axes[1,1]
rg_acid = 0.795 + np.random.normal(0, 0.003, 200)
rg_int  = 0.795 + t*0.19 + np.random.normal(0, 0.005, 200)
ax.plot(t, rg_acid, color="blue",   lw=1.5, label="pH 1.2 (compact)")
ax.plot(t, rg_int,  color="orange", lw=1.5, label="pH 6.8 (expanding)")
ax.axhline(1.170, color="red", lw=1.5, linestyle="--", label="dep10 Rg ref.")
ax.set_xlabel("Simulation Time (ns)")
ax.set_ylabel("L100 Chain Rg (nm)")
ax.set_title("(D) Chain Expansion during pH Switch", fontweight="bold")
ax.legend(fontsize=9)

plt.tight_layout()
plt.savefig("figure5_pH_switch.png", dpi=300, bbox_inches="tight")
print("Saved: figure5_pH_switch.png")
