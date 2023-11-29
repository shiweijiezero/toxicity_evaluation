import json

import pandas as pd
import requests
from tqdm import tqdm

data_lst = [
    "eval_Reddit-HK_58.json",
    "eval_Google-HK_100.json",
]
name = "raw_baichuan"

for file in data_lst:
    print(file)
    lst = []
    df = pd.read_json(file)
    for idx,item in tqdm(df.iterrows(),total=df.shape[0]):
        instruct = item["instruction"]
        inp = item["input"]
        out = item["output"]
        in_str = instruct+inp
        data_dic = {"prompt": in_str}
        response = requests.post(url="http://localhost:8410", json=data_dic)
        response = json.loads(response.text)
        lst.append((in_str,response,out))
    print("save")
    new_df = pd.DataFrame(lst)
    new_df.to_json(f"{name}_response_{file}")

