import hashlib
import os
from datetime import datetime, timedelta


def generate_file_name(params):
    params_str = "_".join(map(str, params))
    hash_object = hashlib.md5(params_str.encode())
    file_name = hash_object.hexdigest()
    return file_name


# def encode_selected(selected, mode):
#     array = options[mode]
#     size = len(array)
#     result = ''
#     i = 0
#
#     if not isinstance(selected, (list, tuple)):
#         selected = [selected]
#
#     for elem in selected:
#         while i < size and elem != array[i]:
#             result += '0'
#             i += 1
#
#         if i < size and elem == array[i]:
#             result += '1'
#             i += 1
#
#     result += '0' * (size - len(result))
#
#     return result

# def get_file_path(start_date, end_date, dist, track, params, mode='t'):
#     start_date = start_date.replace('/', '_').replace(':', '_').replace(' ', '_')
#     end_date = end_date.replace('/', '_').replace(':', '_').replace(' ', '_')
#     base_dir = "C:\\machine learning\\gb_greyhound\\grayhound\\data"
#
#     if mode == 't':
#         sub_dir = "train"
#         ending = "_train_data.csv"
#     elif mode == 'p':
#         sub_dir = "pred"
#         ending = "_predict_data.csv"
#     elif mode == 'r':
#         sub_dir = "res"
#         ending = "_results.csv"
#     elif mode == 'm':
#         sub_dir = "model"
#         ending = "_model.pkl"
#     elif mode == 'ohe':
#         sub_dir = "model"
#         ending = "_onehot.csv"
#     elif mode == "mms":
#         sub_dir = "model"
#         ending = "_mms.csv"
#     elif mode == "iso":
#         sub_dir = "model"
#         ending = "_iso.csv"
#     else:
#         raise ValueError(f"Unknown mode: {mode}")
#
#     encoded_dist = encode_selected(dist, 'dist')
#     encoded_track = encode_selected(track, 'track')
#
#     params_list = [start_date, end_date, encoded_dist, encoded_track]
#
#     encoded_params = encode_selected(params, 'params')
#     params_list.append(encoded_params)
#
#     file_name = generate_file_name(params_list) + ending
#     file_path = os.path.join(base_dir, sub_dir, file_name)
#
#
#     directory = os.path.dirname(file_path)
#     if not os.path.exists(directory):
#         os.makedirs(directory)
#
#     return file_path

import pandas as pd

def is_csv_file_empty(file_path: str) -> bool:
    return os.path.getsize(file_path) == 0



def get_pred_file() -> str:
    dir_path = os.path.join(os.getcwd(), "..", "..", "data", "to_pred")
    date = datetime.today()
    date = date.strftime('%Y-%m-%d')
    file_path = os.path.join(dir_path, f'to_pred_{date}.csv')
    print(file_path)
    return file_path



def load_dataset(filename: str) -> pd.DataFrame:
    return pd.read_csv(filename)



def save_final_file(df: pd.DataFrame) -> None:
    df.to_csv(os.path.join(os.getcwd(), "..", "..", "data", "temp.csv"))



def get_final_file() -> str:
    return os.path.join(os.getcwd(), "..", "..", "data", "temp.csv")