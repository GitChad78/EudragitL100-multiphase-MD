#!/bin/bash
# ============================================================
# Eudragit L100 Multi-Phase MD - GROMACS 2025.4 Analysis Pipeline
# Run from the directory containing your .xtc and .tpr files
# ============================================================

echo === Radius of Gyration ===
gmx gyrate -f md.xtc -s md.tpr -o rg.xvg

echo === SASA ===
gmx sasa -f md.xtc -s md.tpr -o sasa.xvg -probe 0.14

echo === Hydrogen Bonds ===
gmx hbond -f md.xtc -s md.tpr -num hbnum.xvg

echo === Mean Square Displacement ===
gmx msd -f md.xtc -s md.tpr -o msd.xvg -b 200 -e 800

echo === Radial Distribution Function ===
gmx rdf -f md.xtc -s md.tpr -o rdf.xvg

echo === Z-axis Density Profile ===
gmx density -f md.xtc -s md.tpr -o density.xvg -d Z -sl 50

echo === Potential Energy ===
gmx energy -f md.edr -o energy.xvg

echo === Inter-chain COM Distance ===
gmx distance -f md.xtc -s md.tpr -oav dist.xvg

echo === Analysis complete. All .xvg files ready for plotting ===
