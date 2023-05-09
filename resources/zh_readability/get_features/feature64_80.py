# -*-  coding:utf-8 -*-
from resources.zh_readability.read_write_txt.acquire_cp import acquire_cp

def feature64_80(data_set):
    # 获得短语标注结果
    (data_set.np_result, data_set.vp_result, data_set.pp_result, data_set.ip_sentence, data_set.ip, trees) = \
        acquire_cp(data_set)
    tree_result = data_set.syfm.count_high_of_tree(trees) # 得到整篇文章句法树集合

    print('ppresult')
    print(data_set.pp_result)

    # 短语
    data_set.features_dict["71|P-71|"] = round(data_set.sf.get_average_length_word_phrase(data_set.pp_result), 4)

    # 从句
    num_sentence_with_ip = len(data_set.ip_sentence)
    # data_set.features_dict["72|CL-72|"] = round(num_sentence_with_ip, 4)
    data_set.features_dict["73|CL-73|"] = round((data_set.v_lines - num_sentence_with_ip) / data_set.v_lines, 4)
    data_set.features_dict["74|CL-74|"] = round(data_set.sf.get_average_length_word_phrase(data_set.ip) / data_set.v_lines, 4)
    
    # 句法
    data_set.features_dict["78|S-78|"] = round(sum(tree_result) / len(tree_result), 4)  # 文章平均句法树高度

    return data_set
