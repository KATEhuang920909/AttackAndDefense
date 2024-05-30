from flask import Flask, request
import sys
import os

sys.path.append("../")
sys.path.append("../ir/hardmatch")

current_path = os.getcwd()  # 获取当前路径
parent_path = os.path.dirname(current_path)
from dfa import DFA
import json
import pandas as pd
import numpy as np

import pickle
from functools import partial

app = Flask(__name__)

# hard match model
dfa = DFA()



# ===============hard match====================
@app.route('/hard_match/filter', methods=['POST', 'GET'])
def text_filter():
    string = request.args.get('contents', '')
    response_dict = dict()
    print("string", string)
    if dfa.exists(string) is False:
        response_dict['is_illegal'] = False
        position = []
    else:
        response_dict['is_illegal'] = True
        position = dfa.filter_all(string)
    response_dict['position'] = position
    print("response_dict", response_dict)

    # response = json.dumps(response_dict)
    return response_dict


@app.route('/hard_match/add', methods=['POST', 'GET'])
def add_new_words():
    string = request.args.get('word', '')
    if string in dfa.ban_words_set:
        return '"' + string + '"已在敏感词文档中，添加失败'
    dfa.add_new_word(string)
    with open(dfa.path, 'a', encoding='utf-8-sig') as f:
        f.writelines('\n' + string)
    return '添加成功'


@app.route('/hard_match/change', methods=['POST', 'GET'])
def chang_text():
    path = request.args.get('path', '')
    try:
        dfa.change_words(path)
    except FileNotFoundError:
        return '文件"' + path + '"不存在'
    return '已将文件"' + path + '"作为敏感词库'

if __name__ == '__main__':
    port = 4567
    app.run('0.0.0.0', port)
