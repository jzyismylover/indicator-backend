# -*-  coding:utf-8 -*-
class LexicalFeatureMethod:
    def __init__(self, words, tags) -> None:
        self.words = words # 分词结果数组
        self.tags = tags # 词性标注结果数组

    def get_word(self):
        """
        这个函数用于去掉文章的标点符号并得到句子的分词结果
        para:句子
        return:句子的分词结果列表
        """
        line_word = []
        for i, tag in enumerate(self.tags):
            if tag != 'wp':
                line_word.append(self.words[i])
        return line_word

    def get_feature(self, pattern):
        """
        这个函数用于得到文章的特征词
        para:一篇文章的所有词，特征词的标识
        return:该篇文章的该特征词
        """
        feature = []
        for i, tag in enumerate(self.tags):
            tag = tag
            if pattern == tag:
                feature.append(self.words[i])
        return feature

    def get_multi_feature(self, patterns):
        """
        这个函数用于得到文章的特征列表的所有特征词
        para:一篇文章的所有词，特征词的标识的列表
        return:该篇文章的该特征列表的所有特征词
        """
        feature = []
        for i, tag in enumerate(self.tags):
            if tag in patterns:
                feature.append(self.words[i])
        
        return feature

    def get_terminology_feature(self, all_word, terminology_list):
        feature = []
        for word in all_word:
            if word in terminology_list:
                feature.append(word)
        return feature
