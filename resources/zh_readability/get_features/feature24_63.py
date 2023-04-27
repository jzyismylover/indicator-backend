# -*-  coding:utf-8 -*-
from resources.zh_readability.method.word_feature_method import word_feature


def feature24_63(data_set):
    # 形容词
    word_list = data_set.a
    (feature_1, feature_2, feature_3, feature_4, feature_5) = word_feature(
        word_list, data_set.words, data_set.v_lines
    )
    data_set.features_dict["24|A-24|"] = feature_1
    data_set.features_dict["25|A-25|"] = feature_2
    data_set.features_dict["26|A-26|"] = feature_3
    data_set.features_dict["27|A-27|"] = feature_4
    data_set.features_dict["28|A-28|"] = feature_5
    # 功能词
    word_list = data_set.function_word
    (feature_1, feature_2, feature_3, feature_4, feature_5) = word_feature(
        word_list, data_set.words, data_set.v_lines
    )
    data_set.features_dict["29|F-29|"] = feature_1
    data_set.features_dict["30|F-30|"] = feature_2
    data_set.features_dict["31|F-31|"] = feature_3
    data_set.features_dict["32|F-32|"] = feature_4
    data_set.features_dict["33|F-33|"] = feature_5
    # 动词
    word_list = data_set.v
    (feature_1, feature_2, feature_3, feature_4, feature_5) = word_feature(
        word_list, data_set.words, data_set.v_lines
    )
    data_set.features_dict["34|V-34|"] = feature_1
    data_set.features_dict["35|V-35|"] = feature_2
    data_set.features_dict["36|V-36|"] = feature_3
    data_set.features_dict["37|V-37|"] = feature_4
    data_set.features_dict["38|V-38|"] = feature_5
    # 普通名词
    word_list = data_set.n
    (feature_1, feature_2, feature_3, feature_4, feature_5) = word_feature(
        word_list, data_set.words, data_set.v_lines
    )
    data_set.features_dict["39|N-39|"] = feature_1
    data_set.features_dict["40|N-40|"] = feature_2
    data_set.features_dict["41|N-41|"] = feature_3
    data_set.features_dict["42|N-42|"] = feature_4
    data_set.features_dict["43|N-43|"] = feature_5
    # 所有名词
    word_list = data_set.all_noun
    (feature_1, feature_2, feature_3, feature_4, feature_5) = word_feature(
        word_list, data_set.words, data_set.v_lines
    )
    data_set.features_dict["44|N-44|"] = feature_1
    data_set.features_dict["45|N-45|"] = feature_2
    data_set.features_dict["46|N-46|"] = feature_3
    data_set.features_dict["47|N-47|"] = feature_4
    data_set.features_dict["48|N-48|"] = feature_5
    # 实词
    word_list = data_set.content_word
    (feature_1, feature_2, feature_3, feature_4, feature_5) = word_feature(
        word_list, data_set.words, data_set.v_lines
    )
    data_set.features_dict["49|C-49|"] = feature_1
    data_set.features_dict["50|C-50|"] = feature_2
    data_set.features_dict["51|C-51|"] = feature_3
    data_set.features_dict["52|C-52|"] = feature_4
    data_set.features_dict["53|C-53|"] = feature_5
    # 习语
    word_list = data_set.i
    (feature_1, feature_2, feature_3, feature_4, feature_5) = word_feature(
        word_list, data_set.words, data_set.v_lines
    )
    data_set.features_dict["54|I-54|"] = feature_1
    data_set.features_dict["55|I-55|"] = feature_2
    data_set.features_dict["56|I-56|"] = feature_3
    data_set.features_dict["57|I-57|"] = feature_4
    data_set.features_dict["58|I-58|"] = feature_5
    # 副词
    word_list = data_set.d
    (feature_1, feature_2, feature_3, feature_4, feature_5) = word_feature(
        word_list, data_set.words, data_set.v_lines
    )
    data_set.features_dict["59|AD-59|"] = feature_1
    data_set.features_dict["60|AD-60|"] = feature_2
    data_set.features_dict["61|AD-61|"] = feature_3
    data_set.features_dict["62|AD-62|"] = feature_4
    data_set.features_dict["63|AD-63|"] = feature_5

    return data_set
