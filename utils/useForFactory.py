import abc


class Base_Utils(object):
    def __init__(self) -> None:
        self.sentences = []
        self.words = []
        self.frequency = []
        self.h_value = 0
        self.tags = []
        self.hapax = []

    # GET 分词列表
    @abc.abstractmethod
    def get_words(self):
        pass

    # GET 词频字典
    def get_word_frequency(self) -> None:
        pass

    # GET h_value
    def get_h_value(self) -> None:
        pass

    # GET 词性标注
    @abc.abstractmethod
    def get_word_character(self):
        pass

    # GET 动词列表
    @abc.abstractmethod
    def get_verb_words(self):
        pass

    # GET 形容词列表
    @abc.abstractmethod
    def get_adjective_words(self):
        pass
    
    @abc.abstractmethod
    def get_real_words(self):
      pass
