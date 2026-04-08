load /home/ubupablo78/sim1_L100_PEG/md.gro, L100_PEG400
hide everything, L100_PEG400

# L100 = first 204 atoms - RED CARTOON
select L100_chain, L100_PEG400 and index 1-204
show cartoon, L100_chain
color red, L100_chain

# PEG400 - ORANGE TRANSPARENT STICKS
select PEG_only, L100_PEG400 and index 205-1404
show sticks, PEG_only
color orange, PEG_only
set stick_transparency, 0.6

bg_color white
zoom L100_chain
ray 1200, 900
png /mnt/c/Users/Soham/Desktop/3D_L100_PEG400_RED.png, dpi=300
quit
