load /home/ubupablo78/sim1_L100_PEG/md.gro, PEG_system
hide everything

# Show all atoms as sticks with element colors
show sticks, PEG_system
util.cbag PEG_system

# Color by element
color red, PEG_system and element C
color yellow, PEG_system and element O
color white, PEG_system and element H

# Black background same as TEC image
bg_color black

# Zoom to fit all
zoom PEG_system
ray 1200, 900
png /mnt/c/Users/Soham/Desktop/PEG400_SAME_STYLE1.png, dpi=300
quit
