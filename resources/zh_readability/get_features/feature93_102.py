# -*-  coding:utf-8 -*-
from resources.zh_readability.method.word_feature_method import word_feature


def feature93_102(data_set):
    # 连词
    word_list = data_set.c
    (feature_1, feature_2, feature_3,
     feature_4, feature_5) = word_feature(word_list, data_set.words, data_set.v_lines)
    # data_set.features_dict["93|CO-93|"] = feature_1
    data_set.features_dict["94|CO-94|"] = feature_2
    data_set.features_dict["95|CO-95|"] = feature_3
    data_set.features_dict["96|CO-96|"] = feature_4
    # data_set.features_dict["97|CO-97|"] = feature_5
    # 代词
    # word_list = data_set.r
    # (feature_1, feature_2, feature_3,
    #  feature_4, feature_5) = word_feature(word_list, data_set.words, data_set.v_lines)
    # data_set.features_dict["98|CO-98|"] = feature_1
    # data_set.features_dict["99|CO-99|"] = feature_2
    # data_set.features_dict["100|CO-100|"] = feature_3
    # data_set.features_dict["101|CO-101|"] = feature_4
    # data_set.features_dict["102|CO-102|"] = feature_5
    
    return data_set
