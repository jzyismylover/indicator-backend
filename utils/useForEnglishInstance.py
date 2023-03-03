import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag
from utils.useForFactory import Base_Utils
from utils.constant import EN_SPECIAL_WORDS as SYMBOLS


class EN_Utils(Base_Utils):
    def get_sentences(self, text):
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        sentences = tokenizer.tokenize(text)
        return sentences

    def get_words(self, sentences):
        all_words = []
        for sentence in sentences:
            words = word_tokenize(sentence, preserve_line=True)
            filtered_words = []
            for word in words:
                if re.search('[a-zA-Z0-9]', word) is None:
                    pass
                else:
                    for _ in SYMBOLS:
                        word = word.replace(_, '')
                    filtered_words.append(word.lower())
            all_words.extend(filtered_words)
        return all_words

    def get_word_character(self, words):
        tags = pos_tag(words)
        return tags

    def get_noun_words(self, tags, words=[]):
        noun_words = []
        for _, tag in tags:
            if self.is_noun_word(tag):
                noun_words.append(_)
        return noun_words

    def get_verb_words(self, tags, words=[]):
        verb_words = []
        for _, tag in tags:
            if self.is_verb_word(tag):
                verb_words.append(_)
        return verb_words

    def get_adjective_words(self, tags, words=[]):
        adjective_words = []
        for _, tag in tags:
            if self.is_adjective_word(tag):
                adjective_words.append(_)
        return adjective_words

    def get_real_words(self, tags, words=[]):
        real_words = []

        for _, tag in tags:
            if self.is_real_word(tag):
                real_words.append(_)
        real_words = [i for i in set(real_words)]

        return real_words

    def is_verb_word(self, tag):
        if tag in ('VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'):
            return True
        else:
            return False

    def is_adjective_word(self, tag):
        if tag in ('JJ', 'JJR', 'JJS'):
            return True
        else:
            return False

    def is_noun_word(self, tag):
        if tag in ('NN', 'NNS', 'NNP', 'NNPS'):
            return True
        else:
            return False

    def is_real_word(self, tag):
        function_word_tags = ['CC', 'DT', 'IN', 'PDT', 'RP', 'TO', 'UH']
        if tag not in function_word_tags:
            return True
        else:
            return False
