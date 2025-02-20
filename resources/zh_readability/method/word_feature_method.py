# -*-  coding:utf-8 -*-
from resources.zh_readability.feature_bean.lexical_feature import LexicalFeature


def word_feature(word_list, all_word_pos, v_lines):
    """
    特征27-66，特征92-101
    :param word_list: word_list分别是三个版本的某个词性
    :param all_word_pos:
    :param v3_lines: v3句子数
    :return:
    """

    lexical_feature_a = LexicalFeature(word_list)


    # 得到文章某种词在文章总词数的占比
    feature_1 = round(lexical_feature_a.get_percentage_word_per_doc(all_word_pos), 4)
    # 得到文档的唯一某种词的个数 v1 v2
    feature_2 = round(lexical_feature_a.get_num_of_unique_word(), 4)
    # 得到文档的唯一某种词在去重后总词数的占比 v1 v2
    feature_3 = round(lexical_feature_a.get_percentage_unique_word_per_doc(all_word_pos), 4)
    # 得到句子平均某种词个数 v3
    feature_4 = lexical_feature_a.get_average_word_per_sentence(v_lines)
    # 得到句子平均唯一某种词个数 v3
    feature_5 = lexical_feature_a.get_average_unique_word_per_sentence(v_lines)

    return (feature_1, feature_2,
            feature_3, feature_4, feature_5)
