"""
Figure 2 - Schematic molecular representation of L100 conformational
response at 3.5% MAA deprotonation (Phase 0 and Phase 3).
Manuscript: pH Responsive Conformation, Plasticiser Interactions,
and Film Formation in Eudragit L100: An All-Atom MD Study
Authors: Vaibhav Ambudkar, Rashmi Chauhan, Soham Ambudkar
GitHub: https://github.com/GitChad78/EudragitL100-multiphase-MD
Zenodo: https://doi.org/10.5281/zenodo.19471701
Data sources (all from GROMACS analysis):
  Rg at pH 1.2 (dep035): 0.920 nm  - gmx gyrate (Table S3, ESI)
  Rg at pH 6.8 (Phase 3): ~1.050 nm (+14.1%) - gmx gyrate (Table S9, ESI)
  Deprotonation ratio: 3.5% = 4 COO- + 6 COOH per 10-MAA chain
  H-bonds: gmx hbond output
  Na+ counterions: gmx editconf/gmx genion setup
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle, Ellipse
import numpy as np

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(22, 13))
fig.patch.set_facecolor('white')

fig.text(0.50, 0.997,
    'Figure 2.  Schematic Molecular Representation of L100 '
    'Conformational Response  (3.5% MAA Deprotonation)',
    ha='center', va='top', fontsize=17, fontweight='bold', color='#1a1a2e')
fig.text(0.25, 0.955,
    '3.5% Deprotonation  |  pH 1.2  \u2014  Compact Coil',
    ha='center', va='top', fontsize=13, fontweight='bold', color='#922B21')
fig.text(0.75, 0.955,
    '3.5% Deprotonation  |  pH 6.8  \u2014  Expanding Coil',
    ha='center', va='top', fontsize=13, fontweight='bold', color='#1A5276')

def draw_panel(ax, tight, panel_label, rg_text, rg_color,
               bg, sphere_col, n_cooh, n_coo, n_mma,
               show_repulsion, show_hydrophobic, show_na,
               n_water, seed):
    ax.set_xlim(-1.52, 1.52); ax.set_ylim(-1.52, 1.52)
    ax.set_aspect('equal'); ax.axis('off')
    ax.set_facecolor(bg)
    np.random.seed(seed)
    sr = 0.78 if tight else 1.16
    sph = Ellipse((0,0), sr*2.05, sr*1.75,
                  facecolor=sphere_col, alpha=0.45,
                  edgecolor='none', zorder=1)
    ax.add_patch(sph)
    th = np.linspace(0, 2*np.pi, 300)
    ax.plot(sr*np.cos(th), sr*0.875*np.sin(th),
            color=sphere_col, alpha=0.50, lw=1.4, zorder=2)
    for a in [30, 60, 90, 120, 150]:
        ph = np.radians(a)
        rx = sr*abs(np.sin(ph))
        ax.plot(rx*np.cos(th), sr*0.875*np.sin(th)*0.50,
                color=sphere_col, alpha=0.25, lw=0.9, zorder=2)
    ax.plot(sr*0.48*np.cos(th), sr*0.875*np.sin(th),
            color=sphere_col, alpha=0.25, lw=0.9, zorder=2)
    n_loops = 3 if tight else 5
    t = np.linspace(0, n_loops*2*np.pi, 700)
    rc = 0.48 if tight else 0.78
    if tight:
        xc = rc*np.cos(t)*(1+0.06*np.sin(2.2*t))
        yc = rc*0.58*np.sin(t)*(1+0.05*np.cos(1.9*t))
    else:
        xc = rc*np.cos(t)*(1+0.18*np.sin(1.8*t))
        yc = rc*0.65*np.sin(t)*(1+0.14*np.cos(2.1*t))
    ax.plot(xc, yc, color='#1C2833', lw=3.5,
            alpha=0.93, zorder=4, solid_capstyle='round')
    n_pts = len(t)
    total = n_cooh + n_coo + n_mma
    step = n_pts // (total + 2)
    coo_idx  = [step*(i+1) for i in range(n_coo)]
    cooh_idx = [step*(n_coo+i+1) for i in range(n_cooh)]
    mma_idx  = [step*(n_coo+n_cooh+i+1) for i in range(n_mma)]
    for idx in coo_idx:
        px, py = xc[idx], yc[idx]
        ax.add_patch(Circle((px,py), 0.085, facecolor='#7D3C98',
                            edgecolor='white', lw=1.8, zorder=6))
        ox = 0.13 if px >= 0 else -0.13
        ax.text(px+ox, py+0.10, 'COO\u207b', fontsize=12.5,
                color='#7D3C98', fontweight='bold', ha='center', zorder=7)
    for idx in cooh_idx:
        px, py = xc[idx], yc[idx]
        ax.add_patch(Circle((px,py), 0.085, facecolor='#C0392B',
                            edgecolor='white', lw=1.8, zorder=6))
        ox = 0.13 if px >= 0 else -0.13
        ax.text(px+ox, py+0.10, 'COOH', fontsize=12.5,
                color='#C0392B', fontweight='bold', ha='center', zorder=7)
    for idx in mma_idx:
        px, py = xc[idx], yc[idx]
        ax.add_patch(Circle((px,py), 0.065, facecolor='#5D6D7E',
                            edgecolor='white', lw=1.4, zorder=6))
    if show_hydrophobic:
        ax.annotate('', xy=(0.08,0.04), xytext=(0.78,0.60),
                    arrowprops=dict(arrowstyle='->',color='#7D3C98',
                                    lw=2.4, mutation_scale=22), zorder=9)
        ax.text(0.82, 0.70, 'Hydrophobic\ncollapse',
                fontsize=13, color='#7D3C98', fontweight='bold',
                ha='left', va='center')
    if show_repulsion:
        for (x1,y1),(x2,y2) in [
            ((-0.28,0.18),(-0.68,0.56)),(( 0.26,0.16),( 0.68,0.54)),
            ((-0.20,-0.26),(-0.60,-0.62)),(( 0.22,-0.24),( 0.62,-0.60))]:
            ax.annotate('', xy=(x2,y2), xytext=(x1,y1),
                        arrowprops=dict(arrowstyle='->',color='#E74C3C',
                                        lw=2.2, mutation_scale=18), zorder=9)
        ax.text(-0.01, 1.30,
                'Electrostatic repulsion\n(COO\u207b\u2013COO\u207b)',
                fontsize=12.5, color='#E74C3C', fontweight='bold',
                ha='center', va='center',
                bbox=dict(boxstyle='round,pad=0.38', facecolor='#FADBD8',
                          alpha=0.92, edgecolor='#E74C3C', lw=1.5))
    r_in = sr*0.95; r_out = sr*1.38
    placed = 0; tries = 0
    while placed < n_water and tries < 800:
        angle = np.random.uniform(0, 2*np.pi)
        r = np.random.uniform(r_in, r_out)
        wx = r*np.cos(angle); wy = r*0.875*np.sin(angle)
        if abs(wx) < 1.43 and abs(wy) < 1.43:
            col = '#5DADE2' if not tight else '#AED6F1'
            ax.plot(wx, wy, 'o', color=col, ms=11,
                    alpha=0.55 if not tight else 0.40,
                    markeredgecolor='white', markeredgewidth=1.0, zorder=3)
            placed += 1
        tries += 1
    if not tight:
        for _ in range(6):
            wx = np.random.uniform(-0.55, 0.55)
            wy = np.random.uniform(-0.45, 0.45)
            ax.plot(wx, wy, 'o', color='#5DADE2', ms=10,
                    alpha=0.44, markeredgecolor='white',
                    markeredgewidth=1.0, zorder=3)
    if show_na:
        for nx,ny in [(0.58,0.82),(-0.68,0.58),(0.80,-0.44),
                      (-0.55,-0.74),(1.18,0.20),(-1.15,0.05)]:
            if abs(nx) < 1.43 and abs(ny) < 1.43:
                tri = plt.Polygon([[nx,ny+0.095],[nx-0.082,ny-0.060],
                                   [nx+0.082,ny-0.060]],
                                  facecolor='#F39C12',
                                  edgecolor='white', lw=1.4, zorder=7)
                ax.add_patch(tri)
                ax.text(nx+0.14, ny+0.04, 'Na\u207a', fontsize=11.5,
                        color='#D68910', fontweight='bold', va='center')
    ax.text(0, 1.44, rg_text, ha='center', va='center',
            fontsize=20, fontweight='bold', color=rg_color)
    lbl = f'{n_coo} COO\u207b + {n_cooh} COOH\nper chain  (3.5% deprotonation)'
    ax.text(0, -1.35, lbl, ha='center', va='center',
            fontsize=13, fontweight='bold', color='#555555')
    ax.text(-1.44, 1.44, panel_label, fontsize=26,
            fontweight='bold', color='#1a1a2e', va='top')

draw_panel(ax1, tight=True, panel_label='(A)',
           rg_text='Rg = 0.920 nm  (pH 1.2)',
           rg_color='#C0392B', bg='#FDF0F0', sphere_col='#E8C4C4',
           n_cooh=6, n_coo=4, n_mma=4,
           show_repulsion=False, show_hydrophobic=True,
           show_na=False, n_water=7, seed=42)

draw_panel(ax2, tight=False, panel_label='(B)',
           rg_text='Rg \u2248 1.050 nm  (pH 6.8,  +14.1%)',
           rg_color='#1A5276', bg='#EEF5FF', sphere_col='#AED6F1',
           n_cooh=6, n_coo=4, n_mma=4,
           show_repulsion=True, show_hydrophobic=False,
           show_na=True, n_water=18, seed=55)

leg = [
    plt.Line2D([0],[0], color='#1C2833', lw=3.5,
               label='L100 polymer backbone'),
    mpatches.Patch(color='#C0392B',
                   label='MAA-COOH  (protonated, acid pH)'),
    mpatches.Patch(color='#7D3C98',
                   label='MAA-COO\u207b  (deprotonated, intestinal pH)'),
    mpatches.Patch(color='#5D6D7E', label='MMA units  (hydrophobic)'),
    plt.Line2D([0],[0], marker='o', color='w',
               markerfacecolor='#5DADE2', ms=13,
               markeredgecolor='white',
               label='Water molecules  (hydration shell)'),
    plt.Line2D([0],[0], marker='^', color='w',
               markerfacecolor='#F39C12', ms=13,
               markeredgecolor='white', label='Na\u207a counterions'),
    plt.Line2D([0],[0], color='#E74C3C', lw=2.2,
               label='Electrostatic repulsion  (COO\u207b-COO\u207b)'),
    plt.Line2D([0],[0], color='#7D3C98', lw=2.2,
               label='Hydrophobic collapse direction'),
    mpatches.Patch(color='#E8C4C4', alpha=0.7,
                   label='Rg sphere  (compact, pH 1.2)'),
    mpatches.Patch(color='#AED6F1', alpha=0.55,
                   label='Rg sphere  (expanding, pH 6.8)'),
]
fig.legend(handles=leg, loc='lower center', fontsize=12,
           ncol=5, framealpha=0.96, frameon=True,
           edgecolor='#AAAAAA', bbox_to_anchor=(0.50, 0.00),
           handlelength=2.0, handleheight=1.3,
           borderpad=0.7, labelspacing=0.6, columnspacing=1.5)

plt.subplots_adjust(left=0.01, right=0.99,
                    top=0.93, bottom=0.12, wspace=0.04)
plt.savefig('figure02_schematic_deprotonation.png',
            dpi=300, bbox_inches='tight', facecolor='white')
print("Saved: figure02_schematic_deprotonation.png")
