# -*- coding:utf-8 -*-

def acquire_cws(data_set):
    sfm = data_set.sfm
    words = data_set.words
    raw_text = data_set.raw_text
    ch1 = sfm.get_character(raw_text)  # 所有的字符
    (oneWord1, twoWord1, threeWord1, fourWord1, moreWord1) = sfm.get_gram_word(words)  # 得到X字词语
    chinese1 = sfm.get_chinese(raw_text)  # 得到所有的汉字

    return chinese1, ch1, oneWord1, twoWord1, threeWord1, fourWord1, moreWord1
