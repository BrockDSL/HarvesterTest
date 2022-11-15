import os
import pandas as pd

folder = 'HarvestedReddits/technology'

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    filejson = pd.read_json(filepath)
    filejson.to_csv("newfile.csv", index=False)
    print(pd.read_csv("newfile.csv"))