import datetime
import pandas as pd
from math import *

# Time of the month selection
now = datetime.datetime.now()

month = now.month

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

# Auxiliary Calculations

LonMT_T = LonMT.transpose()
LonT_T = LonT.transpose()

LatMT_c = LatMT[0].tolist()
LonMT_c = LonMT_T[0].tolist()

LatT_c = LatT[0].tolist()
LonT_c = LonT_T[0].tolist()

T_Data = [TJan, TFeb, TMar, TApr, TMay, TJun, TJul, TAug, TSep, TOct, TNov, TDec]
MT_Data = [MTJan, MTFeb, MTMar, MTApr, MTMay, MTJun, MTJul, MTAug, MTSep, MTOct, MTNov, MTDec]

# Data Input

print("Enter your desired latitude")
lat = float(input())
print("Enter your desired longitude")
lon = float(input())

# Step 1

Nii = [31, 28.25, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Step 2

# Longitude T
LonMT_CV = min(LonT_c, key=lambda x: abs(x-lon))
T_pos_lon = LonT_c.index(LonMT_CV)

T_aux_1 = LonMT_CV - lon

if T_aux_1 > 0:
    T_pos_lon_r = T_pos_lon
    T_pos_lon_l = T_pos_lon - 1
    TLon_R = LonT_c[T_pos_lon_r]
    TLon_L = LonT_c[T_pos_lon_l]
else:
    T_pos_lon_l = T_pos_lon
    T_pos_lon_r = T_pos_lon + 1
    TLon_R = LonT_c[T_pos_lon_r]
    TLon_L = LonT_c[T_pos_lon_l]

print("The closest numbers to", lon, "are:", TLon_L, "and", TLon_R, "and their positions are",
      T_pos_lon_l, "and", T_pos_lon_r)

# Latitude T
LatMT_CV = min(LonT_c, key=lambda x: abs(x-lat))
T_pos_lat = LatT_c.index(LatMT_CV)

T_aux_2 = LatMT_CV - lat

if T_aux_2 > 0:
    T_pos_lat_t = T_pos_lat
    T_pos_lat_b = T_pos_lat - 1
    TLat_T = LatT_c[T_pos_lat_t]
    TLat_B = LatT_c[T_pos_lat_b]
else:
    T_pos_lat_b = T_pos_lat
    T_pos_lat_t = T_pos_lat + 1
    TLat_T = LatT_c[T_pos_lat_t]
    TLat_B = LatT_c[T_pos_lat_b]

print("The closest numbers to", lat, "are:", TLat_B, "and", TLat_T, "and their positions are",
      T_pos_lat_b, "and", T_pos_lat_t)

T_i1 = T_Data[month-1].loc[T_pos_lat_b, T_pos_lon_l]
T_i2 = T_Data[month-1].loc[T_pos_lat_t, T_pos_lon_l]
T_i3 = T_Data[month-1].loc[T_pos_lat_b, T_pos_lon_r]
T_i4 = T_Data[month-1].loc[T_pos_lat_t, T_pos_lon_r]

T_t = (lat - TLat_B)/(TLat_T-TLat_B)
T_s = (lon - TLon_L)/(TLon_R - TLon_L)

# Final value of T
TF = (1 - T_s)*(1 - T_t)*T_i1 + (1 - T_s)*T_t*T_i2 + T_s*(1 - T_t)*T_i3 + T_t*T_s*T_i4

print("T = ", TF, "K")

print("It's Surrounding values are:", T_i2, T_i3, T_i1, T_i4)

# Step 3

# Longitude MT
LonMT_CV = min(LonMT_c, key=lambda x: abs(x-lon))
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
LatMT_CV = min(LonMT_c, key=lambda x: abs(x-lat))
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

MT_i1 = MT_Data[month-1].loc[MT_pos_lat_b, MT_pos_lon_l]
MT_i2 = MT_Data[month-1].loc[MT_pos_lat_t, MT_pos_lon_l]
MT_i3 = MT_Data[month-1].loc[MT_pos_lat_b, MT_pos_lon_r]
MT_i4 = MT_Data[month-1].loc[MT_pos_lat_t, MT_pos_lon_r]

MT_t = (lat - MTLat_B)/(MTLat_T-MTLat_B)
MT_s = (lon - MTLon_L)/(MTLon_R - MTLon_L)

# Final value of MT
MTF = (1 - MT_s)*(1 - MT_t)*MT_i1 + (1 - MT_s)*MT_t*MT_i2 + MT_s*(1 - MT_t)*MT_i3 + MT_t*MT_s*MT_i4

print("MT = ", MTF)

print("It's Surrounding values are:", MT_i2, MT_i3, MT_i1, MT_i4)

# Step 4

tii = TF - 273.15
print("tii = ", tii, "°C")

# Step 5

if tii >= 0:
    rii = 0.5874*exp(0.0883*tii)
else:
    rii = 0.5874

print("rii = ", rii)

# Step 6a

T_i1_1 = [0] * 12
T_i2_1 = [0] * 12
T_i3_1 = [0] * 12
T_i4_1 = [0] * 12
Tii = [0] * 12

MT_i1_1 = [0] * 12
MT_i2_1 = [0] * 12
MT_i3_1 = [0] * 12
MT_i4_1 = [0] * 12
MTii = [0] * 12
rii = [0] * 12
P0ii = [0] * 12

for aux_month in range(0, 12):

    T_i1_1[aux_month] = T_Data[aux_month].loc[T_pos_lat_b, T_pos_lon_l]
    T_i2_1[aux_month] = T_Data[aux_month].loc[T_pos_lat_t, T_pos_lon_l]
    T_i3_1[aux_month] = T_Data[aux_month].loc[T_pos_lat_b, T_pos_lon_r]
    T_i4_1[aux_month] = T_Data[aux_month].loc[T_pos_lat_t, T_pos_lon_r]
    
    MT_i1_1[aux_month] = MT_Data[aux_month].loc[MT_pos_lat_b, MT_pos_lon_l]
    MT_i2_1[aux_month] = MT_Data[aux_month].loc[MT_pos_lat_t, MT_pos_lon_l]
    MT_i3_1[aux_month] = MT_Data[aux_month].loc[MT_pos_lat_b, MT_pos_lon_r]
    MT_i4_1[aux_month] = MT_Data[aux_month].loc[MT_pos_lat_t, MT_pos_lon_r]

    Tii[aux_month] = ((1 - T_s) * (1 - T_t) * T_i1_1[aux_month] + (1 - T_s) * T_t * T_i2_1[aux_month] +
                      T_s * (1 - T_t) * T_i3_1[aux_month] + T_t * T_s * T_i4_1[aux_month]) - 273.15
    
    MTii[aux_month] = ((1 - MT_s) * (1 - MT_t) * MT_i1_1[aux_month] + (1 - MT_s) * MT_t * MT_i2_1[aux_month] +
                       MT_s * (1 - MT_t) * MT_i3_1[aux_month] + MT_t * MT_s * MT_i4_1[aux_month])

    if Tii[aux_month] >= 0:
        rii[aux_month] = 0.5874*exp(0.0883*Tii[aux_month])
    else:
        rii[aux_month] = 0.5874

    P0ii[aux_month] = (100 * MTii[aux_month]) / (24 * Nii[aux_month] * rii[aux_month])

print(Tii[month-1])

print(MTii[month-1])

print(rii[month-1])

print(P0ii[month-1])

# Step 6b

P0an = [0]*12

# for aux_month_1 in range (0,12):
