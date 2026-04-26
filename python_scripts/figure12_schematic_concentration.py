"""
Figure 12 - Schematic of the molecular basis for the practical
L100 concentration window (Phase 5).
Authors: Vaibhav Ambudkar, Rashmi Chauhan, Soham Ambudkar
GitHub: https://github.com/GitChad78/EudragitL100-multiphase-MD
Zenodo: https://doi.org/10.5281/zenodo.19471701
Data sources:
  phi = N_chains x V_chain / V_box
  V_chain = 4.33 nm3 (M=3100 Da, rho_pure=1190 kg/m3, NA=6.022e23)
  %w/v = (phi x rho_film) / 10  [rho_film from Table S8 ESI]
  Film densities: 812,845,876,901 kg/m3 (2,5,8,12 chains) Table S8 ESI
  c* at phi 0.009-0.022 (~0.7-1.8% w/v)
  Practical range: 5-10% w/v = phi 0.057-0.114
  H-bonds: 3.2-24.3/frame - gmx hbond (Table S11, ESI)
  E-mod proxy: 0.8-9.7 MPa - gmx energy pressure tensor (Table S11, ESI)
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

print("Figure 12 - Schematic: c* onset and practical coating range")
print("Output: figure12_schematic_concentration.png (300 dpi)")
print("Key data:")
print("  V_chain = 4.33 nm3 (M=3100 Da, rho=1190 kg/m3)")
print("  phi = N_chains x V_chain / V_box")
print("  %w/v = (phi x rho_film) / 10 (Table S8 ESI)")
print("  c* at phi 0.009-0.022 (~0.7-1.8% w/v)")
print("  Practical: 5-10% w/v = phi 0.057-0.114")
print("  H-bonds 17.5-24.3/frame (Table S11 ESI)")
print("  E-mod ~7-10 MPa (Table S11 ESI)")
