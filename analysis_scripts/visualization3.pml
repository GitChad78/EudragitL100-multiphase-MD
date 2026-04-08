# ════════════════════════════════
# IMAGE 1: L100 + PEG400 ONLY
# ════════════════════════════════
load /home/ubupablo78/sim1_L100_PEG/md.gro, L100_PEG400
hide everything, L100_PEG400

# L100 polymer - blue cartoon
select L100_sim1, L100_PEG400 and index 1-204
show cartoon, L100_sim1
color marine, L100_sim1
set cartoon_tube_radius, 0.4

# PEG400 - orange sticks
select PEG_sim1, L100_PEG400 and index 205-1404
show sticks, PEG_sim1
color orange, PEG_sim1
set stick_radius, 0.2

# Settings
bg_color white
set depth_cue, 1
set ray_shadows, 1
set ambient, 0.4
set ray_trace_mode, 1
zoom L100_PEG400
ray 1200, 900
png /mnt/c/Users/Soham/Desktop/3D_L100_PEG400_FINAL.png, dpi=300
print "Image 1 saved: L100+PEG400"

# ════════════════════════════════
# IMAGE 2: L100 + TEC ONLY
# ════════════════════════════════
load /home/ubupablo78/sim2_L100_TEC/md.gro, L100_TEC
hide everything, L100_TEC

# L100 polymer - red cartoon
select L100_sim2, L100_TEC and index 1-204
show cartoon, L100_sim2
color firebrick, L100_sim2
set cartoon_tube_radius, 0.4

# TEC - green sticks
select TEC_sim2, L100_TEC and index 205-7368
show sticks, TEC_sim2
color green, TEC_sim2
set stick_radius, 0.2

# Settings
bg_color white
zoom L100_TEC
ray 1200, 900
png /mnt/c/Users/Soham/Desktop/3D_L100_TEC_FINAL.png, dpi=300
print "Image 2 saved: L100+TEC"

quit
