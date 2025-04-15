import pandas as pd
import pickle
import time
from tqdm import tqdm

dtypes = {'age':'int','workclass':'category','education':'category','marital_status':'category','occupation':'category','relationship':'category','race':'category',
          'gender':'category','capital_gain':'int','capital_loss':'int','hours_per_week':'int','native_country':'category','income':'category'}
columns = list(dtypes.keys())
data = pd.read_csv('adultSalary.csv', names=columns).astype(dtypes)

# n = 20000
# n = len(data)
# data = data[:n]

synth_path = "df_synthpop.pickle"
with open(synth_path,"rb") as fr1:
    synth_data = pickle.load(fr1)

# synth_data = synth_data[:n-int(n*0.1)]
# synth_data = pd.concat([data[:int(n*0.1)], synth_data])

stime = time.time()
data_list = []
synth_data_list = []
for i in range(len(synth_data)):
    data_list.append(data.iloc[i, :].values.flatten().tolist())
    synth_data_list.append(synth_data.iloc[i, :].values.flatten().tolist())

cnt = 0
for row1 in tqdm(synth_data_list):
    for row2 in data_list:
        if row1 == row2:
            cnt += 1
            break
print(time.time()-stime)
print(cnt / len(synth_data))

