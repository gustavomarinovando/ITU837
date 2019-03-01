import pandas as pd

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

LonT_T = LonT.transpose()

LatT_c = LatT[0].tolist()
LonT_c = LonT_T[0].tolist()

print("Enter your desired latitude and longitude")

lat = 22.9
lon = -43.23

# lat = float(input())
# lon = float(input())

print("Your longitude is :", lon)
print("Your latitude is:", lat)

# Longitude MT
LonMT_CV = min(LonT_c, key=lambda x: abs(x-lon))
pos_lon = LonT_c.index(LonMT_CV)

aux = LonMT_CV - lon

if aux > 0:
    pos_lon_r = pos_lon
    pos_lon_l = pos_lon - 1
    TLon_R = LonT_c[pos_lon_r]
    TLon_L = LonT_c[pos_lon_l]
else:
    pos_lon_l = pos_lon
    pos_lon_r = pos_lon + 1
    TLon_R = LonT_c[pos_lon_r]
    TLon_L = LonT_c[pos_lon_l]

print("The closest numbers to", lon, "are:", TLon_L, "and", TLon_R, "and their positions are",
      pos_lon_l, "and", pos_lon_r)

# Latitude MT
LatMT_CV = min(LonT_c, key=lambda x: abs(x-lat))
pos_lat = LatT_c.index(LatMT_CV)

aux1 = LatMT_CV - lat

if aux1 > 0:
    pos_lat_t = pos_lat
    pos_lat_b = pos_lat - 1
    TLat_T = LatT_c[pos_lat_t]
    TLat_B = LatT_c[pos_lat_b]
else:
    pos_lat_b = pos_lat
    pos_lat_t = pos_lat + 1
    TLat_T = LatT_c[pos_lat_t]
    TLat_B = LatT_c[pos_lat_b]

print("The closest numbers to", lat, "are:", TLat_B, "and", TLat_T, "and their positions are",
      pos_lat_b, "and", pos_lat_t)

i1 = TJan.loc[pos_lat_b, pos_lon_l]
i2 = TJan.loc[pos_lat_t, pos_lon_l]
i3 = TJan.loc[pos_lat_b, pos_lon_r]
i4 = TJan.loc[pos_lat_t, pos_lon_r]

t = (lat - TLat_B)/(TLat_T-TLat_B)
s = (lon - TLon_L)/(TLon_R - TLon_L)

# Final value of MT
TF = (1 - s)*(1 - t)*i1 + (1 - s)*t*i2 + s*(1 - t)*i3 + t*s*i4 - 273.15

print("T = ", TF)

print("Surrounding values:", TJan.loc[pos_lat_t, pos_lon_l], TJan.loc[pos_lat_t, pos_lon_r],
      TJan.loc[pos_lat_b, pos_lon_l], TJan.loc[pos_lat_b, pos_lon_r])
