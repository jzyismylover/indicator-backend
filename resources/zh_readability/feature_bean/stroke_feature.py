# -*-  coding:utf-8 -*-
class StrokeFeature:
    """这个类包含笔画特征"""

    def __init__(self, low_stroke, middle_stroke, high_stroke):
        self.lowStroke = low_stroke
        self.middleStroke = middle_stroke
        self.highStroke = high_stroke

    def get_low_stroke_per_doc(self, all_chinese):
        """
        函数作用：获得文档的低笔画占比
        :param 低笔画的字
        :return: 文档的低笔画占比
        """
        low_pre = round(len(self.lowStroke) * 1.0 / len(all_chinese), 4)
        return low_pre

    def get_middle_stroke_per_doc(self, all_chinese):
        """
        函数作用：获得文档的中笔画占比
        :param 中笔画的字
        :return: 文档的中笔画占比
        """
        middle_pre = round(len(self.middleStroke) * 1.0 / len(all_chinese), 4)
        return middle_pre

    def get_high_stroke_per_doc(self, all_chinese):
        """
        函数作用：获得文档的高笔画占比
        :param 高笔画的字
        :return: 文档的高笔画占比
        """
        high_pre = round(len(self.highStroke) * 1.0 / len(all_chinese), 4)
        return high_pre

    @staticmethod
    def get_average_stroke_per_doc(stroke, all_chinese):
        """
        函数作用：获得文档的平均笔画数
        :param stroke:笔画数
        :param all_chinese:
        :return:文档的平均笔画数
        """
        average_stroke = round(stroke * 1.0 / len(all_chinese), 4)
        return average_stroke
