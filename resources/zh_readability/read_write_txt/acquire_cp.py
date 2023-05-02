# -*- coding:utf-8 -*-
import jieba
from utils.hanlp import CON_PARSER

def acquire_cp(data_set):
    # 获取成分句法树
    syfm = data_set.syfm
    sentences = data_set.sentences
    trees = []
    for sentence in sentences:
        words = jieba.cut(sentence)
        tree = CON_PARSER(words)
        trees.append(tree)
    np_result1 = syfm.find_all_terms_by_feature(trees, "NP")
    pp_result1 = syfm.find_all_terms_by_feature(trees, "PP")
    vp_result1 = syfm.find_all_terms_by_feature(trees, "VP")
    ip_sentence, ip = syfm.get_ic_sentence(''.join(trees)) # 获取子从句相关信息

    return np_result1, vp_result1, pp_result1, ip_sentence, ip, trees
