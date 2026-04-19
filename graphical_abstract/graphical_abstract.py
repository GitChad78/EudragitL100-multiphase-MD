import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np

# ── Global style ──────────────────────────────────────────────
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.linewidth": 0.8,
})

fig = plt.figure(figsize=(16, 22))
fig.patch.set_facecolor("white")

# ── Title ─────────────────────────────────────────────────────
fig.text(0.5, 0.978, "Eudragit L100  \u00b7  All-atom MD Simulation Study",
         ha="center", va="top", fontsize=22, fontweight="bold", color="#1a1a2e")
fig.text(0.5, 0.963, "pH response  \u00b7  Plasticizer  \u00b7  Film barrier  \u00b7  Counterions  \u00b7  Concentration",
         ha="center", va="top", fontsize=11, color="#555577")

def phase_box(ax, color, label, label_color="#1a1a2e"):
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    box = FancyBboxPatch((0.01, 0.01), 0.98, 0.98,
                         boxstyle="round,pad=0.02",
                         facecolor=color, edgecolor="#CCCCCC",
                         linewidth=1.2, zorder=0)
    ax.add_patch(box)
    ax.text(0.03, 0.96, label, fontsize=10, fontweight="bold",
            color=label_color, va="top", transform=ax.transAxes)
    return ax

# ══ PHASE 0 ══════════════════════════════════════════════════
ax_p0 = fig.add_axes([0.02, 0.760, 0.46, 0.195])
phase_box(ax_p0, "#EEF2FF", "PHASE 0  \u00b7  pH / Ionisation Series")

ax_bar = fig.add_axes([0.04, 0.778, 0.17, 0.155])
deprot = [0, 2, 5, 10]
rg_vals = [0.795, 0.865, 0.960, 1.170]
bar_colors = ["#A8C4E0", "#7BAFD4", "#4E8FC0", "#1A5276"]
bars = ax_bar.bar(deprot, rg_vals, width=1.6, color=bar_colors, edgecolor="white")
ax_bar.set_xlabel("% MAA ionised", fontsize=7.5)
ax_bar.set_ylabel("Rg (nm)", fontsize=7.5)
ax_bar.set_xticks(deprot)
ax_bar.set_xticklabels(["0%", "2%", "5%", "10%"], fontsize=7)
ax_bar.set_ylim(0, 1.45)
ax_bar.tick_params(labelsize=7)
ax_bar.set_facecolor("#EEF2FF")
for bar, val in zip(bars, rg_vals):
    ax_bar.text(bar.get_x()+bar.get_width()/2, val+0.02,
                f"{val}", ha="center", fontsize=6.5, fontweight="bold")

ax_wave = fig.add_axes([0.23, 0.778, 0.24, 0.155])
ax_wave.set_xlim(0, 1); ax_wave.set_ylim(0, 1); ax_wave.axis("off")
ax_wave.set_facecolor("#EEF2FF")
ax_wave.text(0.03, 0.95, "0% MAA  \u2014  compact", fontsize=8.5,
             fontweight="bold", color="#1A5276", va="top")
ax_wave.text(0.03, 0.80, "Rg = 0.795 nm", fontsize=7.5, color="#333333")
x = np.linspace(0.03, 0.97, 400)
y1 = 0.63 + 0.05*np.sin(x*55)
ax_wave.plot(x, y1, color="#4E8FC0", lw=2.2)
ax_wave.annotate("", xy=(0.5, 0.43), xytext=(0.5, 0.54),
                 arrowprops=dict(arrowstyle="->", color="#333333", lw=1.5))
ax_wave.text(0.54, 0.46, "\u2191 pH", fontsize=8.5, color="#333333")
ax_wave.text(0.03, 0.36, "10% MAA  \u2014  expanded", fontsize=8.5,
             fontweight="bold", color="#6B2FA0")
ax_wave.text(0.03, 0.22, "Rg = 1.170 nm (+47.1%)", fontsize=7.5, color="#333333")
y2 = 0.12 + 0.09*np.sin(x*32)
ax_wave.plot(x, y2, color="#8E44AD", lw=2.5)

# ══ PHASE 0b ═════════════════════════════════════════════════
ax_p0b = fig.add_axes([0.52, 0.760, 0.46, 0.195])
phase_box(ax_p0b, "#EEFBF3", "PHASE 0b  \u00b7  Plasticizer Comparison (TEC vs PEG400)")

ax_bar2 = fig.add_axes([0.55, 0.778, 0.30, 0.155])
components = ["vdW", "H-bond", "Coulomb"]
tec_vals = [1821, 340, 260]
peg_vals = [980, 420, 310]
x2 = np.arange(len(components))
w = 0.35
ax_bar2.bar(x2-w/2, tec_vals, w, color="#27AE60", label="TEC", edgecolor="white")
ax_bar2.bar(x2+w/2, peg_vals, w, color="#A9DFBF", label="PEG400", edgecolor="white")
for i, (t, p) in enumerate(zip(tec_vals, peg_vals)):
    ax_bar2.text(i-w/2, t+30, str(t), ha="center", fontsize=7, fontweight="bold")
    ax_bar2.text(i+w/2, p+30, str(p), ha="center", fontsize=7)
ax_bar2.set_xticks(x2)
ax_bar2.set_xticklabels(components, fontsize=8)
ax_bar2.set_ylabel("Interaction Energy (kJ/mol)", fontsize=7.5)
ax_bar2.legend(fontsize=7.5, loc="upper right", framealpha=0.7)
ax_bar2.set_facecolor("#EEFBF3")
ax_bar2.tick_params(labelsize=7)
ax_bar2.text(0.02, -0.28,
    "vdW dominant  \u00b7  TEC dE lower by 1821 kJ/mol  \u00b7  H-bonding minor",
    fontsize=7, color="#1A7A4A", transform=ax_bar2.transAxes)
ax_bar2.text(0.02, -0.40,
    "TEC preferred plasticizer for L100 enteric films",
    fontsize=7, color="#1A7A4A", transform=ax_bar2.transAxes)

# ══ PHASE 1 ══════════════════════════════════════════════════
ax_p1 = fig.add_axes([0.02, 0.545, 0.46, 0.205])
phase_box(ax_p1, "#FFFBEE", "PHASE 1  \u00b7  TEC Loading Series (10\u201340% w/w)")

ax_mob = fig.add_axes([0.05, 0.565, 0.25, 0.155])
tec_pct = np.array([10, 20, 30, 40])
mobility = np.array([1.21, 0.98, 0.72, 1.09])
ax_mob.plot(tec_pct, mobility, color="#C47A00", lw=2.5, zorder=2)
ax_mob.scatter([30], [0.72], color="#E74C3C", s=70, zorder=5)
ax_mob.axvline(30, color="#E74C3C", lw=1, linestyle="--", alpha=0.5)
ax_mob.text(30.5, 0.74, "30% w/w\n(lowest mobility)", fontsize=6.5, color="#E74C3C")
ax_mob.set_xlabel("% TEC w/w", fontsize=7.5)
ax_mob.set_ylabel("Mobility", fontsize=7.5)
ax_mob.set_xlim(8, 42); ax_mob.set_ylim(0.65, 1.3)
ax_mob.set_xticks([10, 20, 30, 40])
ax_mob.tick_params(labelsize=7)
ax_mob.set_facecolor("#FFFBEE")

ax_info = fig.add_axes([0.31, 0.565, 0.15, 0.155])
ax_info.set_xlim(0, 1); ax_info.set_ylim(0, 1); ax_info.axis("off")
ibox = FancyBboxPatch((0.05, 0.05), 0.90, 0.90, boxstyle="round,pad=0.05",
                      facecolor="#FDEBD0", edgecolor="#C47A00", lw=1.5)
ax_info.add_patch(ibox)
ax_info.text(0.5, 0.80, "Free volume at 30%:", ha="center", fontsize=7,
             fontweight="bold", color="#7D4E00")
ax_info.text(0.5, 0.62, "+14.8% \u2192 effective", ha="center", fontsize=7, color="#333")
ax_info.text(0.5, 0.46, "plasticisation", ha="center", fontsize=7, color="#333")
ax_info.text(0.5, 0.28, "no excessive matrix", ha="center", fontsize=6.5, color="#666")
ax_info.text(0.5, 0.12, "weakening", ha="center", fontsize=6.5, color="#666")

# ══ PHASE 2 ══════════════════════════════════════════════════
ax_p2 = fig.add_axes([0.52, 0.545, 0.46, 0.205])
phase_box(ax_p2, "#F0F9EE", "PHASE 2  \u00b7  Multichain Film  \u00b7  Gastric Barrier")

ax_film = fig.add_axes([0.55, 0.580, 0.38, 0.135])
ax_film.set_xlim(0, 1); ax_film.set_ylim(0, 1); ax_film.axis("off")
wbox = FancyBboxPatch((0, 0.72), 1, 0.26, boxstyle="round,pad=0.01",
                      facecolor="#D6EAF8", edgecolor="none")
ax_film.add_patch(wbox)
ax_film.text(0.5, 0.87, "water phase above film  \u00b7  \u2191 diffusivity",
             ha="center", fontsize=8, color="#1A5276")
for xi in [0.08, 0.18, 0.28, 0.68, 0.78, 0.88]:
    ax_film.plot(xi, 0.96, "o", color="#5DADE2", ms=5)
pbox = FancyBboxPatch((0, 0.35), 1, 0.35, boxstyle="round,pad=0.01",
                      facecolor="#A9DFBF", edgecolor="none")
ax_film.add_patch(pbox)
ax_film.text(0.5, 0.57, "polymer-rich film", ha="center",
             fontsize=9, fontweight="bold", color="#1A7A4A")
ax_film.text(0.5, 0.45, "dense packing  \u00b7  \u2193 water diffusivity",
             ha="center", fontsize=7.5, color="#1A5276")
ax_film.text(0.5, 0.37, "gastric barrier intact  \u00b7  low drug permeability",
             ha="center", fontsize=7.5, color="#1A5276")
gbox = FancyBboxPatch((0, 0.01), 1, 0.32, boxstyle="round,pad=0.01",
                      facecolor="#FADBD8", edgecolor="none")
ax_film.add_patch(gbox)
ax_film.text(0.5, 0.17, "gastric fluid below film  \u00b7  low pH",
             ha="center", fontsize=8, color="#922B21")
for xi in [0.08, 0.18, 0.28, 0.68, 0.78, 0.88]:
    ax_film.plot(xi, 0.05, "o", color="#5DADE2", ms=4)
ax_film.text(1.02, 0.525, "film", fontsize=7, color="#2E7D32", rotation=90, va="center")
ax_film.annotate("", xy=(1.01, 0.36), xytext=(1.01, 0.69),
                 arrowprops=dict(arrowstyle="<->", color="#2E7D32", lw=1))

ax_bul = fig.add_axes([0.55, 0.548, 0.40, 0.033])
ax_bul.axis("off")
ax_bul.text(0, 0.8, "\u2022 Effective enteric coat: water excluded from polymer interior",
            fontsize=7.5, color="#1A5276")
ax_bul.text(0, 0.4, "\u2022 TEC retained in dense matrix \u00b7 low drug permeability at gastric pH",
            fontsize=7.5, color="#1A5276")
ax_bul.text(0, 0.0, "\u2022 Multichain packing confirms barrier function from MD simulation",
            fontsize=7.5, color="#1A5276")

# ══ PHASE 3 ══════════════════════════════════════════════════
ax_p3 = fig.add_axes([0.02, 0.320, 0.46, 0.215])
phase_box(ax_p3, "#FDF0F5", "PHASE 3  \u00b7  pH-Switch Film (Gastric \u2192 Intestinal)")

ax_ph = fig.add_axes([0.05, 0.340, 0.40, 0.165])
ax_ph.set_xlim(0, 1); ax_ph.set_ylim(0, 1); ax_ph.axis("off")
g2 = FancyBboxPatch((0.01, 0.15), 0.37, 0.78, boxstyle="round,pad=0.02",
                    facecolor="#FADBD8", edgecolor="#C0392B", lw=1.5)
ax_ph.add_patch(g2)
ax_ph.text(0.195, 0.89, "Gastric pH", ha="center", fontsize=9,
           fontweight="bold", color="#922B21")
xg = np.linspace(0.03, 0.37, 200)
yg = 0.60 + 0.055*np.sin(xg*80)
ax_ph.plot(xg, yg, color="#E74C3C", lw=2)
ax_ph.text(0.195, 0.38, "compact \u00b7 dry \u00b7 TEC slow",
           ha="center", fontsize=7.5, color="#922B21")
ax_ph.annotate("", xy=(0.62, 0.55), xytext=(0.42, 0.55),
               arrowprops=dict(arrowstyle="->", color="#333333", lw=2))
ax_ph.text(0.50, 0.65, "\u2191 pH", ha="center", fontsize=9, color="#333333")
ib = FancyBboxPatch((0.62, 0.15), 0.36, 0.78, boxstyle="round,pad=0.02",
                    facecolor="#D5F5E3", edgecolor="#27AE60", lw=1.5)
ax_ph.add_patch(ib)
ax_ph.text(0.80, 0.89, "Intestinal pH", ha="center", fontsize=9,
           fontweight="bold", color="#1A7A4A")
xi2 = np.linspace(0.64, 0.96, 200)
yi2 = 0.60 + 0.10*np.sin(xi2*50)
ax_ph.plot(xi2, yi2, color="#27AE60", lw=2.5)
for xd in [0.67, 0.74, 0.81, 0.88, 0.95]:
    ax_ph.plot(xd, 0.45, "o", color="#5DADE2", ms=5)
ax_ph.text(0.80, 0.30, "swollen \u00b7 hydrated \u00b7 TEC mobile",
           ha="center", fontsize=7.5, color="#1A7A4A")
ax_ph.text(0.5, 0.10,
    "hydration \u2191 \u00b7 swelling \u2191 \u00b7 TEC mobility \u2191\n"
    "intestinal drug release triggered\npH-responsive swelling confirmed by MD",
    ha="center", fontsize=7.5, color="#555555")

# ══ PHASE 4 ══════════════════════════════════════════════════
ax_p4 = fig.add_axes([0.52, 0.320, 0.46, 0.215])
phase_box(ax_p4, "#FFF5F5", "PHASE 4  \u00b7  Counterion Effects (Cl\u207b vs HCO\u2083\u207b/CO\u2083\u00b2\u207b)")

ax_ci = fig.add_axes([0.55, 0.345, 0.40, 0.165])
ax_ci.set_xlim(0, 1); ax_ci.set_ylim(0, 1); ax_ci.axis("off")
cl = plt.Circle((0.10, 0.82), 0.075, color="#E74C3C", zorder=3)
ax_ci.add_patch(cl)
ax_ci.text(0.10, 0.82, "Cl\u207b", ha="center", va="center",
           fontsize=8, fontweight="bold", color="white")
xc = np.linspace(0.02, 0.38, 200)
yc = 0.63 + 0.05*np.sin(xc*60)
ax_ci.plot(xc, yc, color="#E74C3C", lw=2)
ax_ci.text(0.20, 0.51, "Cl\u207b reference", ha="center", fontsize=8, color="#922B21")
hco = plt.Circle((0.62, 0.82), 0.072, color="#27AE60", zorder=3)
ax_ci.add_patch(hco)
ax_ci.text(0.62, 0.82, "HCO\u2083", ha="center", va="center",
           fontsize=6, fontweight="bold", color="white")
co3 = plt.Circle((0.83, 0.82), 0.082, color="#1A7A4A", zorder=3)
ax_ci.add_patch(co3)
ax_ci.text(0.83, 0.82, "CO\u2083\u00b2\u207b", ha="center", va="center",
           fontsize=6, fontweight="bold", color="white")
xh = np.linspace(0.52, 0.96, 200)
yh = 0.63 + 0.07*np.sin(xh*45)
ax_ci.plot(xh, yh, color="#27AE60", lw=2.5)
ax_ci.text(0.74, 0.51, "HCO\u2083\u207b/CO\u2083\u00b2\u207b",
           ha="center", fontsize=8, color="#1A7A4A")
ax_bci = fig.add_axes([0.55, 0.328, 0.14, 0.065])
ax_bci.bar([0, 1], [0.920, 0.938], color=["#E74C3C", "#27AE60"],
           width=0.6, edgecolor="white")
ax_bci.set_xticks([0, 1])
ax_bci.set_xticklabels(["Cl\u207b", "HCO\u2083\u207b"], fontsize=7)
ax_bci.set_ylabel("Rg", fontsize=7)
ax_bci.tick_params(labelsize=6)
ax_bci.text(1, 0.940, "+2%", ha="center", fontsize=7,
            color="#27AE60", fontweight="bold")
ax_bci.set_facecolor("#FFF5F5")
ax_ci.text(0.5, 0.28,
    "Cl\u207b baseline Rg\nHCO\u2083\u207b/CO\u2083\u00b2\u207b: +-2% expansion\ncounterion effect small overall",
    ha="center", fontsize=7.5, color="#555555")
ax_ci.text(0.5, 0.08,
    "ionic environment: minimal impact \u00b7 pH dominates\nrobust conformation across physiological fluids",
    ha="center", fontsize=7.5, color="#8E1A1A")

# ══ PHASE 5 ══════════════════════════════════════════════════
ax_p5 = fig.add_axes([0.02, 0.080, 0.96, 0.230])
phase_box(ax_p5, "#F5F0FF", "PHASE 5  \u00b7  Concentration Series  \u00b7  Overlap Concentration c*")

ax_visc = fig.add_axes([0.06, 0.100, 0.52, 0.170])
phi = np.linspace(0.001, 0.08, 500)
eta = 0.1 + 200*(phi**2.5)*np.exp(phi*15)
ax_visc.plot(phi, eta, color="#333333", lw=2.5)
ax_visc.axvline(0.012, color="#8E44AD", lw=1.5, linestyle="--")
ax_visc.axvline(0.022, color="#8E44AD", lw=1.5, linestyle="--")
ax_visc.fill_betweenx([0, max(eta)*1.05], 0.012, 0.022, alpha=0.15, color="#8E44AD")
ax_visc.text(0.017, max(eta)*0.75, "c*", ha="center", fontsize=14,
             fontweight="bold", color="#4A1A8E")
ax_visc.text(0.017, max(eta)*0.55,
    "phi = 0.012-0.022\n= 5-7% w/v L100",
    ha="center", fontsize=8, color="#4A1A8E")
ax_visc.set_xlabel("polymer volume fraction phi", fontsize=9)
ax_visc.set_ylabel("eta (viscosity)", fontsize=9)
ax_visc.set_xlim(0, 0.08)
ax_visc.set_ylim(0, max(eta)*1.08)
ax_visc.set_yticks([])
ax_visc.set_xticks([0.012, 0.022])
ax_visc.set_xticklabels(["phi=0.012", "phi=0.022"], fontsize=8)
ax_visc.text(0.02, -0.14, "dilute", fontsize=8, color="#555555",
             transform=ax_visc.transAxes)
ax_visc.text(0.72, -0.14, "semi-dilute (entangled)", fontsize=8, color="#555555",
             transform=ax_visc.transAxes)
ax_visc.set_facecolor("#F5F0FF")

# Dilute chain cartoons
ax_dil = fig.add_axes([0.06, 0.148, 0.09, 0.065])
ax_dil.set_xlim(0, 1); ax_dil.set_ylim(0, 1); ax_dil.axis("off")
for cx, cy, r in [(0.28, 0.60, 0.22), (0.72, 0.32, 0.20)]:
    circ = plt.Circle((cx, cy), r, fill=False, edgecolor="#888888",
                       lw=1.5, linestyle="--")
    ax_dil.add_patch(circ)
    xw = np.linspace(cx-r*0.8, cx+r*0.8, 100)
    yw = cy + r*0.4*np.sin(xw*20)
    ax_dil.plot(xw, yw, color="#888888", lw=1.5)

# Entangled chain cartoons
ax_ent = fig.add_axes([0.45, 0.148, 0.09, 0.065])
ax_ent.set_xlim(0, 1); ax_ent.set_ylim(0, 1); ax_ent.axis("off")
colors_e = ["#4A1A8E", "#8E44AD", "#333333"]
for i, (cx, cy) in enumerate([(0.3, 0.65), (0.55, 0.45), (0.7, 0.70)]):
    xw = np.linspace(0.05, 0.95, 150)
    yw = cy + 0.12*np.sin(xw*25 + i*2)
    ax_ent.plot(xw, yw, color=colors_e[i], lw=2)

ax_visc.text(0.5, -0.22,
    "Practical working range for aqueous coating dispersions: 5-7% w/v L100",
    ha="center", fontsize=9, color="#4A1A8E", fontweight="bold",
    transform=ax_visc.transAxes)

# ══ KEY OUTPUTS FOOTER ═══════════════════════════════════════
ax_foot = fig.add_axes([0.02, 0.042, 0.96, 0.034])
ax_foot.set_xlim(0, 1); ax_foot.set_ylim(0, 1); ax_foot.axis("off")
fbox = FancyBboxPatch((0, 0), 1, 1, boxstyle="round,pad=0.02",
                      facecolor="#EAF0FF", edgecolor="#2E4080", lw=1.5)
ax_foot.add_patch(fbox)
ax_foot.text(0.5, 0.68,
    "Key outputs: pH-driven Rg switch  \u00b7  TEC optimal at ~30%  \u00b7  dense film barrier  \u00b7  pH-responsive swelling",
    ha="center", fontsize=9, fontweight="bold", color="#2E4080")
ax_foot.text(0.5, 0.22,
    "counterions minor effect  \u00b7  c* = 5-7% w/v practical range for L100 aqueous dispersions",
    ha="center", fontsize=9, color="#5566AA")

# ══ GITHUB NOTE ══════════════════════════════════════════════
ax_note = fig.add_axes([0.02, 0.002, 0.96, 0.036])
ax_note.set_xlim(0, 1); ax_note.set_ylim(0, 1); ax_note.axis("off")
nbox = FancyBboxPatch((0, 0), 1, 1, boxstyle="round,pad=0.02",
                      facecolor="#FFFFFF", edgecolor="#4C72B0", lw=1.2)
ax_note.add_patch(nbox)
ax_note.text(0.5, 0.65,
    "Graphical abstract generated using Python/matplotlib.",
    ha="center", fontsize=8, color="#333333", style="italic")
ax_note.text(0.5, 0.18,
    "Script freely available at GitHub: https://github.com/GitChad78/EudragitL100-multiphase-MD  (graphical_abstract/graphical_abstract.py)",
    ha="center", fontsize=8, color="#2E4080", fontweight="bold")

plt.savefig("graphical_abstract_final.png", dpi=200,
            bbox_inches="tight", facecolor="white")
print("Saved: graphical_abstract_final.png")
