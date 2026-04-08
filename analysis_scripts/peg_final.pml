load /home/ubupablo78/sim1_L100_PEG/md.gro, PEG_system
hide everything
bg_color white
set ray_opaque_background, on
select L100_chain, PEG_system and index 1-204
show spheres, L100_chain
color blue, L100_chain
set sphere_scale, 0.3, L100_chain
select PEG_mol, PEG_system and index 205-1404
show spheres, PEG_mol
color orange, PEG_mol
set sphere_scale, 0.2, PEG_mol
set sphere_transparency, 0.4, PEG_mol
center L100_chain
zoom all
set ray_opaque_background, on
ray 1200, 900
png /mnt/c/Users/Soham/Desktop/PEG400_GOOD.png, dpi=300
quit
