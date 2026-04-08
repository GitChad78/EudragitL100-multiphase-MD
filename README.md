# Eudragit L100 Multi-Phase All-Atom MD Simulation

Manuscript submitted to RSC Pharmaceuticals, 2025

## Software and Hardware
- GROMACS 2025.4
- GAFF2 Force Field (acpype v2.1)
- SPC/E Water Model
- Ubuntu 22.04 LTS / NVIDIA RTX 5050 GPU

## Repository Structure
- python_scripts/: Figure generation scripts (Figures 1-7, S1-S7)
- gromacs_mdp/: All .mdp parameter files (em, nvt, npt, md)
- topology/: Force field files (.itp, .mol2) for L100, TEC, PEG400
- analysis_scripts/: GROMACS analysis pipeline (run_analysis.sh)

## Simulation Phases
- Phase 0:  Deprotonation series 0-10% | 7 systems | 1 ns each
- Phase 0b: PEG400 vs TEC plasticizer | 2 systems | 50 ns each
- Phase 1:  TEC concentration 10-40% w/w | 4 systems | 1 ns each
- Phase 2:  5-chain film model | 1 system | 2 ns
- Phase 3:  pH-switch 1.2 vs 6.8 | 2 systems | 2 ns each
- Phase 4:  Counterion effects NaCl/NaHCO3/Na2CO3 | 3 systems | 1 ns each
- Phase 5:  Concentration series 2-12 chains | 4 systems | 2 ns each

## Force Field Parameters
- L100 (MAA-MMA copolymer): GAFF2, AM1-BCC charges via acpype
- TEC (Triethyl Citrate): GAFF2, AM1-BCC charges via acpype
- PEG400: OPLS-AA
- Water: SPC/E | Ions: NaCl 150 mM

## Raw Data and Trajectories
All .xvg output files and .xtc trajectories deposited on Zenodo:
DOI: 10.5281/zenodo.19471701

## Reproducing the Analysis
1. Install GROMACS 2025.4
2. Use topology/ files to rebuild systems
3. Run equilibration using gromacs_mdp/ in order: em, nvt, npt, md
4. Run analysis_scripts/run_analysis.sh to reproduce all .xvg data
5. Run python_scripts/ to reproduce all figures
