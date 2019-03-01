MTii = 20.008
Nii = 28.25
P0ii = 90
rii = 0.5874

if P0ii > 70:
    P0ii = 70
    rii = (100*MTii)/(70*24*Nii)
else:
    P0ii = P0ii
    rii = rii

print(P0ii, rii)
