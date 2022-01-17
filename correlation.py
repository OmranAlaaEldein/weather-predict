

#
# print("initializing start .... ")
# df = pd.read_csv("C:/Users/Toshiba-pc/Desktop/graduation/dataset/historical_filtered_kpis.csv")
#
#
# targets = [
#     "tch_traffic", "tch_blocking", "tch_fr_slots", "tch_hr_slots",
#     "sdcch_traffic", "sdcch_blocking", "sdcch_time_slots",
#     "pdtch_traffic", "pdtch_blocking", "pdtch_time_slots", "trx"
# ]
#
# df = df[ targets ]
#
# tch_1   = df[ ["trx" , "sdcch_blocking" ,"tch_traffic" ] ]
#
# tch_1_1 = df[["trx","tch_fr_slots" , "tch_hr_slots"]]
#
# tch_2   = df[ ["trx","pdtch_blocking" ,"sdcch_traffic" ] ]
#
# tch_3   = df[ ["trx" ,"pdtch_traffic", "sdcch_time_slots"] ]
#
# tch_4   = df[ ["trx" , "pdtch_time_slots" , "tch_blocking"] ]
#
# # for tch correlation ...
#
# print()
# order = []
# targ = ["trx" , "sdcch_blocking" , "tch_traffic" ]
# index = 0
# temp = tch_1.corr().values[0:1,0:][0].tolist()
# for item in temp :
#     if( item != 1.0 ):
#         order.append( ( item , targ[index] ) )
#     index += 1
#
#
# targ = ["trx"  ,"pdtch_blocking" ,"sdcch_traffic" ]
# index = 0
# temp = tch_2.corr().values[0:1,0:][0].tolist()
# for item in temp :
#     if (item != 1.0):
#         order.append((item, targ[index]))
#     index += 1
#
#
# targ =  ["trx" ,"pdtch_traffic", "sdcch_time_slots"]
# index = 0
# temp = tch_3.corr().values[0:1,0:][0].tolist()
# for item in temp :
#     if (item != 1.0):
#         order.append((item, targ[index]))
#     index += 1
#
#
# targ = ["trx" , "pdtch_time_slots" , "tch_blocking"]
# index = 0
# temp = tch_4.corr().values[0:1,0:][0].tolist()
# for item in temp :
#     if (item != 1.0):
#         order.append((item, targ[index]))
#     index += 1
#
#
#
#
# targ = ["trx","tch_fr_slots" , "tch_hr_slots"]
# index = 0
# temp = tch_1_1.corr().values[0:1,0:][0].tolist()
# for item in temp :
#     if (item != 1.0):
#         order.append((item, targ[index]))
#     index += 1
#
#
#
#
# order.sort(reverse=True)
# print(order)
#
#
# print()
# print(tch_1.corr())
# print()
# print(tch_1_1.corr())
# print()
# print(tch_2.corr())
# print()
# print(tch_3.corr())
# print()
# print(tch_4.corr())
# print()
#

# plt.matshow(df.corr())
# plt.xticks(range(len(df.columns)), df.columns)
#plt.yticks(range(len(df.columns)), df.columns)
#plt.colorbar()
#plt.show()



import pandas as pd
#import plotly as plt


print("initializing start .... ")
df = pd.read_csv("C:/Users/Asus/Desktop/last data/test.csv")
targets = ["Date", "weather.Max tempature", "weather.Min Tempature", "Humidity",
     "wind", "Name", "NE Type","pressure"]
df = df[ targets ]
print(df.corr())
print(len(df.columns))

plt.matshow(df.corr())
plt.xticks(range(len(df.columns)), df.columns)
plt.yticks(range(len(df.columns)), df.columns)
plt.colorbar()
plt.show()
