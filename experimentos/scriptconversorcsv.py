import csv
import json
import operator
import datetime
import numpy
import copy
import pandas as pd
import os
import array
from collections import OrderedDict as od

df = pd.read_json(r'.\resultados\avgcpu.json')
df.to_csv(r'.\resultados\avgcpu.csv', index = None, na_rep ='NaN')

with open('./resultados/lat.json', "r") as f:
    data = json.load(f)

columns = []
fulllist = []
for attr, value in data.items():
    columns.append(attr)
    fulllist.append(value['lat'])

df_concat = pd.DataFrame()
for i in range(len(fulllist)):
    df = pd.DataFrame(data=fulllist[i], columns=[columns[i]])
    df_concat = pd.concat([df, df_concat], axis=1)

df_concat.to_csv(r'.\resultados\lat.csv', index = None, na_rep ='NaN')

df = pd.read_json(r'.\resultados\peaktps.json')
df.to_csv(r'.\resultados\peaktps.csv', index = None, na_rep ='NaN')

with open('./resultados/sizesblocks.json', "r") as f:
    data = json.load(f)

columns = []
fulllist = []
for attr, value in data.items():
    columns.append(attr)
    fulllist.append(value['size'])

df_concat = pd.DataFrame()
for i in range(len(fulllist)):
    df = pd.DataFrame(data=fulllist[i], columns=[columns[i]])
    df_concat = pd.concat([df, df_concat], axis=1)

df_concat.to_csv(r'.\resultados\sizesblocks.csv', index = None, na_rep ='NaN')

with open('./resultados/tps.json', "r") as f:
    data = json.load(f)

columns = []
fulllist = []
for attr, value in data.items():
    columns.append(attr)
    fulllist.append(value['alltps'])

df_concat = pd.DataFrame()
for i in range(len(fulllist)):
    df = pd.DataFrame(data=fulllist[i], columns=[columns[i]])
    df_concat = pd.concat([df, df_concat], axis=1)

df_concat.to_csv(r'.\resultados\tps.csv', index = None, na_rep ='NaN')

with open('./resultados/txsblocks.json', "r") as f:
    data = json.load(f)

columns = []
fulllist = []
for attr, value in data.items():
    columns.append(attr)
    fulllist.append(value['txs_per_block'])

df_concat = pd.DataFrame()
for i in range(len(fulllist)):
    df = pd.DataFrame(data=fulllist[i], columns=[columns[i]])
    df_concat = pd.concat([df, df_concat], axis=1)

df_concat.to_csv(r'.\resultados\txsblocks.csv', index = None, na_rep ='NaN')