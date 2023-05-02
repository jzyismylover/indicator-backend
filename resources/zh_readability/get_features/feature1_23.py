# -*-  coding:utf-8 -*-
from resources.zh_readability.feature_bean.chinese_word_feature import (
    ChineseWordFeature,
)
from resources.zh_readability.feature_bean.gram_word_feature import GramWordFeature
from resources.zh_readability.feature_bean.stroke_feature import StrokeFeature
from resources.zh_readability.feature_bean.word_feature import WordFeature
from resources.zh_readability.read_write_txt.acquire_stroke import acquire_stroke
from resources.zh_readability.read_write_txt.acquire_ws import acquire_cws


def feature1_23(data_set):
    v_lines = data_set.v_lines
    all_word = data_set.words
    (
        chinese,
        ch,
        one_word,
        two_word,
        three_word,
        four_word,
        more_word,
    ) = acquire_cws(data_set)

    (most, second, low, middle, high, strokes) = acquire_stroke(
        data_set.raw_text,
        data_set.strokes_method,
        data_set.strokes_list,
        chinese,
        data_set.most_com_word,
        data_set.second_com_word,
    )

    '''
    类实例化
    '''
    # 常用字/次常用字特征类实例化
    word_feature = WordFeature(most, second)
    # 笔画特征类实例化
    stroke_feature = StrokeFeature(low, middle, high)
    # 字数特征类实例化
    chinese_word_feature = ChineseWordFeature(chinese, ch)
    # X字词特征类实例化
    gram_word_feature = GramWordFeature(
        one_word, two_word, three_word, four_word, more_word
    )

    '''
    输出特征1-26
    '''
    # data_set.features_dict["1|CC-1|"] = round(
    #     word_feature.get_percentage_most_word_per_doc(chinese), 4
    # )
    # data_set.features_dict["2|CC-2|"] = round(
    #     word_feature.get_percentage_second_word_per_doc(chinese), 4
    # )
    # data_set.features_dict["3|CC-3|"] = round(
    #     word_feature.get_percentage_all_most_word_per_doc(chinese), 4
    # )
    # data_set.features_dict["4|CC-4|"] = round(
    #     stroke_feature.get_low_stroke_per_doc(chinese), 4
    # )
    # data_set.features_dict["5|CC-5|"] = round(
    #     stroke_feature.get_middle_stroke_per_doc(chinese), 4
    # )
    # data_set.features_dict["6|CC-6|"] = round(
    #     stroke_feature.get_high_stroke_per_doc(chinese), 4
    # )
    data_set.features_dict["7|CC-7|"] = round(
        stroke_feature.get_average_stroke_per_doc(strokes, chinese), 4
    )
    data_set.features_dict["8|WC-8|"] = round(
        chinese_word_feature.get_average_character_per_doc(all_word), 4
    )
    data_set.features_dict["9|WC-9|"] = round(
        chinese_word_feature.get_unique_average_character_per_doc(all_word), 4
    )
    # data_set.features_dict["10|WC-10|"] = round(
    #     gram_word_feature.get_num_of_two_word(), 4
    # )
    # data_set.features_dict["11|WC-11|"] = round(
    #     gram_word_feature.get_percentage_two_word_per_doc(all_word), 4
    # )
    # data_set.features_dict["12|WC-12|"] = round(
    #     gram_word_feature.get_num_of_three_word(), 4
    # )
    data_set.features_dict["13|WC-13|"] = round(
        gram_word_feature.get_percentage_three_word_per_doc(all_word), 4
    )
    # data_set.features_dict["14|WC-14|"] = round(
    #     gram_word_feature.get_num_of_four_word(), 4
    # )
    # data_set.features_dict["15|WC-15|"] = round(
    #     gram_word_feature.get_percentage_four_word_per_doc(all_word), 4
    # )
    # data_set.features_dict["16|WC-16|"] = round(
    #     gram_word_feature.get_num_of_more_word(), 4
    # )
    # data_set.features_dict["17|WC-17|"] = round(
    #     gram_word_feature.get_percentage_more_word_per_doc(all_word), 4
    # )

    data_set.features_dict[
        "18|SC-18|"
    ] = gram_word_feature.get_average_more_word_per_sentence(v_lines)
    data_set.features_dict[
        "19|SC-19|"
    ] = chinese_word_feature.get_average_word_per_sentence(all_word, v_lines)
    data_set.features_dict[
        "20|SC-20|"
    ] = chinese_word_feature.get_average_chinese_per_sentence(v_lines)
    # data_set.features_dict[
    #     "21|SC-21|"
    # ] = chinese_word_feature.get_average_character_per_sentence(v_lines)

    data_set.features_dict["22|D-22|"] = round(
        chinese_word_feature.get_num_of_all_chinese(), 4
    )
    data_set.features_dict["23|D-23|"] = round(
        chinese_word_feature.get_num_of_all_character(), 4
    )

    return data_set
