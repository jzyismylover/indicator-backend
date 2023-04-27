# -*-  coding:utf-8 -*-
import os
from resources.zh_readability.method.lexical_feature_method import LexicalFeatureMethod
from resources.zh_readability.method.shallow_feature_method import ShallowFeatureMethod
from resources.zh_readability.method.stroke_feature_method import StrokeFeatureMethod
# from resources.zh_readability.feature_bean.syntactic_feature import SyntacticFeature

# from resources.zh_readability.method.syntactic_feature_method import SyntacticFeatureMethod


class DataSet:
    def __init__(self, raw_text, sentences, words, tags):
        # 挂载原文本、分句、分词
        (self.raw_text, self.sentences, self.words, self.tags) = (
            raw_text,
            sentences,
            words,
            tags,
        )
        self.v_lines = len(sentences)

        # 实例化各类特征的方法
        self.lfm = LexicalFeatureMethod(words, tags)  # 词汇特征
        self.sfm = ShallowFeatureMethod()
        self.strokes_method = StrokeFeatureMethod()  # 笔画特征
        # self.syfm = SyntacticFeatureMethod() # 句法特征
        # self.sf = SyntacticFeature()  #
        self.strokes_list = self.strokes_method.get_model()  # 获得汉字笔画大全的列表
        (
            self.most_com_word,
            self.second_com_word,
        ) = self.sfm.get_excel(  # 获取最常用&第二常用文字列表
            os.path.join('static', 'strokes_file', '现代汉语常用字表.xlsx')
        )
        self.terminology_list = self.sfm.get_txt(  # 获取财经术语词典
            os.path.join('static', 'strokes_file', '财经术语词典.txt')
        )
        self.features_dict = {}  # 特征字典
