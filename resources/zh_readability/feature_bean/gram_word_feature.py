# -*-  coding:utf-8 -*-
class GramWordFeature:
    """这个类包含GramWord的相关特征"""

    def __init__(self, one_word, two_word, three_word, four_word, more_word):
        """
        将文章的两字词语，三字词语，四字词语，以及四字以上的词语列表作为参数初始化该类
        :param one_word:
        :param two_word:
        :param three_word:
        :param four_word:
        :param more_word:
        """
        self.oneWord = one_word
        self.twoWord = two_word
        self.threeWord = three_word
        self.fourWord = four_word
        self.moreWord = more_word

    def get_num_of_two_word(self):
        """
        函数作用：得到文档的两字词语的个数
        :return: 文档的两字词语的个数
        """
        return len(self.twoWord) * 1.0

    def get_num_of_three_word(self):
        """
        函数作用：得到文档的三字词语的个数
        :return: 文档的三字词语的个数
        """
        return len(self.threeWord) * 1.0

    def get_num_of_four_word(self):
        """
        函数作用：得到文档的四字词语的个数
        :return: 文档的四字词语的个数
        """
        return len(self.fourWord) * 1.0

    def get_num_of_more_word(self):
        """
        函数作用：得到文档的多字词语的个数
        :return: 文档的多字词语的个数
        """
        return len(self.moreWord) * 1.0

    def get_percentage_two_word_per_doc(self, all_word):
        """
        函数作用：得到文档的两字词语的占比
        :param 文档的所有词的列表
        :return: 文档的两字词语的占比
        """
        gram_word2 = round(len(self.twoWord) * 1.0 / len(all_word), 4)
        return gram_word2

    def get_percentage_three_word_per_doc(self, all_word):
        """
        函数作用：得到文档的三字词语的占比
        :param 文档的所有词的列表
        :return: 文档的三字词语的占比
        """
        gram_word3 = round(len(self.threeWord) * 1.0 / len(all_word), 4)
        return gram_word3

    def get_percentage_four_word_per_doc(self, all_word):
        """
        函数作用：得到文档的四字词语的占比
        :param 文档的所有词的列表
        :return: 文档的四字词语的占比
        """
        gram_word4 = round(len(self.fourWord) * 1.0 / len(all_word), 4)
        return gram_word4

    def get_percentage_more_word_per_doc(self, all_word):
        """
        函数作用：得到文档的多字词语的占比
        :param 文档的所有词的列表
        :return: 文档的多字词语的占比
        """
        gram_word_more = round(len(self.moreWord) * 1.0 / len(all_word), 4)
        return gram_word_more

    def get_average_more_word_per_sentence(self, num_of_lines):
        """
        函数作用：得到单句的平均多词词语的个数
        :param num_of_lines:
        :return: 单句的平均多词词语的个数
        """
        gram_word_all = round((self.get_num_of_two_word() + self.get_num_of_three_word() + self.get_num_of_four_word()
                               + self.get_num_of_more_word()) * 1.0 / num_of_lines, 4)
        return gram_word_all
