# -*-  coding:utf-8 -*-
class NonnamedEntityNounFeature:
    """这个类包含了非实体名词的相关特征"""

    def __init__(self, not_name_entity_noun):
        self.notNameEntityNoun = not_name_entity_noun

    def get_percentage_not_name_entity_noun_per_doc(self, all_word):
        """
        函数作用：得到文档的非命名实体名词在文档总词数的占比
        :parameter:文档的所有词
        :return: 文档的非命名实体名词在文档总词数的占比
        """
        not_name_entity_noun_feature = round(
            len(self.notNameEntityNoun) * 1.0 / len(all_word), 4
        )
        return not_name_entity_noun_feature

    def get_average_not_name_entity_noun_per_sentence(self, num_of_line):
        """
        函数作用：得到文档的单句非命名实体词的数量
        :parameter:文档的句子数
        :return: 文档的单句非命名实体词的数量
        """
        not_name_entity_noun_feature = round(
            len(self.notNameEntityNoun) * 1.0 / num_of_line, 4
        )
        return not_name_entity_noun_feature
