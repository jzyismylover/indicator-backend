# -*-  coding:utf-8 -*-
from resources.zh_readability.method.tools import unique


class ChineseWordFeature:
    """这个类包含字数相关的特征"""

    def __init__(self, chinese_word, all_character):
        """
        把所有的字的列表和所有的字符当参数初始化该类
        :param chinese_word:
        :param all_character:
        """
        self.chinese_word = chinese_word
        self.all_character = all_character

    def get_num_of_all_chinese(self):
        """
        :return: 文档的总字数
        """
        return len(self.chinese_word) * 1.0

    def get_num_of_all_character(self):
        """
        :return: 文档的总字符数
        """
        return len(self.all_character) * 1.0

    def get_average_chinese_per_sentence(self, num_of_line):
        """
        :param: 文档的句子数
        :return: 句子的平均字数
        """
        return round(len(self.chinese_word) * 1.0 / num_of_line, 4)

    def get_average_character_per_sentence(self, num_of_line):
        """
        :param: 文档的句子数
        :return: 句子的平均字符数
        """
        return round(len(self.all_character) * 1.0 / num_of_line, 4)

    def get_average_character_per_doc(self, all_word):
        """
        函数作用: 得到文档的词汇平均字数（不去重）
        :param : 文档的所有词列表
        :return:文档的词汇平均字数（不去重）
        """
        average_character = round(len(self.chinese_word) * 1.0 / len(all_word), 4)
        return average_character

    def get_unique_average_character_per_doc(self, all_word):
        """
        函数作用: 得到文档的词汇平均字数（去重）
        :param : 文档的所有词列表
        :return:文档的词汇平均字数（去重）
        """
        unique_character = unique(self.chinese_word)
        unique_all_word = unique(all_word)
        average_unique_character = round(len(unique_character) * 1.0 / len(unique_all_word), 4)
        return average_unique_character

    @staticmethod
    def get_average_word_per_sentence(all_word, num_of_line):
        """
        :param: 文档的词语列表
        :param: 句子数
        :return: 句子的平均词数
        """
        return round(len(all_word) * 1.0 / num_of_line, 4)
