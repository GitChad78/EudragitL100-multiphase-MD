"""
Figure 7 - Schematic of multi-chain L100 film structure
and water barrier effect (Phase 2 and Phase 5).
Authors: Vaibhav Ambudkar, Rashmi Chauhan, Soham Ambudkar
GitHub: https://github.com/GitChad78/EudragitL100-multiphase-MD
Zenodo: https://doi.org/10.5281/zenodo.19471701
Data sources:
  Film density 5-chain: 845 kg/m3 - gmx density (Table S8, ESI)
  D_bulk SPC/E water: 2.5e-9 m2/s (reference value)
  D_film: <2.0e-9 m2/s - gmx msd (Table S8, ESI)
  TEC retained in film: gmx mindist analysis
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

print("Figure 7 - Schematic: Multi-chain film structure and water barrier")
print("Output: figure07_schematic_film_barrier.png (300 dpi)")
print("Key data:")
print("  Film density 5-chain: 845 kg/m3 (gmx density, Table S8 ESI)")
print("  D_bulk SPC/E: 2.5e-9 m2/s (reference)")
print("  D_film: <2.0e-9 m2/s (gmx msd, Table S8 ESI)")
