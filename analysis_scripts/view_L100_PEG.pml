
# L100 + PEG400 Visualization
load /home/ubupablo78/sim1_L100_PEG/md.gro, L100_PEG
hide everything
show cartoon, L100_PEG
color marine, L100_PEG and resname UNL
color orange, L100_PEG and resname PEG
show sticks, L100_PEG and resname PEG
show lines, L100_PEG and resname IPA
color cyan, L100_PEG and resname IPA
set cartoon_transparency, 0.3
zoom L100_PEG
ray 1200, 900
png /home/ubupablo78/simulation_outputs/3D_L100_PEG.png, dpi=300
quit
