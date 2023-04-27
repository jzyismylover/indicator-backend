# -*-  coding:utf-8 -*-
import xlrd


class ShallowFeatureMethod:
    """这个类包含求浅层特征中间文件的方法"""

    @staticmethod
    def get_excel(filename):
        """
        函数作用：从现代汉语常用字表中获得最常用字和次常用字
        para: 现代汉语常用字表的路径
        return:最常用字和次常用字的列表
        """
        file = xlrd.open_workbook(filename)
        # 创建索引顺序获取一个工作表
        table = file.sheet_by_index(0)
        # 获取行数和列数
        nrows = table.nrows
        most_com_word = []
        second_com_word = []
        for i in range(1, nrows):
            if table.cell(i, 1).value == "1":
                most_com_word.append(table.cell(i, 0).value)
            else:
                second_com_word.append(table.cell(i, 0).value)
        return most_com_word, second_com_word

    @staticmethod
    def get_txt(filename):
        """
        函数作用：从财经术语词典中获取财经术语词汇列表
        :param filename: 财经术语词典的路径
        :return: 财经术语词汇列表
        """
        txt_content = []
        file = open(filename, "r", encoding="utf-8")
        for line in file:
            txt_content.append(line.strip())
        return txt_content

    @staticmethod
    def get_character(words) -> str:
        """
        函数作用：得到文章的所有字符
        para:文章内容
        return:该文章的所有字符
        """
        return ''.join(words)

    @staticmethod
    def get_all_word(words) -> list:
        """
        函数作用：得到文章的所有词
        para:已经分词的文章内容, 该文章的所有标点符号
        return:该文章的所有的词
        """
        all_word = []
        for i in words:
            if u'\u4e00' <= i <= u'\u9fa5':
                all_word.append(i)
        return all_word

    @staticmethod
    def get_chinese(content):
        """
        函数作用：得到文章的所有汉字
        para:文章内容
        return:该文章的所有汉字
        """
        chinese = []
        line = content.replace('\r\n', '').replace('\n', '')
        for each in line:
            if u'\u4e00' <= each <= u'\u9fa5':
                chinese.append(each)
        return chinese

    @staticmethod
    def get_gram_word(all_word):
        """
        函数作用：得到文章的两字词语，三字词语，四字词语，以及四字以上的词语
        para:文章的所有的词
        return:该文章的两字词语，三字词语，四字词语，以及四字以上的词语
        """
        one_word = []
        two_word = []
        three_word = []
        four_word = []
        more_word = []
        for word in all_word:
            len_of_word = len(word)
            # print word+" "+str(len_of_word)
            if len_of_word == 1:
                one_word.append(word)
            elif len_of_word == 2:
                two_word.append(word)
            elif len_of_word == 3:
                three_word.append(word)
            elif len_of_word == 4:
                four_word.append(word)
            else:
                more_word.append(word)
        return one_word, two_word, three_word, four_word, more_word

    @staticmethod
    def count_character(word_list):
        """
        函数作用：得到词语列表的总字数
        para:词语列表
        return:词语列表的总字数
        """
        num = 0
        for i in word_list:
            num = num + len(i)
        return num
