import abc
import numpy as np
from utils.hanlp import UNIVERSAL_HANLP as Hanlp
from sentry_sdk import capture_exception


class BaseUtils(object):
    # GET 词频list
    def get_word_frequency(self, words):
        hapax = []
        frequency = []
        words_set = set(words)

        for word in words_set:
            frequency.append({'num': words.count(word), 'word': word})
            if words.count(word) == 1:
                hapax.append(word)

        frequency = sorted(
            frequency, key=lambda row: (row['num'], row['word']), reverse=True
        )
        return {
            'frequency': [i for i in map(lambda row: row['num'], frequency)],
            'frequency_words': [i for i in map(lambda row: row['word'], frequency)],
            'hapax': hapax,
        }

    def is_verb_word(self, tag):
        if tag == 'VERB':
            return True
        else:
            return False

    def is_adjective_word(self, tag):
        if tag == 'ADJ':
            return True
        else:
            return False

    def is_real_word(self, tag):
        REAL_WORD_LIST = ['ADJ', 'NOUN', 'NUM', 'PRON', 'PROPN', 'VERB']
        if tag in REAL_WORD_LIST:
            return True
        else:
            return False

    def get_verb_words(self, tags, words=[]):
        verb_words = []
        for i, tag in enumerate(tags):
            if self.is_verb_word(tag):
                verb_words.append(words[i])

        return verb_words

    # GET 形容词列表
    def get_adjective_words(self, tags, words=[]):
        adjective_words = []
        for i, tag in enumerate(tags):
            if self.is_adjective_word(tag):
                adjective_words.append(words[i])

        return adjective_words

    # GET 实词列表
    def get_real_words(self, tags, words=[]):
        real_words = []
        for i, tag in enumerate(tags):
            if self.is_real_word(tag):
                real_words.append(words[i])

        return [i for i in set(real_words)]

    # GET 分句列表
    @abc.abstractmethod
    def get_sentences(self, text):
        pass
        
    # GET 分词列表
    def get_words(self, sentences):
        words = []
        tags = []
        SENTENCES_LIMIT = 6  # 单次处理的句子数
        i = 0

        while i < len(sentences):
            try:
                sentence = sentences[i : i + SENTENCES_LIMIT]
                ans = Hanlp(sentence, tasks='ud')
                words.extend([i for j in ans['tok'] for i in j])
                tags.extend([i for j in ans['pos'] for i in j])
            except Exception as e:
                capture_exception(e)
                pass
            finally:
                i = i + SENTENCES_LIMIT

        self.tags = tags
        return words

    # GET 词性标注
    def get_word_character(self, words):
        return self.tags
