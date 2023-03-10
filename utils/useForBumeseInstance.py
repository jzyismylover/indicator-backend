# -*- coding: utf-8 -*-

"""
缅甸语
"""
import re
from utils.useForFactory import BaseUtils

class BUUtils(BaseUtils):
    def get_sentences(self, text):
        """
        ။(taa gun)：用于分割句子。相当于英文中的句号。
        ၊(nya yit)：用于分割短语或词组。相当于英文中的逗号。
        ၍(lae gyi)：用于表示省略或缩写。相当于英文中的省略号或缩写号。
        """
        sentence_breaks = r'[။၊၍?!,]'
        sentences = re.split(sentence_breaks, text)
        return sentences
