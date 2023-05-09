# -*-  coding:utf-8 -*-
import re


class SyntacticFeature:
    @staticmethod
    def get_num_of_ic_per_doc(ic_result):
        """
        函数作用：得到文档的含子句的句子的个数
        :param ic_result:
        :return:文档的含子句的句子的个数
        """
        sum = 0
        for each in ic_result:
            if len(re.findall("IC", each)) != 0:
                sum = sum + 1
        return sum * 1.0

    @staticmethod
    def get_num_of_word_phrase_per_doc(result):
        """
        函数作用：得到文档的xx(NP,PP,VP)短语总数
        :param:result
        :return:文档的名词短语总数
        """
        return len(result) * 1.0

    @staticmethod
    def get_num_of_word_phrase_per_sentence(result, num_of_line):
        """
        函数作用：得到句子的平均xx(NP,VP)短语个数
        :param result:
        :param num_of_line:
        :return:
        """
        return round(len(result) * 1.0 / num_of_line, 4)

    @staticmethod
    def get_average_length_word_phrase(result: list):
        """
        函数作用：得到xx(NP,PP,VP)短语的平均长度
        :param result:
        :return: 得到xx(NP,PP,VP)短语的平均长度
        """
        length = len(result)
        sum = 0
        for i in result:
            sum = sum + len(i)
        if length == 0:
            return 0
        else:
            return round(sum * 1.0 / length, 4)

    @staticmethod
    def get_average_ic_per_sentence(num_of_ic, num_of_line):
        """
        函数作用：得到句子的平均子句个数
        :param num_of_ic:
        :param num_of_line:
        :return: 句子的平均子句个数
        """
        return round(num_of_ic * 1.0 / num_of_line, 4)

    @staticmethod
    def get_average_non_ic_per_sentence(num_of_ic, num_of_line):
        """
            函数作用：得到文档的不含有子句的句子占句子总数的占比
            :param num_of_ic:
            :param num_of_line:
            :return: 得到文档的不含有子句的句子占句子总数的占比
            """
        return round((num_of_line - num_of_ic) * 1.0 / num_of_line, 4)

    @staticmethod
    def get_high_of_syntactic_tree(tree_result):
        """
        函数作用：得到文档平均句法树高度
        :param tree_result:
        :return: 文档平均句法树高度
        """
        high = 0
        for each in tree_result:
            high = high + each
        average = round(high * 1.0 / len(tree_result), 4)
        return average
