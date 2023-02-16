import abc


class Base_Utils(object):
    # GET 分句列表
    @abc.abstractmethod
    def get_sentences(self, text):
        pass

    # GET 分词列表
    @abc.abstractmethod
    def get_words(self, sentences):
        pass

    # GET 词频list
    def get_word_frequency(self, words) -> None:
        pass

    # GET hPoint
    def get_h_value(self) -> None:
        pass

    # GET 词性标注
    @abc.abstractmethod
    def get_word_character(self, words):
        pass

    # GET 动词列表
    @abc.abstractmethod
    def get_verb_words(self, tags, words=[]):
        pass

    # GET 形容词列表
    @abc.abstractmethod
    def get_adjective_words(self, tags, words=[]):
        pass

    # GET 实词列表
    @abc.abstractmethod
    def get_real_words(self, tags, words=[]):
        pass
