import datetime
import pandas as pd
from math import *

# Data Loading

# Latitude and Longitude of the Monthly Mean Total Rainfall
LonMT = pd.read_csv('Data/LON_MT.TXT', sep=" ", header=None)
LatMT = pd.read_csv('Data/LAT_MT.TXT', sep=" ", header=None)
# Monthly Mean Total Rainfall
MTJan = pd.read_csv('Data/MT_Month01.TXT', sep=" ", header=None)
MTFeb = pd.read_csv('Data/MT_Month02.TXT', sep=" ", header=None)
MTMar = pd.read_csv('Data/MT_Month03.TXT', sep=" ", header=None)
MTApr = pd.read_csv('Data/MT_Month04.TXT', sep=" ", header=None)
MTMay = pd.read_csv('Data/MT_Month05.TXT', sep=" ", header=None)
MTJun = pd.read_csv('Data/MT_Month06.TXT', sep=" ", header=None)
MTJul = pd.read_csv('Data/MT_Month07.TXT', sep=" ", header=None)
MTAug = pd.read_csv('Data/MT_Month08.TXT', sep=" ", header=None)
MTSep = pd.read_csv('Data/MT_Month09.TXT', sep=" ", header=None)
MTOct = pd.read_csv('Data/MT_Month10.TXT', sep=" ", header=None)
MTNov = pd.read_csv('Data/MT_Month11.TXT', sep=" ", header=None)
MTDec = pd.read_csv('Data/MT_Month12.TXT', sep=" ", header=None)
# Latitude and Longitude of the Monthly Mean Surface Temperature
LonT = pd.read_csv('Data/LON_T.TXT', sep=" ", header=None)
LatT = pd.read_csv('Data/LAT_T.TXT', sep=" ", header=None)
# Monthly Mean Surface Temperature
TJan = pd.read_csv('Data/T_Month01.TXT', sep=" ", header=None)
TFeb = pd.read_csv('Data/T_Month02.TXT', sep=" ", header=None)
TMar = pd.read_csv('Data/T_Month03.TXT', sep=" ", header=None)
TApr = pd.read_csv('Data/T_Month04.TXT', sep=" ", header=None)
TMay = pd.read_csv('Data/T_Month05.TXT', sep=" ", header=None)
TJun = pd.read_csv('Data/T_Month06.TXT', sep=" ", header=None)
TJul = pd.read_csv('Data/T_Month07.TXT', sep=" ", header=None)
TAug = pd.read_csv('Data/T_Month08.TXT', sep=" ", header=None)
TSep = pd.read_csv('Data/T_Month09.TXT', sep=" ", header=None)
TOct = pd.read_csv('Data/T_Month10.TXT', sep=" ", header=None)
TNov = pd.read_csv('Data/T_Month11.TXT', sep=" ", header=None)
TDec = pd.read_csv('Data/T_Month12.TXT', sep=" ", header=None)
# Latitude and Longitude of R001
LonR_ref = pd.read_csv('Data/LON_R001.TXT', sep=" ", header=None)
LatR_ref = pd.read_csv('Data/LAT_R001.TXT', sep=" ", header=None)
# Rainfall Rate Exceeded for 0.01% of an Average Year
R001 = pd.read_csv('Data/R001.TXT', sep=" ", header=None)

# Auxiliary Calculations

LonMT_T = LonMT.transpose()
LonT_T = LonT.transpose()
LonR_ref_T = LonR_ref.transpose()

LatMT_c = LatMT[0].tolist()
LonMT_c = LonMT_T[0].tolist()

LatT_c = LatT[0].tolist()
LonT_c = LonT_T[0].tolist()

LatR_c = LatR_ref[0].tolist()
LonR_c = LonR_ref_T[0].tolist()

T_Data = [TJan, TFeb, TMar, TApr, TMay, TJun, TJul, TAug, TSep, TOct, TNov, TDec]
MT_Data = [MTJan, MTFeb, MTMar, MTApr, MTMay, MTJun, MTJul, MTAug, MTSep, MTOct, MTNov, MTDec]
R_Data = R001

# Data Input

print("Enter your desired latitude")
lat = float(input())
print("Enter your desired longitude")
lon = float(input())
print("Enter your desired probability")
p = float(input())

# Step 1

# Time of the month selection
now = datetime.datetime.now()
month = now.month - 1

Nii = [31, 28.25, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Step 2

# Longitude T
LonMT_CV = min(LonT_c, key=lambda x: abs(x - lon))
T_pos_lon = LonT_c.index(LonMT_CV)

T_aux_1 = LonMT_CV - lon

if T_aux_1 >= 0:
    T_pos_lon_r = T_pos_lon
    T_pos_lon_l = T_pos_lon - 1
    TLon_R = LonT_c[T_pos_lon_r]
    TLon_L = LonT_c[T_pos_lon_l]
else:
    T_pos_lon_l = T_pos_lon
    T_pos_lon_r = T_pos_lon + 1
    TLon_R = LonT_c[T_pos_lon_r]
    TLon_L = LonT_c[T_pos_lon_l]

# print("The closest numbers to", lon, "are:", TLon_L, "and", TLon_R, "and their positions are",
#      T_pos_lon_l, "and", T_pos_lon_r)

# Latitude T
LatMT_CV = min(LatT_c, key=lambda x: abs(x - lat))
T_pos_lat = LatT_c.index(LatMT_CV)

T_aux_2 = LatMT_CV - lat

if T_aux_2 >= 0:
    T_pos_lat_t = T_pos_lat
    T_pos_lat_b = T_pos_lat - 1
    TLat_T = LatT_c[T_pos_lat_t]
    TLat_B = LatT_c[T_pos_lat_b]
else:
    T_pos_lat_b = T_pos_lat
    T_pos_lat_t = T_pos_lat + 1
    TLat_T = LatT_c[T_pos_lat_t]
    TLat_B = LatT_c[T_pos_lat_b]

# print("The closest numbers to", lat, "are:", TLat_B, "and", TLat_T, "and their positions are",
#      T_pos_lat_b, "and", T_pos_lat_t)

T_i1 = [0] * 12
T_i2 = [0] * 12
T_i3 = [0] * 12
T_i4 = [0] * 12
Tii = [0] * 12

T_t = (lat - TLat_B) / (TLat_T - TLat_B)
T_s = (lon - TLon_L) / (TLon_R - TLon_L)

for aux_month_t in range(0, 12):

    T_i1[aux_month_t] = T_Data[aux_month_t].loc[T_pos_lat_b, T_pos_lon_l]
    T_i2[aux_month_t] = T_Data[aux_month_t].loc[T_pos_lat_t, T_pos_lon_l]
    T_i3[aux_month_t] = T_Data[aux_month_t].loc[T_pos_lat_b, T_pos_lon_r]
    T_i4[aux_month_t] = T_Data[aux_month_t].loc[T_pos_lat_t, T_pos_lon_r]

    Tii[aux_month_t] = ((1 - T_s) * (1 - T_t) * T_i1[aux_month_t] + (1 - T_s) * T_t * T_i2[aux_month_t] +
                        T_s * (1 - T_t) * T_i3[aux_month_t] + T_t * T_s * T_i4[aux_month_t])

print("\nStep 2. Value of Temperature for this month")
print("T = ", Tii[month], "K")

print("It's Surrounding values are:", T_i2[month], T_i3[month], T_i1[month], T_i4[month])

# Step 3

# Longitude MT
LonMT_CV = min(LonMT_c, key=lambda x: abs(x - lon))
MT_pos_lon = LonMT_c.index(LonMT_CV)

MT_aux_1 = LonMT_CV - lon

if MT_aux_1 > 0:
    MT_pos_lon_r = MT_pos_lon
    MT_pos_lon_l = MT_pos_lon - 1
    MTLon_R = LonMT_c[MT_pos_lon_r]
    MTLon_L = LonMT_c[MT_pos_lon_l]
else:
    MT_pos_lon_l = MT_pos_lon
    MT_pos_lon_r = MT_pos_lon + 1
    MTLon_R = LonMT_c[MT_pos_lon_r]
    MTLon_L = LonMT_c[MT_pos_lon_l]

# Latitude MT
LatMT_CV = min(LatMT_c, key=lambda x: abs(x - lat))
MT_pos_lat = LatMT_c.index(LatMT_CV)

MT_aux_2 = LatMT_CV - lat

if MT_aux_2 > 0:
    MT_pos_lat_t = MT_pos_lat
    MT_pos_lat_b = MT_pos_lat - 1
    MTLat_T = LatMT_c[MT_pos_lat_t]
    MTLat_B = LatMT_c[MT_pos_lat_b]
else:
    MT_pos_lat_b = MT_pos_lat
    MT_pos_lat_t = MT_pos_lat + 1
    MTLat_T = LatMT_c[MT_pos_lat_t]
    MTLat_B = LatMT_c[MT_pos_lat_b]

MT_i1 = [0] * 12
MT_i2 = [0] * 12
MT_i3 = [0] * 12
MT_i4 = [0] * 12
MTii = [0]*12

MT_t = (lat - MTLat_B) / (MTLat_T - MTLat_B)
MT_s = (lon - MTLon_L) / (MTLon_R - MTLon_L)

for aux_month_mt in range(0, 12):

    MT_i1[aux_month_mt] = MT_Data[aux_month_mt].loc[MT_pos_lat_b, MT_pos_lon_l]
    MT_i2[aux_month_mt] = MT_Data[aux_month_mt].loc[MT_pos_lat_t, MT_pos_lon_l]
    MT_i3[aux_month_mt] = MT_Data[aux_month_mt].loc[MT_pos_lat_b, MT_pos_lon_r]
    MT_i4[aux_month_mt] = MT_Data[aux_month_mt].loc[MT_pos_lat_t, MT_pos_lon_r]

    MTii[aux_month_mt] = ((1 - MT_s) * (1 - MT_t) * MT_i1[aux_month_mt] + (1 - MT_s) * MT_t * MT_i2[aux_month_mt] +
                          MT_s * (1 - MT_t) * MT_i3[aux_month_mt] + MT_t * MT_s * MT_i4[aux_month_mt])
print("\nStep 3. Value of MT for this month")
print("MT = ", MTii[month])

print("It's Surrounding values are:", MT_i2[month], MT_i3[month], MT_i1[month], MT_i4[month])

# Step 4

tii = [0] * 12

for aux_temp in range(0, 12):
    tii[aux_temp] = Tii[aux_temp] - 273.15

print("\nStep 4. Temperature from K to °C")
print("tii = ", tii[month], "°C")

# Step 5

rii = [0]*12

for aux_rii in range(0, 12):
    if tii[aux_rii] >= 0:
        rii[aux_rii] = 0.5874 * exp(0.0883 * tii[aux_rii])
    else:
        rii[aux_rii] = 0.5874

print("\nStep 5. Value of Rii")
print("rii = ", rii[month])

# Step 6a

P0ii = [0] * 12

for aux_p0ii in range(0, 12):
    P0ii[aux_p0ii] = (100 * MTii[aux_p0ii]) / (24 * Nii[aux_p0ii] * rii[aux_p0ii])

print("\nStep 6a. Value of P0ii for this month")
print("P0ii = ", P0ii[month], "%")

# Step 6b

for aux_month_1 in range(0, 12):
    if P0ii[aux_month_1] > 70:
        P0ii[aux_month_1] = 70
        rii[aux_month_1] = (100*MTii[aux_month_1])/(70*24*Nii[aux_month_1])

print("\nStep 6b. New Values of P0ii and rii")
print("rii = ", rii[month])
print("P0ii = ", P0ii[month])

# Step 7

aux_s7_1 = [0]*12
aux_s7_2 = [0]*12

for aux_month_2 in range(0, 12):
    aux_s7_1[aux_month_2] = Nii[aux_month_2]*P0ii[aux_month_2]

P0an = sum(aux_s7_1) / sum(Nii)

print("\nStep 7. Value of P0 annual")
print("P0annual = ", P0an, "%")

# Step 8

# Longitude R001

LonR_CV = min(LonR_c, key=lambda x: abs(x - lon))
R_pos_lon = LonR_c.index(LonR_CV)

R_aux_1 = LonR_CV - lon

if R_aux_1 >= 0:
    R_pos_lon_r = R_pos_lon
    R_pos_lon_l = R_pos_lon - 1
    RLon_R = LonR_c[R_pos_lon_r]
    RLon_L = LonR_c[R_pos_lon_l]
else:
    R_pos_lon_l = R_pos_lon
    R_pos_lon_r = R_pos_lon + 1
    RLon_R = LonR_c[R_pos_lon_r]
    RLon_L = LonR_c[R_pos_lon_l]

# Latitude R001
LatR_CV = min(LatR_c, key=lambda x: abs(x - lat))
R_pos_lat = LatR_c.index(LatR_CV)

R_aux_2 = LatR_CV - lat

if R_aux_2 >= 0:
    R_pos_lat_t = R_pos_lat
    R_pos_lat_b = R_pos_lat - 1
    RLat_T = LatR_c[R_pos_lat_t]
    RLat_B = LatR_c[R_pos_lat_b]
else:
    R_pos_lat_b = R_pos_lat
    R_pos_lat_t = R_pos_lat + 1
    RLat_T = LatR_c[R_pos_lat_t]
    RLat_B = LatR_c[R_pos_lat_b]

R_t = (lat - RLat_B) / (RLat_T - RLat_B)
R_s = (lon - RLon_L) / (RLon_R - RLon_L)

R_i1 = R_Data.loc[R_pos_lat_b, R_pos_lon_l]
R_i2 = R_Data.loc[R_pos_lat_t, R_pos_lon_l]
R_i3 = R_Data.loc[R_pos_lat_b, R_pos_lon_r]
R_i4 = R_Data.loc[R_pos_lat_t, R_pos_lon_r]

R_ref = ((1 - R_s) * (1 - R_t) * R_i1 + (1 - R_s) * R_t * R_i2 +
         R_s * (1 - R_t) * R_i3 + R_t * R_s * R_i4)

print("\nR_ref = ", R_ref, "mm/h")

print("It's Surrounding values are:", R_i2, R_i3, R_i1, R_i4)

aux_s8_1 = [0]*12
aux_s8_2 = [0]*12
aux_s8_3 = [0]*12
Pii = [0]*12

for aux_step8 in range(0, 12):
    aux_s8_1[aux_step8] = (log(R_ref)+0.7938-log(rii[aux_step8]))/1.26
    Pii[aux_step8] = 0.5*P0ii[aux_step8]*erfc(aux_s8_1[aux_step8]/sqrt(2))
    aux_s8_2[aux_step8] = Nii[aux_step8]*Pii[aux_step8]

P = sum(aux_s8_2) / sum(Nii)
print("\nP(R>R_ref) = ", P)

rel_er = 100 * abs((P / p)-1)
print("\nRelative error = ", rel_er)

if p > P0an:
    Rp = 0
else:
    R_low = 0
    R_high = 500
    while rel_er > 1e-3:
        if P < p:
            R_high = R_ref
        else:
            R_low = R_ref
        R_ref = (R_low + R_high)/2
        for aux_ref in range(0, 12):
            aux_s8_1[aux_ref] = (log(R_ref) + 0.7938 - log(rii[aux_ref])) / 1.26
            Pii[aux_ref] = 0.5 * P0ii[aux_ref] * erfc(aux_s8_1[aux_ref] / sqrt(2))
            aux_s8_3[aux_ref] = Nii[aux_ref] * Pii[aux_ref]
        P = sum(aux_s8_3) / sum(Nii)
        rel_er = 100 * abs((P / p) - 1)
    Rp = R_ref
print("The value of Rp is: ", Rp)
print("Final Relative Error is", rel_er)

