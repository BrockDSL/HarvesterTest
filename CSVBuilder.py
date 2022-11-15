import os
import pandas as pd

folder = 'HarvestedReddits/technology'

for filename in os.listdir(folder):
    filejson = pd.read_json(filename)
    print(filejson)