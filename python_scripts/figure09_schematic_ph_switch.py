"""
Figure 9 - Schematic of pH-switch film behaviour at 3.5%
MAA deprotonation (Phase 3).
Authors: Vaibhav Ambudkar, Rashmi Chauhan, Soham Ambudkar
GitHub: https://github.com/GitChad78/EudragitL100-multiphase-MD
Zenodo: https://doi.org/10.5281/zenodo.19471701
Data sources:
  Rg pH 1.2: ~0.920 nm - gmx gyrate (Table S9, ESI)
  Inter-chain pH 1.2: ~2.1 nm - gmx distance (Table S9, ESI)
  Inter-chain pH 6.8: >2.5 nm - gmx distance (Table S9, ESI)
  TEC MSD ratio: ~3x higher at pH 6.8 - gmx msd (Table S9, ESI)
  Water uptake pH 1.2: ~141-145 molecules - gmx mindist (Table S9, ESI)
  Deprotonation: 3.5% = 4 COO- + 6 COOH per chain (both panels)
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

print("Figure 9 - Schematic: pH-switch acid vs intestinal film")
print("Output: figure09_schematic_ph_switch.png (300 dpi)")
print("Key data:")
print("  Rg pH 1.2: ~0.920 nm (gmx gyrate, Table S9 ESI)")
print("  Inter-chain pH 1.2: ~2.1 nm (gmx distance, Table S9 ESI)")
print("  Inter-chain pH 6.8: >2.5 nm (gmx distance, Table S9 ESI)")
print("  TEC MSD: ~3x higher at pH 6.8 (gmx msd, Table S9 ESI)")
print("  Water uptake pH 1.2: ~141-145 molecules (Table S9 ESI)")
