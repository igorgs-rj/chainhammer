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

diretorios = [name for name in os.listdir(".") if os.path.isdir(name)]

files = os.listdir(".")

formatedDataTxsBlocks = {}
formatedDataBlocksSizes = {}
formatedDataAvgCpu = {}
formatedDataPeakTps = {}
formatedDataLat = {}
formatedDataAllTps = {}

for x in files:
    if x.endswith(".json"):
        with open(x, "r") as f:
            data = json.load(f)
        vTpsBlock = sorted(data["alltps"].items(), key = lambda x: int(x[0]))
        formatedDataAllTps[x.split('.')[0]] = {}
        formatedDataAllTps[x.split('.')[0]]["alltps"] =  []
        for k,v in vTpsBlock:
            formatedDataAllTps[x.split('.')[0]]["alltps"].append(v)

        vBlock = sorted(data["blocks_txs"].items(), key = lambda x: int(x[0]))
        formatedDataTxsBlocks[x.split('.')[0]] = {}
        formatedDataTxsBlocks[x.split('.')[0]]["txs_per_block"] =  []
        for k,v in vBlock:
            formatedDataTxsBlocks[x.split('.')[0]]["txs_per_block"].append(len(v))

        vLat = sorted(data["lat"].items(), key = lambda x: int(x[0]))
        formatedDataLat[x.split('.')[0]] = {}
        formatedDataLat[x.split('.')[0]]["lat"] =  []
        for k,v in vLat:
            formatedDataLat[x.split('.')[0]]["lat"].append(int(v))

        vSize = sorted(data["blocks_size"].items(), key = lambda x: int(x[0]))
        formatedDataBlocksSizes[x.split('.')[0]] = {}
        formatedDataBlocksSizes[x.split('.')[0]]["size"] =  []
        for k,v in vSize:
            formatedDataBlocksSizes[x.split('.')[0]]["size"].append(v)

        formatedDataAvgCpu[x.split('.')[0]] = {}
        formatedDataAvgCpu[x.split('.')[0]]["avg_cpu_usage"] = data["cpu_usage"]
        formatedDataPeakTps[x.split('.')[0]] = {}
        formatedDataPeakTps[x.split('.')[0]]["peak_Tps"] = data["tps"]["peakTpsAv"]
        

        

with open("resultados/txsblocks.json", "w") as f:
    json.dump(formatedDataTxsBlocks, f)

with open("resultados/sizesblocks.json", "w") as f:
    json.dump(formatedDataBlocksSizes, f)

with open("resultados/avgcpu.json", "w") as f:
    json.dump(formatedDataAvgCpu, f)

with open("resultados/peaktps.json", "w") as f:
    json.dump(formatedDataPeakTps, f)

with open("resultados/lat.json", "w") as f:
    json.dump(formatedDataLat, f)

with open("resultados/tps.json", "w") as f:
    json.dump(formatedDataAllTps, f)
