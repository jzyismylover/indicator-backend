# -*-  coding:utf-8 -*-
import re


class SyntacticFeatureMethod:
    """这个是句法特征的方法类"""

    def find_all_terms_by_feature(self, content, feature):
        result = []
        list = self.get_word_sub_str(content, feature[0], feature[1])
        for each in list:
            temp_str = self.find_sub_string(each, feature)
            if temp_str is not None:
                temp_str = self.remove_tag(temp_str)
                result.append(temp_str + "\n")
        return result

    @staticmethod
    def get_word_sub_str(content, feature_1, feature_2):
        result = []
        for line in content:
            str_list = list(line)
            index = 0
            mark = []

            start = 0
            flag = 0
            for each in str_list:
                if each == "(":
                    try:
                        if flag == 0:
                            if str_list[index + 1] == feature_1:
                                if str_list[index + 2] == feature_2:
                                    flag = index
                        mark.append(index)
                    except:
                        break
                if each == ")":
                    try:
                        sub_str_start_index = mark[len(mark) - 1]
                        sub_str_end_index = index + 1
                        if sub_str_start_index == flag:
                            flag = 0
                            result.append(line[sub_str_start_index:sub_str_end_index])
                        mark.pop()
                    except:
                        break
                index = index + 1
        return result

    @staticmethod
    def remove_tag(content):
        line = re.sub(r"[A-Z() 0-9,.%+-_a-z]", "", content)
        return line

    @staticmethod
    def find_sub_string(content, feature):
        end = len(feature) + 1
        if content[1:end] == feature:
            return content

    @staticmethod
    def get_ic_sentence(source_str):
        ip = []
        sentence_ic = []
        sentence_head = False
        for index in range(len(source_str)):
            if source_str[index : index + 4] == '(TOP':
                sentence_head = True
            if sentence_head:
                if source_str[index : index + 3] == '(IP':
                    sentence_ic.append(str(index))
                    sentence_head = False
            if source_str[index : index + 3] == '(IP':
                ip.append(str(index))

        return sentence_ic, ip

    @staticmethod
    def count_high_of_tree(trees):
        trees_height = []
        for tree in trees:
            trees_height.append(tree.height)

        return trees_height

    @staticmethod
    def count_dependent_distance(file_path):
        file = open(file_path, 'r', encoding='utf-8')
        lines = file.readlines()
        sum_dep = 0  # 依存距离总和
        sentence_count = 0  # 句子数
        for line in lines:
            line = line.strip()
            word_list = re.findall('\((.*?)\)', line)
            for word in word_list:
                word = word.split(',')
                dep = word[0]
                governor = word[1]
                dependent = word[2]
                if 'ROOT' in dep:
                    sentence_count += 1
                else:
                    dep_parser = abs(int(governor) - int(dependent))
                    sum_dep += dep_parser
        avg_dep = sum_dep / sentence_count

        return sum_dep, avg_dep

    @staticmethod
    def count_punctuation(word_list):
        # 去除一个词语列表中非中文的词语
        def chinese(word_list):
            c_list = []
            for word in word_list:
                if word >= u'\u4e00' and word <= u'\u9fa5':
                    c_list.append(word)
            return c_list

        # 计算标点句的个数sentence及标点句平均词数word_v
        def is_punctuation(word):
            word = word.strip(' ')
            word = word.strip('\r\n')

            punctuation_list = [
                '，',
                ',',
                '。',
                '；',
                ';',
                '：',
                ':',
                '？',
                '?',
                '！',
                '!',
                '······',
                '……',
                '......',
            ]
            for punctuation in punctuation_list:
                if punctuation in word:
                    return True
            return False

        c_list = chinese(word_list)
        n = 0
        for word in word_list:
            if is_punctuation(word):
                n += 1
        punctuation_num = n
        if punctuation_num == 0:
            punctuation_num = 1
        mean_word_in_punctuation = len(c_list) / punctuation_num
        return punctuation_num, mean_word_in_punctuation
