import pandas as pd

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

LonMT_T = LonMT.transpose()
LonT_T = LonT.transpose()

LatMT_c = LatMT[0].tolist()
LonMT_c = LonMT_T[0].tolist()

LatT_c = LatT[0].tolist()
LonT_c = LonT_T[0].tolist()

# print("Initial values from MT:", LonMT_c[0], LatMT_c[0], "Final values from MT", LonMT_c[1441], LatMT_c[721])
# print("Initial values from T:", LonT_c[0], LatT_c[0], "Final values from T", LonT_c[480], LatT_c[240])

print("Enter your desired latitude and longitude")

lat = 22.9
lon = -43.23

# lat = float(input())
# lon = float(input())

print("Your longitude is :", lon)
print("Your latitude is:", lat)

# Longitude MT
LonMT_CV = min(LonMT_c, key=lambda x: abs(x-lon))
pos_lon = LonMT_c.index(LonMT_CV)

aux = LonMT_CV - lon

if aux > 0:
    pos_lon_r = pos_lon
    pos_lon_l = pos_lon - 1
    MTLon_R = LonMT_c[pos_lon_r]
    MTLon_L = LonMT_c[pos_lon_l]
else:
    pos_lon_l = pos_lon
    pos_lon_r = pos_lon + 1
    MTLon_R = LonMT_c[pos_lon_r]
    MTLon_L = LonMT_c[pos_lon_l]

print("The closest numbers to", lon, "are:", MTLon_L, "and", MTLon_R, "and their positions are",
      pos_lon_l, "and", pos_lon_r)

# Latitude MT
LatMT_CV = min(LonMT_c, key=lambda x: abs(x-lat))
pos_lat = LatMT_c.index(LatMT_CV)

aux1 = LatMT_CV - lat

if aux1 > 0:
    pos_lat_t = pos_lat
    pos_lat_b = pos_lat - 1
    MTLat_T = LatMT_c[pos_lat_t]
    MTLat_B = LatMT_c[pos_lat_b]
else:
    pos_lat_b = pos_lat
    pos_lat_t = pos_lat + 1
    MTLat_T = LatMT_c[pos_lat_t]
    MTLat_B = LatMT_c[pos_lat_b]

print("The closest numbers to", lat, "are:", MTLat_B, "and", MTLat_T, "and their positions are",
      pos_lat_b, "and", pos_lat_t)

i1 = MTJan.loc[pos_lat_b, pos_lon_l]
i2 = MTJan.loc[pos_lat_t, pos_lon_l]
i3 = MTJan.loc[pos_lat_b, pos_lon_r]
i4 = MTJan.loc[pos_lat_t, pos_lon_r]

t = (lat - MTLat_B)/(MTLat_T-MTLat_B)
s = (lon - MTLon_L)/(MTLon_R - MTLon_L)

# Final value of MT
MTF = (1 - s)*(1 - t)*i1 + (1 - s)*t*i2 + s*(1 - t)*i3 + t*s*i4

print("MT = ", MTF)

print("Surrounding values:", MTJan.loc[pos_lat_t, pos_lon_l], MTJan.loc[pos_lat_t, pos_lon_r],
      MTJan.loc[pos_lat_b, pos_lon_l], MTJan.loc[pos_lat_b, pos_lon_r])
