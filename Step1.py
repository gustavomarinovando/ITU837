import datetime

now = datetime.datetime.now()

month = now.month

if month == 1:
    Nii = 31
elif month == 2:
    Nii = 28.25
elif month == 3:
    Nii = 31
elif month == 4:
    Nii = 30
elif month == 5:
    Nii = 31
elif month == 6:
    Nii = 30
elif month == 7:
    Nii = 31
elif month == 8:
    Nii = 31
elif month == 9:
    Nii = 30
elif month == 10:
    Nii = 31
elif month == 11:
    Nii = 30
else:
    Nii = 31

print("La cantidad de dias en este mes son:", Nii)
