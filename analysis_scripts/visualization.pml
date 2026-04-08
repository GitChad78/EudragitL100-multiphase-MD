load /home/ubupablo78/sim1_L100_PEG/md.gro, L100_PEG400
load /home/ubupablo78/sim2_L100_TEC/md.gro, L100_TEC
hide everything
show cartoon, L100_PEG400
color marine, L100_PEG400
show cartoon, L100_TEC
color firebrick, L100_TEC
hide everything, resname IPA
hide everything, resname SOL
bg_color white
hide everything, L100_TEC
zoom L100_PEG400
ray 1200, 900
png /mnt/c/Users/Soham/Desktop/3D_L100_PEG400_final.png, dpi=300
show cartoon, L100_TEC
hide everything, L100_PEG400
zoom L100_TEC
ray 1200, 900
png /mnt/c/Users/Soham/Desktop/3D_L100_TEC_final.png, dpi=300
show cartoon, L100_PEG400
zoom
ray 1200, 900
png /mnt/c/Users/Soham/Desktop/3D_Both_Structures.png, dpi=300
quit
