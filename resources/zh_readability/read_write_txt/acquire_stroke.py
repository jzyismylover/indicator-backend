# -*- coding:utf-8 -*-


def acquire_stroke(raw_text, stroke_method, stroke_list, chinese1, most_com_word, second_com_word):

    most1 = []  # 最常用字
    second1 = []  # 次常用字
    for i in chinese1:  # 遍历所有字
        if i in most_com_word:
            most1.append(i)
        elif i in second_com_word:
            second1.append(i)

    low1 = []  # 低笔画汉字（不去重)
    middle1 = []  # 中笔画汉字(不去重）
    high1 = []  # 高笔画汉字(不去重)
    strokes1 = 0
    line1 = raw_text.replace('\r\n', '').replace('\n', '')
    for uchar in line1:
        if stroke_method.is_chinese(uchar):
            stroke = stroke_method.count_word_num(uchar, stroke_list)
            strokes1 = strokes1 + stroke
            if stroke <= 10:
                low1.append(uchar)
            elif 11 <= stroke <= 15:
                middle1.append(uchar)
            else:
                high1.append(uchar)

    return most1, second1, low1, middle1, high1, strokes1
