"""
Eudragit L100 · All-atom MD Simulation Study — Graphical Abstract
Run:    python NEW_G_A.py
Output: graphical_abstract_output.png
Needs:  pip install matplotlib numpy scipy
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
from matplotlib.gridspec import GridSpec
from scipy.interpolate import make_interp_spline
import warnings
warnings.filterwarnings('ignore')

# ── Exact colours (pixel-sampled from reference) ──────────────────────────────
BG_PAGE     = "#FFFFFF"
BG_TITLE    = "#EEEDFD"   # lavender title strip
BG_P0       = "#E9F0FF"   # phase 0  light blue
BG_P0B      = "#E1F4EE"   # phase 0b light green
BG_P1       = "#F5EDD8"   # phase 1  warm cream
BG_P2       = "#E8F5EC"   # phase 2  light green
BG_P3       = "#FEDDEE"   # phase 3  pink
BG_P4       = "#FFE7E9"   # phase 4  light pink
BG_P5       = "#F2EFE8"   # phase 5  warm cream
BG_FOOTER   = "#E8E6D8"   # footer   warm-gray (same as P5 bottom)

# bar / element colours
C_BAR1   = "#8FB5DE"   # 0%  MAA  light blue
C_BAR2   = "#48A0E0"   # 2%  MAA  medium blue
C_BAR3   = "#2D6EB0"   # 5%  MAA  darker blue
C_BAR4   = "#1A4E80"   # 10% MAA  dark blue
C_TEC    = "#337848"   # TEC green bars
C_PEG    = "#919F9C"   # PEG400 grey bars
C_ORANGE = "#DA5C22"   # Phase 1 curve / marker
C_DKBLUE = "#2255A0"   # Phase 0 wavy compact
C_LTBlue = "#68A8DC"   # Phase 0 wavy expanded light
C_PKWAVY = "#AA6478"   # Phase 3 gastric wavy
C_TEAL   = "#6E9F93"   # Phase 3 intestinal wavy
C_CL_RG  = "#C08888"   # Phase 4 Cl Rg bar
C_HC_RG  = "#80B860"   # Phase 4 HCO3 Rg bar
C_DARK   = "#1A1A1A"
C_GRAY   = "#555555"
C_P5     = "#303028"   # Phase 5 viscosity curve

# ── Helpers ───────────────────────────────────────────────────────────────────
def wv(ax, cx, cy, amp, freq, color, lw, scale, n=300):
    """Wavy chain in axes-fraction coords."""
    x = np.linspace(cx - scale/2, cx + scale/2, n)
    y = cy + amp * np.sin(freq * np.pi * (x - cx) / (scale/2))
    ax.plot(x, y, color=color, lw=lw, solid_capstyle='round',
            transform=ax.transAxes, zorder=4)

def wv_data(ax, cx, cy, amp, freq, color, lw, scale, n=300):
    """Wavy chain in data coords."""
    x = np.linspace(cx - scale, cx + scale, n)
    y = cy + amp * np.sin(freq * np.pi * (x - cx) / scale)
    ax.plot(x, y, color=color, lw=lw, solid_capstyle='round', zorder=4)

def oval(ax, cx, cy, rx, ry, color, lw=0.9):
    """Dashed oval in data coords."""
    t = np.linspace(0, 2*np.pi, 200)
    ax.plot(cx + rx*np.cos(t), cy + ry*np.sin(t), color=color, lw=lw, ls='--')

def inset_style(ax, bg, edge):
    ax.set_facecolor(bg)
    for sp in ax.spines.values():
        sp.set_linewidth(0.7); sp.set_color(edge)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

def panel_style(ax, bg, edge):
    ax.set_facecolor(bg)
    for sp in ax.spines.values():
        sp.set_edgecolor(edge); sp.set_linewidth(1.5)
    ax.axis('off')

def hdr(ax, num, subtitle, x=0.018, y=0.976):
    # Draw bold "PHASE N" label then lighter subtitle after measured offset
    label = f"PHASE {num}"
    ax.text(x, y, label, transform=ax.transAxes,
            fontsize=10, fontweight='bold', color=C_DARK, va='top')
    # Offset: each char ≈ 0.012 in axes units at fontsize 10
    offset = len(label) * 0.0118 + 0.008
    ax.text(x + offset, y, f" · {subtitle}", transform=ax.transAxes,
            fontsize=8.8, color=C_DARK, va='top')

# ── Figure ────────────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(14, 19), facecolor=BG_PAGE)

# Full-poster rounded lavender border
fig.add_artist(mpatches.FancyBboxPatch(
    (0.008, 0.007), 0.984, 0.986,
    boxstyle="round,pad=0.008",
    linewidth=2.0, edgecolor="#B0AADD",
    facecolor=BG_TITLE,
    transform=fig.transFigure, zorder=0))

gs = GridSpec(8, 2, figure=fig,
              left=0.032, right=0.968,
              top=0.966, bottom=0.075,
              hspace=0.30, wspace=0.055,
              height_ratios=[0.28, 1, 1, 1, 1, 1, 1, 1.0])

# ════════════════════════════════════════════════════════════════════
#  TITLE
# ════════════════════════════════════════════════════════════════════
axt = fig.add_subplot(gs[0, :])
axt.set_facecolor(BG_TITLE); axt.axis('off')
axt.text(0.5, 0.72, "Eudragit L100 · All-atom MD Simulation Study",
         ha='center', va='center', fontsize=16, fontweight='bold',
         color="#3535A0", transform=axt.transAxes)
axt.text(0.5, 0.14,
         "pH response · Plasticizer · Film barrier · Counterions · Concentration",
         ha='center', va='center', fontsize=9, color="#5555AA",
         transform=axt.transAxes)

# ════════════════════════════════════════════════════════════════════
#  PHASE 0  ·  pH / Ionisation Series
# ════════════════════════════════════════════════════════════════════
a0 = fig.add_subplot(gs[1:3, 0])
panel_style(a0, BG_P0, "#8AAAD8")
hdr(a0, "0", "pH / Ionisation Series")

# Bar chart (left half)
i0 = a0.inset_axes([0.045, 0.12, 0.44, 0.76])
inset_style(i0, BG_P0, "#8AAAD8")
pct  = [0, 2, 5, 10]
rg   = [0.795, 0.865, 0.960, 1.170]
bcol = [C_BAR1, C_BAR2, C_BAR3, C_BAR4]
bars = i0.bar(pct, rg, width=1.8, color=bcol, edgecolor='none')
for b, v in zip(bars, rg):
    i0.text(b.get_x()+b.get_width()/2, v+0.013, str(v),
            ha='center', fontsize=6.2, color=C_DARK)
i0.axhline(1.0, color=C_BAR2, lw=0.8, ls='--', alpha=0.55, xmin=0.0)
i0.set_xticks(pct)
i0.set_xticklabels(['0%','2%','5%','10%'], fontsize=6.5)
i0.set_yticks([0.0, 0.5, 1.0])
i0.set_ylabel("Rg (nm)", fontsize=7)
i0.set_xlabel("% MAA ionised", fontsize=6.5)
i0.set_ylim(0, 1.40)
i0.tick_params(labelsize=6.5, length=2)

# Vertical dashed divider
a0.plot([0.52, 0.52], [0.06, 0.95], color="#8AAAD8", lw=0.8, ls='--',
        transform=a0.transAxes)

# "0% MAA — compact"
a0.text(0.565, 0.945, "0% MAA — compact", transform=a0.transAxes,
        fontsize=8, fontweight='bold', color=C_DKBLUE, va='top')
wv(a0, 0.755, 0.79, amp=0.032, freq=4.2, color=C_DKBLUE, lw=2.2, scale=0.38)
a0.text(0.600, 0.695, "Rg = 0.795 nm", transform=a0.transAxes,
        fontsize=7, color=C_DARK)
# Arrow
a0.annotate('', xy=(0.755, 0.632), xytext=(0.755, 0.690),
            xycoords='axes fraction',
            arrowprops=dict(arrowstyle='->', color=C_DARK, lw=1.1))
a0.text(0.775, 0.660, "↑ pH", transform=a0.transAxes, fontsize=7, color=C_DARK)

# "10% MAA — expanded"
a0.text(0.565, 0.585, "10% MAA — expanded", transform=a0.transAxes,
        fontsize=8, fontweight='bold', color=C_DKBLUE, va='top')
# Two overlapping wavy chains
wv(a0, 0.735, 0.415, amp=0.055, freq=3.2, color=C_DKBLUE, lw=2.2, scale=0.38)
wv(a0, 0.780, 0.350, amp=0.055, freq=3.2, color=C_LTBlue, lw=2.0, scale=0.38)
a0.text(0.565, 0.225, "Rg = 1.170 nm (+47.1%)", transform=a0.transAxes,
        fontsize=7, color=C_DARK)
a0.text(0.018, 0.032,
        "* Nonmonotonic at 2% → strong expansion at 10% (intestinal pH)",
        transform=a0.transAxes, fontsize=6.0, color=C_GRAY, style='italic')

# ════════════════════════════════════════════════════════════════════
#  PHASE 0b  ·  Plasticizer Comparison (TEC vs PEG400)
# ════════════════════════════════════════════════════════════════════
a0b = fig.add_subplot(gs[1:3, 1])
panel_style(a0b, BG_P0B, "#70B890")
a0b.text(0.018, 0.976, "PHASE 0b", transform=a0b.transAxes,
         fontsize=10, fontweight='bold', color=C_DARK, va='top')
a0b.text(0.195, 0.976, "· Plasticizer Comparison (TEC vs PEG400)",
         transform=a0b.transAxes, fontsize=8.8, color=C_DARK, va='top')

i0b = a0b.inset_axes([0.075, 0.22, 0.90, 0.62])
inset_style(i0b, BG_P0B, "#70B890")
cats  = ['vdW', 'H-bond', 'Coulomb']
tec_v = [1821, 340, 260]
peg_v = [980,  420, 310]
xp = np.array([0, 1, 2]); w = 0.30
b1 = i0b.bar(xp-w/2, tec_v, width=w, color=C_TEC,  label='TEC',    edgecolor='none')
b2 = i0b.bar(xp+w/2, peg_v, width=w, color=C_PEG, label='PEG400', edgecolor='none')
for b, v in zip(list(b1)+list(b2), tec_v+peg_v):
    i0b.text(b.get_x()+b.get_width()/2, v+28, str(v),
             ha='center', fontsize=6.2, color=C_DARK)
for yv in [500, 1000, 1500]:
    i0b.axhline(yv, color=C_TEC, lw=0.5, ls='--', alpha=0.35)
i0b.set_xticks(xp)
i0b.set_xticklabels(cats, fontsize=7.5)
i0b.set_ylabel("|Interaction Energy| (kJ/mol)", fontsize=6.8)
i0b.set_xlabel("Interaction Energy Component", fontsize=7)
i0b.set_ylim(0, 2250); i0b.set_yticks([0, 500, 1000, 1500, 2000])
i0b.legend(fontsize=7, framealpha=0.6, loc='upper right',
           handlelength=1.2, handleheight=0.9)
i0b.tick_params(labelsize=6.5, length=2)

a0b.text(0.04, 0.185,
         "vdW dominant · TEC ΔE lower by 1821 kJ/mol · H-bonding minor",
         transform=a0b.transAxes, fontsize=7.0, color=C_DARK)
a0b.text(0.04, 0.095,
         "TEC preferred plasticizer for L100 enteric films",
         transform=a0b.transAxes, fontsize=7.0, color=C_DARK)

# ════════════════════════════════════════════════════════════════════
#  PHASE 1  ·  TEC Loading Series
# ════════════════════════════════════════════════════════════════════
a1 = fig.add_subplot(gs[3:5, 0])
panel_style(a1, BG_P1, "#C8A050")
hdr(a1, "1", "TEC Loading Series (10–40% w/w)")

# Chart takes upper 58%, leaves room for x-labels + info-box below
i1 = a1.inset_axes([0.10, 0.36, 0.86, 0.52])
inset_style(i1, BG_P1, "#C8A050")
xt  = np.array([10, 15, 20, 25, 30, 35, 40])
mob = np.array([0.28, 0.52, 0.70, 0.88, 1.00, 0.80, 0.55])
xs  = np.linspace(10, 40, 300)
spl = make_interp_spline(xt, mob, k=3)
i1.plot(xs, spl(xs), color=C_ORANGE, lw=2.4)
i1.plot(30, 1.0, 'o', color="#D04820", ms=10, zorder=5)
i1.axvline(30, color="#D04820", lw=1.0, ls='--', alpha=0.55, ymax=0.93)
i1.set_ylabel("Mobility", fontsize=7.5)
i1.set_xticks([10, 40]); i1.set_xticklabels(['10%', '40%'], fontsize=6.5)
i1.set_yticks([])
i1.set_ylim(-0.02, 1.13); i1.set_xlim(8, 42)
i1.tick_params(labelsize=6.5, length=2)

# x-axis labels drawn manually in axes coords (no collision with info box)
a1.text(0.175, 0.305, "10%",         transform=a1.transAxes, fontsize=7, color=C_DARK, ha='center')
a1.text(0.50,  0.305, "% TEC w/w",   transform=a1.transAxes, fontsize=7.2,
        color="#9A6010", ha='center', fontweight='normal')
a1.text(0.50,  0.255, "~30% w/w (lowest mobility)", transform=a1.transAxes, fontsize=6.8,
        color="#9A6010", ha='center')
a1.text(0.895, 0.305, "40%",         transform=a1.transAxes, fontsize=7, color=C_DARK, ha='center')

# Info box
a1.add_patch(FancyBboxPatch((0.05, 0.038), 0.90, 0.20,
    boxstyle="round,pad=0.012",
    facecolor="#F0D898", edgecolor="#C8A050", lw=0.8,
    transform=a1.transAxes, zorder=2))
a1.text(0.50, 0.192, "Free volume at 30%: +14.8% → effective plasticisation",
        transform=a1.transAxes, fontsize=7.2, color=C_DARK, ha='center')
a1.text(0.50, 0.090, "no excessive matrix weakening",
        transform=a1.transAxes, fontsize=7.2, color=C_DARK, ha='center')

# ════════════════════════════════════════════════════════════════════
#  PHASE 2  ·  Multichain Film · Gastric Barrier
# ════════════════════════════════════════════════════════════════════
a2 = fig.add_subplot(gs[3:5, 1])
panel_style(a2, BG_P2, "#70B880")
hdr(a2, "2", "Multichain Film · Gastric Barrier")

# Water phase above (light blue)
a2.add_patch(FancyBboxPatch((0.040, 0.730), 0.840, 0.148,
    boxstyle="round,pad=0.012", facecolor="#C0D8EE",
    edgecolor="#90B8D8", lw=0.8, transform=a2.transAxes))
for xi in [0.115, 0.170, 0.228]:
    a2.plot(xi, 0.832, 'o', ms=7, color="#4080B0",
            transform=a2.transAxes, zorder=3)
a2.text(0.520, 0.806, "water phase above film · ↑ diffusivity",
        transform=a2.transAxes, fontsize=7.5, color=C_DARK, ha='center')

# Polymer-rich film (green)
a2.add_patch(FancyBboxPatch((0.040, 0.508), 0.840, 0.210,
    boxstyle="round,pad=0.008", facecolor="#98D898",
    edgecolor="#50A850", lw=0.8, transform=a2.transAxes))
a2.text(0.460, 0.637, "polymer-rich film",
        transform=a2.transAxes, fontsize=9, fontweight='bold',
        color=C_DARK, ha='center')
a2.text(0.460, 0.575, "dense packing · ↓ water diffusivity",
        transform=a2.transAxes, fontsize=7.2, color=C_DARK, ha='center')
a2.text(0.460, 0.520, "gastric barrier intact · low drug permeability",
        transform=a2.transAxes, fontsize=7.2, color=C_DARK, ha='center')

# Gastric fluid below (light blue)
a2.add_patch(FancyBboxPatch((0.040, 0.368), 0.840, 0.128,
    boxstyle="round,pad=0.012", facecolor="#C0D8EE",
    edgecolor="#90B8D8", lw=0.8, transform=a2.transAxes))
for xi in [0.10, 0.158]:
    a2.plot(xi, 0.437, 'o', ms=6, color="#4080B0",
            transform=a2.transAxes, zorder=3)
a2.text(0.520, 0.437, "gastric fluid below film · low pH",
        transform=a2.transAxes, fontsize=7.5, color=C_DARK, ha='center')

# "film" bracket right
a2.annotate('', xy=(0.897, 0.508), xytext=(0.897, 0.878),
            xycoords='axes fraction',
            arrowprops=dict(arrowstyle='-[,widthB=0.22',
                            color=C_DARK, lw=1.0))
a2.text(0.942, 0.690, "film", transform=a2.transAxes, fontsize=7,
        color=C_DARK, rotation=90, va='center')

# Dashed divider + bullets
a2.plot([0.03, 0.97], [0.344, 0.344], color="#80C080", lw=0.6, ls='--',
        transform=a2.transAxes)
bullets = [
    "▶ Effective enteric coat: water excluded from polymer interior",
    "▶ TEC retained in dense matrix · low drug permeability at gastric pH",
    "▶ Multichain packing confirms barrier function from MD simulation",
]
for i, b in enumerate(bullets):
    a2.text(0.045, 0.302 - i*0.082, b, transform=a2.transAxes,
            fontsize=6.8, color=C_DARK)

# ════════════════════════════════════════════════════════════════════
#  PHASE 3  ·  pH-Switch Film (Gastric → Intestinal)
# ════════════════════════════════════════════════════════════════════
a3 = fig.add_subplot(gs[5:7, 0])
panel_style(a3, BG_P3, "#D08090")
hdr(a3, "3", "pH-Switch Film (Gastric → Intestinal)")

# Gastric box (pink)
a3.add_patch(FancyBboxPatch((0.035, 0.345), 0.340, 0.520,
    boxstyle="round,pad=0.015", facecolor="#F4D2DC",
    edgecolor="#D090A8", lw=1.0, transform=a3.transAxes))
a3.text(0.205, 0.848, "Gastric pH",
        transform=a3.transAxes, fontsize=8.5, fontweight='bold',
        color="#B05070", ha='center')
wv(a3, 0.205, 0.670, amp=0.034, freq=3.8, color=C_PKWAVY, lw=2.2, scale=0.29)
wv(a3, 0.205, 0.555, amp=0.034, freq=3.8, color="#C07888", lw=2.0, scale=0.29)
a3.text(0.205, 0.385, "compact · dry · TEC slow",
        transform=a3.transAxes, fontsize=6.8, color=C_DARK, ha='center')

# Arrow + "↑ pH" + pink line
a3.annotate('', xy=(0.618, 0.590), xytext=(0.400, 0.590),
            xycoords='axes fraction',
            arrowprops=dict(arrowstyle='->', color="#D04060", lw=1.8))
a3.text(0.510, 0.635, "↑ pH",
        transform=a3.transAxes, fontsize=8.5, color="#D04060",
        ha='center', fontweight='bold')
a3.plot([0.400, 0.618], [0.558, 0.558], color="#D04060", lw=1.2,
        transform=a3.transAxes)

# Intestinal box (teal)
a3.add_patch(FancyBboxPatch((0.622, 0.345), 0.340, 0.520,
    boxstyle="round,pad=0.015", facecolor="#D0EAE4",
    edgecolor="#60A090", lw=1.0, transform=a3.transAxes))
a3.text(0.792, 0.848, "Intestinal pH",
        transform=a3.transAxes, fontsize=8.5, fontweight='bold',
        color="#306050", ha='center')
# two teal wavy curves
wv(a3, 0.792, 0.688, amp=0.045, freq=3.5, color=C_TEAL, lw=2.2, scale=0.29)
wv(a3, 0.792, 0.565, amp=0.045, freq=3.5, color="#90C0B8", lw=2.0, scale=0.29)
# water dots
for xi, yi in [(0.672, 0.640), (0.728, 0.678), (0.785, 0.650)]:
    a3.plot(xi, yi, 'o', ms=7, color="#60A8D0", alpha=0.85,
            transform=a3.transAxes, zorder=4)
a3.text(0.792, 0.385, "swollen · hydrated · TEC mobile",
        transform=a3.transAxes, fontsize=6.8, color=C_DARK, ha='center')

# Bottom notes
a3.text(0.50, 0.300, "hydration ↑ · swelling ↑ · TEC mobility ↑",
        transform=a3.transAxes, fontsize=7.0, color=C_DARK, ha='center')
a3.text(0.50, 0.215, "intestinal drug release triggered",
        transform=a3.transAxes, fontsize=7.0, color="#D04060", ha='center')
a3.text(0.50, 0.128, "pH-responsive swelling confirmed by MD",
        transform=a3.transAxes, fontsize=7.0, color=C_DARK, ha='center')

# ════════════════════════════════════════════════════════════════════
#  PHASE 4  ·  Counterion Effects
# ════════════════════════════════════════════════════════════════════
a4 = fig.add_subplot(gs[5:7, 1])
panel_style(a4, BG_P4, "#D09098")
hdr(a4, "4", "Counterion Effects (Cl⁻ vs HCO₃ ⁻/CO₃²⁻)")

def ion_circ(ax, x, y, label, fill, edge, r=0.058, fs=8.5):
    ax.add_patch(plt.Circle((x, y), r, color=fill, ec=edge,
                             lw=1.5, zorder=4, transform=ax.transAxes))
    ax.text(x, y, label, transform=ax.transAxes, ha='center', va='center',
            fontsize=fs, color=edge, fontweight='bold', zorder=5)

# Cl- ion circles
ion_circ(a4, 0.115, 0.838, "Cl⁻", "#FACCD0", "#C04050", r=0.058, fs=8.0)
ion_circ(a4, 0.250, 0.838, "Cl⁻", "#F8D0D4", "#C04050", r=0.058, fs=8.0)

# Cl- wavy + dash line
wv(a4, 0.175, 0.702, amp=0.028, freq=3.8, color="#C04050", lw=2.0, scale=0.28)
a4.plot([0.030, 0.430], [0.700, 0.700], color="#882030",
        lw=1.5, transform=a4.transAxes, zorder=2, solid_capstyle='round')
a4.text(0.175, 0.618, "Cl⁻ reference",
        transform=a4.transAxes, fontsize=7.2, color=C_DARK, ha='center')

# HCO3 / CO3 circles (green, different sizes)
ion_circ(a4, 0.625, 0.820, "HCO₃", "#DAFAD0", "#50A030", r=0.065, fs=7.0)
ion_circ(a4, 0.795, 0.845, "CO₃²⁻", "#C8F0B8", "#50A030", r=0.078, fs=7.0)

# HCO3 wavy
wv(a4, 0.710, 0.702, amp=0.028, freq=3.5, color="#50A030", lw=2.0, scale=0.30)
a4.text(0.710, 0.618, "HCO₃⁻/CO₃²⁻",
        transform=a4.transAxes, fontsize=7.2, color=C_DARK, ha='center')

# Mini Rg bar chart
i4 = a4.inset_axes([0.055, 0.165, 0.320, 0.330])
inset_style(i4, BG_P4, "#C04050")
i4.bar([0], [1.00], width=0.4, color=C_CL_RG, edgecolor='none')
i4.bar([1], [1.02], width=0.4, color=C_HC_RG, edgecolor='none')
i4.text(1, 1.025, "+2%", ha='center', fontsize=7, color="#50A030")
i4.set_xticks([0, 1]); i4.set_xticklabels(["Cl⁻","HCO₃⁻"], fontsize=7)
i4.set_yticks([]); i4.set_ylabel("Rg", fontsize=7.5)
i4.set_ylim(0, 1.12); i4.set_facecolor(BG_P4)
i4.spines['top'].set_visible(False); i4.spines['right'].set_visible(False)

rows4 = [
    ("Cl⁻ baseline Rg",                         C_DARK),
    ("HCO₃⁻/CO₃²⁻: +~2% expansion",            C_DARK),
    ("counterion effect small overall",           C_DARK),
    ("ionic environment: minimal impact · pH dominates", "#C04060"),
    ("robust conformation across physiological fluids",  "#C04060"),
]
for i, (txt, col) in enumerate(rows4):
    a4.text(0.415, 0.458 - i*0.083, txt, transform=a4.transAxes,
            fontsize=6.8, color=col)

# ════════════════════════════════════════════════════════════════════
#  PHASE 5  ·  Concentration Series · Overlap Concentration c*
# ════════════════════════════════════════════════════════════════════
a5 = fig.add_subplot(gs[7, :])
panel_style(a5, BG_P5, "#B0A880")
a5.text(0.010, 0.975, "PHASE 5", transform=a5.transAxes,
        fontsize=10, fontweight='bold', color=C_DARK, va='top')
a5.text(0.110, 0.975, "· Concentration Series · Overlap Concentration c*",
        transform=a5.transAxes, fontsize=8.8, color=C_DARK, va='top')

i5 = a5.inset_axes([0.055, 0.09, 0.908, 0.80])
i5.set_facecolor(BG_P5)

# Viscosity sigmoid
phi = np.linspace(0, 0.145, 600)
eta = 0.04 + 1.22 / (1 + np.exp(-80*(phi - 0.055)))
i5.plot(phi, eta, color=C_P5, lw=2.5)

# c* vertical dashed lines + shaded region
for vx in [0.009, 0.022]:
    i5.axvline(vx, color="#808070", lw=1.0, ls='--', alpha=0.85)
i5.axvspan(0.009, 0.022, alpha=0.10, color="#907060")

i5.set_xlim(-0.005, 0.145)
i5.set_ylim(-0.12, 1.42)
i5.set_xlabel("polymer volume fraction φ", fontsize=8.5)
i5.set_ylabel("η (viscosity)", fontsize=8.5)
i5.set_xticks([0.009, 0.022])
i5.set_xticklabels(["φ=0.009", "φ=0.022"], fontsize=7.8, color="#606050")
i5.set_yticks([])
i5.tick_params(labelsize=7.5, length=3)
i5.set_facecolor(BG_P5)
for sp in i5.spines.values():
    sp.set_linewidth(0.8); sp.set_color("#B0A880")

i5.text(-0.0042, 1.32, "high", fontsize=7.5, color="#606060", ha='right', va='top')
i5.text(-0.0042, 0.00, "low",  fontsize=7.5, color="#606060", ha='right', va='bottom')
i5.text(0.003,  -0.10, "dilute",                  fontsize=7.8, color="#808070", ha='center')
i5.text(0.095,  -0.10, "semi-dilute (entangled)",  fontsize=7.8, color="#808070", ha='center')

# c* annotation box (no edge — matches original subtle box)
i5.add_patch(FancyBboxPatch(
    (0.0085, 0.44), 0.0148, 0.75,
    boxstyle="round,pad=0.003",
    facecolor="#E5E2D0", edgecolor="#B0A870", lw=0.8, zorder=3))
i5.text(0.01590, 1.155, "c*",
        ha='center', fontsize=12, fontweight='bold', color=C_DARK, zorder=5)
i5.text(0.01590, 0.920, "φ ≈ 0.009–0.022",
        ha='center', fontsize=8.2, color=C_DARK, zorder=5)
i5.text(0.01590, 0.690, "≈ 0.7–1.8% w/v L100",
        ha='center', fontsize=8.2, color=C_DARK, zorder=5)

# Dilute polymer chains
oval(i5, 0.0012, 0.28, rx=0.0056, ry=0.110, color="#909080", lw=0.9)
wv_data(i5, 0.0012, 0.28, amp=0.050, freq=3.5, color="#909080", lw=1.5, scale=0.0040)
oval(i5, 0.0045, 0.40, rx=0.0056, ry=0.110, color="#909080", lw=0.9)
wv_data(i5, 0.0045, 0.40, amp=0.050, freq=3.5, color="#909080", lw=1.5, scale=0.0040)

# Semi-dilute entangled chains
wv_data(i5, 0.100, 0.900, amp=0.090, freq=4.2, color=C_P5, lw=2.0, scale=0.022)
wv_data(i5, 0.100, 0.740, amp=0.090, freq=3.8, color="#6A6860", lw=2.0, scale=0.022)

# ── Footer bar ────────────────────────────────────────────────────────────────
# Sits just below the Phase 5 panel, inside the outer lavender border
af = fig.add_axes([0.032, 0.030, 0.936, 0.038])
af.set_facecolor(BG_FOOTER)
for sp in af.spines.values(): sp.set_linewidth(0)
af.axis('off')
af.text(0.5, 0.52,
        "Practical working range for aqueous coating dispersions: "
        "5–10% w/v ~ semi-dilute to concentrated regime (φ ≈ 0.057–0.114)",
        ha='center', va='center', fontsize=8.5,
        color=C_DARK, fontfamily='DejaVu Sans')

# ── Output ────────────────────────────────────────────────────────────────────
out = "NEW_ABSTRACT.png"
fig.savefig(out, dpi=200, bbox_inches='tight', facecolor=BG_PAGE)
print(f"Saved → {out}")
plt.close(fig)
