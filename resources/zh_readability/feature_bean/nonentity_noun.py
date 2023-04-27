# -*-  coding:utf-8 -*-
class NonentityNoun:
    """这个类包含非实体词的相关的特征"""

    def __init__(self, not_entity_noun):
        self.notEntityNoun = not_entity_noun

    def get_average_not_entity_noun_per_sentence(self, num_of_line):
        """
        函数作用：得到文档的单句平均非实体词数量
        :param:numOfLine
        :return: 文档的单句平均非实体词数量
        """
        average_not_entity_noun = round(len(self.notEntityNoun) * 1.0 / num_of_line, 4)
        return average_not_entity_noun
