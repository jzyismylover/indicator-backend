# -*- coding:utf-8 -*-

def acquire_cws(sfm, words):

    ch1 = sfm.get_character(words)  # 所有的字符
    (oneWord1, twoWord1, threeWord1, fourWord1, moreWord1) = sfm.get_gram_word(words)  # 得到X字词语
    chinese1 = sfm.get_chinese(words)  # 得到所有的汉字

    return chinese1, ch1, oneWord1, twoWord1, threeWord1, fourWord1, moreWord1
