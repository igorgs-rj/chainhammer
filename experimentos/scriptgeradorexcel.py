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

for x in files:
    if x.endswith(".json"):
        with open(x, "r") as f:
            data = json.load(f)
        vBlock = sorted(data["blocks_txs"].items(), key = lambda x: int(x[0]))
        formatedDataTxsBlocks[x] = {}
        formatedDataTxsBlocks[x]["txs_per_block"] =  []
        for k,v in vBlock:
            formatedDataTxsBlocks[x]["txs_per_block"].append(len(v))

        vLat = sorted(data["lat"].items(), key = lambda x: int(x[0]))
        formatedDataLat[x] = {}
        formatedDataLat[x]["lat"] =  []
        for k,v in vLat:
            formatedDataLat[x]["lat"].append(int(v))

        vSize = sorted(data["blocks_size"].items(), key = lambda x: int(x[0]))
        formatedDataBlocksSizes[x] = {}
        formatedDataBlocksSizes[x]["size"] =  []
        for k,v in vSize:
            formatedDataBlocksSizes[x]["size"].append(v)

        formatedDataAvgCpu[x] = {}
        formatedDataAvgCpu[x]["avg_cpu_usage"] = data["cpu_usage"]
        formatedDataPeakTps[x] = {}
        formatedDataPeakTps[x]["peak_Tps"] = data["tps"]["peakTpsAv"]
        

        

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
