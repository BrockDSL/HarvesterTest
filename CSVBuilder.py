import os
import pandas as pd

folder = 'HarvestedReddits/technology'

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    filejson = pd.read_json(filepath)
    newname = filename[0:-4:1]+"csv"
    filepath = os.path.join(folder, newname)
    filejson.to_csv(filepath, index=False)
    print(filepath)
    print(pd.read_csv(filepath))