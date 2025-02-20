# -*-  coding:utf-8 -*-
from resources.zh_readability.method.tools import unique


class EntityFeature:
    """这个类包含了实体词相关的特征"""

    def __init__(self, entity):
        self.entity = entity

    def get_num_of_entity(self):
        """
        函数作用：得到文档的实体词总数
        :return: 文档的实体词总数
        """
        num_of_entity = len(self.entity)
        return num_of_entity * 1.0

    def get_num_of_unique_entity(self):
        """
        函数作用：得到文档的唯一实体词总数
        :return: 文档的唯一实体词总数
        """
        unique_entity = unique(self.entity)
        num_of_unique_entity = len(unique_entity)
        return num_of_unique_entity * 1.0

    def get_percentage_entity_per_doc(self, all_word):
        """
        函数作用：得到文档的实体词在文档总词数的占比
        :parameter:文档的所有词
        :return: 文档的实体词在文档总词数的占比
        """
        entity_feature = round(len(self.entity) * 1.0 / len(all_word), 4)
        return entity_feature

    def get_percentage_unique_entity_per_doc(self, all_word):
        """
        函数作用：得到文档的唯一实体词在文档总词数的占比
        :parameter:文档的所有词
        :return: 文档的唯一实体词在文档总词数的占比
        """
        unique_entity_feature = round(len(unique(self.entity)) * 1.0 / len(all_word), 4)
        return unique_entity_feature

    def get_average_entity_per_sentence(self, num_of_line):
        """
        函数作用：得到文档的单句平均实体词数量
        :parameter:文档的总句数
        :return: 文档的单句平均实体词数量
        """
        average_entity = round(len(self.entity) * 1.0 / num_of_line, 4)
        return average_entity

    def get_average_unique_entity_per_sentence(self, num_of_line):
        """
        函数作用：得到文档的单句平均唯一实体词数量
        :parameter:文档的总句数
        :return: 文档的单句平均唯一实体词数量
        """
        average_unique_entity = round(len(unique(self.entity)) * 1.0 / num_of_line, 4)
        return average_unique_entity
