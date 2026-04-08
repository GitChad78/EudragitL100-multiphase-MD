load /home/ubupablo78/sim1_L100_PEG/md.gro, PEG_system
hide everything
bg_color white

# Show ALL atoms as sticks with element colors
select L100_peg, PEG_system and index 1-204
select PEG_mol, PEG_system and index 205-1404

# L100 - BLUE THICK CARTOON
show cartoon, L100_peg
color blue, L100_peg
set cartoon_tube_radius, 1.0

# PEG400 - ORANGE STICKS
show sticks, PEG_mol
color orange, PEG_mol
set stick_transparency, 0.5
set stick_radius, 0.3

zoom L100_peg
ray 1200, 900
png /mnt/c/Users/Soham/Desktop/PEG400_BLUE.png, dpi=300
quit
