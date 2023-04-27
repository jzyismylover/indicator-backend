# -*-  coding:utf-8 -*-
class WordFeature:
    """这个类包含最常用字和次常用字的特征"""

    def __init__(self, most_com_word, second_com_word):
        """
        函数作用：获得词库中的最常用字和次常用字
        :param most_com_word:
        :param second_com_word:
        """
        self.mostComWord = most_com_word
        self.secondComWord = second_com_word

    def get_most_word(self, chinese_word):
        """
        函数作用：获得文档中的最常用字
        :param: 文档中所有的字
        :return: 文档中的最常用字
        """
        most = []  # 最常用字
        for i in chinese_word:
            if i in self.mostComWord:
                most.append(i)
        return most

    def get_second_word(self, chinese_word):
        """
        函数作用：获得文档中的次常用字
        :param: 文档中所有的字
        :return: 文档中的次常用字
        """
        second = []  # 次常用字
        for i in chinese_word:
            if i in self.secondComWord:
                second.append(i)
        return second

    def get_percentage_most_word_per_doc(self, chinese_word):
        """
         函数作用：获得文档中的最常用字的占比
        :param: 文档中所有的字
        :return: 获得文档中的最常用字的占比
        """
        mostWord = self.get_most_word(chinese_word)
        mostWordFeature = round(len(mostWord) * 1.0 / len(chinese_word), 4)
        return mostWordFeature

    def get_percentage_second_word_per_doc(self, chinese_word):
        """
         函数作用：获得文档中的次常用字的占比
        :param: 文档中所有的字
        :return: 获得文档中的次常用字的占比
        """
        second_word = self.get_second_word(chinese_word)
        second_word_feature = round(len(second_word) * 1.0 / len(chinese_word), 4)
        return second_word_feature

    def get_percentage_all_most_word_per_doc(self, chinese_word):
        """
            函数作用：获得文档中的总最常用字的占比
           :param: 文档中所有的字
           :return: 获得文档中的总最常用字的占比
        """
        return self.get_percentage_most_word_per_doc(
            chinese_word) + self.get_percentage_second_word_per_doc(chinese_word)
