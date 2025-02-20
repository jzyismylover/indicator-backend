# -*- coding:utf-8 -*-
import jieba
import hanlp

def acquire_cp(data_set):
    # 沿用 hanlp 中文成分句法分析模型
    CON_PARSER = hanlp.load('CTB9_CON_FULL_TAG_ELECTRA_SMALL')
    # 获取成分句法树
    syfm = data_set.syfm
    sentences = data_set.sentences
    np_result1 = []
    pp_result1 = []
    vp_result1 = []
    trees = []
    for sentence in sentences:
        words = jieba.cut(sentence)
        tree = CON_PARSER(list(words))
        trees.append(tree)
        tree = str(tree)
        np_result1.extend(syfm.find_all_terms_by_feature([tree], "NP"))
        pp_result1.extend(syfm.find_all_terms_by_feature([tree], "PP"))
        vp_result1.extend(syfm.find_all_terms_by_feature([tree], "VP"))
        
    ip_sentence, ip = syfm.get_ic_sentence(''.join([str(tree) for tree in trees])) # 获取子从句相关信息

    return np_result1, vp_result1, pp_result1, ip_sentence, ip, trees
