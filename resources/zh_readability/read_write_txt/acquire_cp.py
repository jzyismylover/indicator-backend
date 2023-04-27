# -*- coding:utf-8 -*-


def acquire_cp(syfm, base_cp_dir, file):

    v1_cp_file = open(base_cp_dir + file, "r", encoding="utf-8")
    cp_content1 = v1_cp_file.readlines()
    np_result1 = syfm.find_all_terms_by_feature(cp_content1, "NP")
    pp_result1 = syfm.find_all_terms_by_feature(cp_content1, "PP")
    vp_result1 = syfm.find_all_terms_by_feature(cp_content1, "VP")
    ip_sentence, ip = syfm.get_ic_sentence(''.join(cp_content1))
    v1_cp_file.close()

    return np_result1, vp_result1, pp_result1, ip_sentence, ip
