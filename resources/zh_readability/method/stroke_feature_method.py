# -*-  coding:utf-8 -*-
import os

class StrokeFeatureMethod:
    """这个类包含笔画特征用到的方法"""

    @staticmethod
    def get_model():
        """
        函数作用：把汉字笔画大全写进列表里面
        para:
        return：存储汉字笔画大全的列表
        """
        h = open(os.path.join('static', 'strokes_file', '汉字笔画大全.txt'), 'r', encoding="utf-8")
        lines = h.readlines()
        h.close()
        return lines

    @staticmethod
    def is_chinese(uchar):
        """
        函数作用：判断字符是否为汉字
        para:单个字符
        return：是汉字或者不是汉字
        """
        if u'\u4e00' <= uchar <= u'\u9fa5':
            return True
        else:
            return False

    @staticmethod
    def count_word_num(uchar, model):
        """
        函数作用：统计每个汉字的笔画数
        para:单个汉字
        return：当前汉字的笔画数
        """
        for i in range(len(model)):
            if uchar in model[i]:
                return i + 1
