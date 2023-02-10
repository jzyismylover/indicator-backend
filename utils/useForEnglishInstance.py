import re
from nltk.tokenize import sent_tokenize
from nltk import pos_tag, word_tokenize
from utils.useForFactory import Base_Utils

SPECIAL_CHARS = ['.', ',', '!', '?']

class EN_Utils(Base_Utils):
    def __init__(self, text: str) -> None:
        self.text = text
        self.sentences = sent_tokenize(text)
        self.words = self.get_words()
        self.hapax = []  # 单现词
        self.frequency_words = [] # 单词排序列表
        self.frequency = self.get_word_frequency() # 单词数量排序列表
        self.tags = []
        self.real_words = []
        self.h_value = 0

    def get_words(self):
        all_words = []
        for sentence in self.sentences:
            words = word_tokenize(sentence)
            filtered_words = []
            for word in words:
                if re.search('[a-zA-Z0-9]', word) is None:
                    pass
                else:
                    new_word = word.replace(",", "").replace(".", "").replace(";", "")
                    new_word = new_word.replace("!", "").replace("?", "").replace("\'", "")
                    filtered_words.append(new_word.lower())
            all_words.extend(filtered_words)
        return all_words

    def get_word_frequency(self) -> dict:
        frequency = []
        words_set = set(self.words)

        for word in words_set:
            frequency.append({'num': self.words.count(word), 'word': word})
            if self.words.count(word) == 1:
                self.hapax.append(word)

        frequency = sorted(frequency, key=lambda row: (row['num'], row['word']), reverse=True)
        self.frequency_words = [i for i in map(lambda row: row['word'], frequency)]
        return [i for i in map(lambda row: row['num'], frequency)]

    def get_h_value(self):
        h_value = 0
        for num, fre in enumerate(self.frequency):
            if num + 1 == fre:
                h_value = fre
                break

        if h_value == 0:
            fi = 0
            fj = 0
            ri = 0
            rj = 0
            for num, fre in enumerate(self.frequency):
                if num + 1 <= fre:
                    fi = fre
                    ri = num + 1
            for num, fre in enumerate(self.frequency):
                if num + 1 >= fre:
                    fj = fre
                    rj = num + 1
                    break
            h_value = (rj * fi - ri * fj) / (rj - ri + fi - fj)
        self.h_value = h_value

    def get_word_character(self):
        self.tags = pos_tag(self.words)

    def get_noun_words(self):
        if len(self.tags) == 0:
            self.get_word_character()
        noun_words = []
        for tag in self.tags:
            if tag[1] in ('NN', 'NNS', 'NNP', 'NNPS'):
                noun_words.append(tag[0])
        return noun_words

    def is_verb_word(self, tag):
        if tag in ('VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'):
            return True
        else: 
            return False
    def get_verb_words(self):
        if len(self.tags) == 0:
            self.get_word_character()
        verb_words = []
        for tag in self.tags:
            if self.is_verb_word(tag[1]):
                verb_words.append(tag[0])
        return verb_words

    def get_adjective_words(self):
        if len(self.tags) == 0:
            self.get_word_character()
        adjective_words = []
        for tag in self.tags:
            if tag[1] in ('JJ', 'JJR', 'JJS'):
                adjective_words.append(tag[0])
        return adjective_words

    def get_real_words(self):
        if len(self.tags) == 0:
            self.get_word_character()

        function_word_tags = ['CC', 'DT', 'IN', 'PDT', 'RP', 'TO', 'UH']

        for _, tag in self.tags:
            if function_word_tags.count(tag) == 0:
                self.real_words.append(_)
        self.real_words = [i for i in set(self.real_words)]