# -*-  coding:utf-8 -*-
from resources.zh_readability.method.tools import unique


class LexicalFeature:
    """这个类包含词法特征"""

    def __init__(self, word_list):
        self.wordList = word_list

    def get_percentage_word_per_doc(self, all_word):
        """
        函数作用：得到文章某种词在文章总词数的占比
        :param all_word: 文章的所有词的列表
        :return: 文章的所有词的列表
        """
        word_feature = round(len(self.wordList) * 1.0 / len(all_word), 4)
        return word_feature

    def get_percentage_unique_word_per_doc(self, all_word):
        """
        函数作用：得到文档的唯一某种词在去重后总词数的占比
        :param all_word: 文章的所有词的列表
        :return:
        """
        unique_word_list = unique(self.wordList)
        the_unique_all_word = unique(all_word)
        unique_feature = round(len(unique_word_list) * 1.0 / len(the_unique_all_word), 4)
        return unique_feature

    def get_num_of_unique_word(self):
        """
        函数作用：得到文档的唯一某种词的个数
        :return: 文档的唯一某种词的个数
        """
        unique_word_list = unique(self.wordList)
        return len(unique_word_list) * 1.0

    def get_average_word_per_sentence(self, num_of_line):
        """
        函数作用：得到句子平均某种词个数
        :param num_of_line: 文章的句子数
        :return: 句子平均某种词个数
        """
        average_word_feature = round(len(self.wordList) * 1.0 / num_of_line, 4)
        return average_word_feature

    def get_average_unique_word_per_sentence(self, num_of_line):
        """
        函数作用：得到句子平均唯一某种词个数
        :param num_of_line: 文章的句子数
        :return: 句子平均唯一某种词个数
        """
        average_unique_word_feature = round(len(unique(self.wordList)) * 1.0 / num_of_line, 4)
        return average_unique_word_feature
