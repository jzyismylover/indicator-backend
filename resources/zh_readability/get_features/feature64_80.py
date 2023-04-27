# -*-  coding:utf-8 -*-
from read_write_txt.acquire_cp import acquire_cp


def feature64_80(data_set):
    # 获得短语标注结果
    (data_set.np_result, data_set.vp_result, data_set.pp_result, data_set.ip_sentence, data_set.ip) = \
        acquire_cp(data_set.syfm, data_set.base_cp_dir, data_set.file)
    tree_result = data_set.syfm.count_high_of_tree(data_set.base_cp_dir + data_set.file)

    punctuation_num, mean_word_in_punctuation = data_set.syfm.count_punctuation(data_set.base_ws_dir + data_set.file)
    sum_dep, avg_dep = data_set.syfm.count_dependent_distance(data_set.base_dp_dir + data_set.file)

    # 短语
    data_set.features_dict["64|P-64|"] = data_set.sf.get_num_of_word_phrase_per_sentence(data_set.np_result, data_set.v_lines)
    data_set.features_dict["65|P-65|"] = data_set.sf.get_num_of_word_phrase_per_sentence(data_set.vp_result, data_set.v_lines)
    data_set.features_dict["66|P-66|"] = round(data_set.sf.get_num_of_word_phrase_per_doc(data_set.np_result), 4)
    data_set.features_dict["67|P-67|"] = round(data_set.sf.get_num_of_word_phrase_per_doc(data_set.vp_result), 4)
    data_set.features_dict["68|P-68|"] = round(data_set.sf.get_num_of_word_phrase_per_doc(data_set.pp_result), 4)
    data_set.features_dict["69|P-69|"] = round(data_set.sf.get_average_length_word_phrase(data_set.np_result), 4)
    data_set.features_dict["70|P-70|"] = round(data_set.sf.get_average_length_word_phrase(data_set.vp_result), 4)
    data_set.features_dict["71|P-71|"] = round(data_set.sf.get_average_length_word_phrase(data_set.pp_result), 4)

    num_sentence_with_ip = len(data_set.ip_sentence)
    data_set.features_dict["72|CL-72|"] = round(num_sentence_with_ip, 4)
    data_set.features_dict["73|CL-73|"] = round((data_set.v_lines - num_sentence_with_ip) / data_set.v_lines, 4)
    data_set.features_dict["74|CL-74|"] = round(data_set.sf.get_average_length_word_phrase(data_set.ip) / data_set.v_lines, 4)
    data_set.features_dict["75|CL-75|"] = round(punctuation_num, 4)
    data_set.features_dict["76|CL-76|"] = round(mean_word_in_punctuation, 4)

    data_set.features_dict["77|S-77|"] = round(len(tree_result), 4)  # 文章句子数
    data_set.features_dict["78|S-78|"] = round(sum(tree_result) / len(tree_result), 4)  # 文章平均句法树高度

    data_set.features_dict["79|CL-79|"] = round(sum_dep, 4)
    data_set.features_dict["80|CL-80|"] = round(avg_dep, 4)

    return data_set
