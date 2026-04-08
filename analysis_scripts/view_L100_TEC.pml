
# L100 + TEC Visualization
load /home/ubupablo78/sim2_L100_TEC/md.gro, L100_TEC
hide everything
show cartoon, L100_TEC
color marine, L100_TEC and resname UNL
color firebrick, L100_TEC and resname TEC
show sticks, L100_TEC and resname TEC
show lines, L100_TEC and resname IPA
color cyan, L100_TEC and resname IPA
set cartoon_transparency, 0.3
zoom L100_TEC
ray 1200, 900
png /home/ubupablo78/simulation_outputs/3D_L100_TEC.png, dpi=300
quit
