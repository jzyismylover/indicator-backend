# -*-  coding:utf-8 -*-
class NamedEntityFeature:
    """这个类包含了命名实体词相关的特征"""

    def __init__(self, named_entity):
        self.namedEntity = named_entity

    def get_percentage_named_entity_per_doc(self, all_word):
        """
        函数作用：得到文档的命名实体词在文档总词数的占比
        :parameter:文档的所有词
        :return: 文档的命名实体词在文档总词数的占比
        """
        named_entity_feature = round(len(self.namedEntity) * 1.0 / len(all_word), 4)
        return named_entity_feature

    def get_average_named_entity_per_sentence(self, num_of_line):
        """
        函数作用：得到文档的单句平均命名实体词数量
        :parameter:文档的句子数
        :return: 文档的单句平均命名实体词数量
        """
        average_named_entity_feature = round(len(self.namedEntity) * 1.0 / num_of_line, 4)
        return average_named_entity_feature

    def get_percentage_named_entity_in_entity(self, entity):
        """
        函数作用：得到文档的命名实体词在文档实体词的占比
        :parameter:文档的所有词
        :return: 文档的命名实体词在文档总词数的占比
        """
        if len(entity) == 0:
            n_e_to_sub = 0
        else:
            n_e_to_sub = round(len(self.namedEntity) * 1.0 / len(entity), 4)
        return n_e_to_sub
