import pandas as pd
from tqdm import tqdm
import evaluate

data_lst = [
    "eval_Reddit-HK_58.json",
    "eval_Google-HK_100.json",
]
name = "sft_baichuan"

print("loading")
toxicity = evaluate.load(
    "toxicity",
    # "./model/models--facebook--roberta-hate-speech-dynabench-r4-target",
    # 'DaNLP/da-electra-hatespeech-detection',
    cache_dir="./model",
    module_type="measurement", )

for file in data_lst:
    target_file = f"{name}_response_{file}"
    df = pd.read_json(target_file)
    response_lst = df[1].to_list()
    response_lst = [item['response'] for item in response_lst]
    raw_answer_lst = df[2].to_list()

    print('start to compute 1')
    response_res = toxicity.compute(predictions=response_lst)["toxicity"]
    print(response_res)
    print('start to compute 2')
    raw_answer_res = toxicity.compute(predictions=raw_answer_lst)["toxicity"]
    print(raw_answer_res)
    print(f"{target_file}")
    print(f"response_res:{sum(response_res) / len(response_res)}")
    print(f"raw_answer_res:{sum(raw_answer_res) / len(raw_answer_res)}")
    print("-" * 20)
