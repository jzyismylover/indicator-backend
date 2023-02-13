import re
from nltk.tokenize import sent_tokenize
from nltk import pos_tag, word_tokenize
from utils.useForFactory import Base_Utils

SPECIAL_CHARS = ['.', ',', '!', '?']


class EN_Utils(Base_Utils):
    def get_sentences(self, text):
        return sent_tokenize(text)

    def get_words(self, sentences):
        all_words = []
        for sentence in sentences:
            words = word_tokenize(sentence)
            filtered_words = []
            for word in words:
                if re.search('[a-zA-Z0-9]', word) is None:
                    pass
                else:
                    new_word = word.replace(",", "").replace(".", "").replace(";", "")
                    new_word = (
                        new_word.replace("!", "").replace("?", "").replace("\'", "")
                    )
                    filtered_words.append(new_word.lower())
            all_words.extend(filtered_words)
        return all_words

    def get_word_frequency(self, words) -> dict:
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
            'hapax': hapax
        }

    def get_word_character(self, words):
        tags = pos_tag(words)
        return tags
        

    def get_noun_words(self, tags, words=[]):
        noun_words = []
        for tag in tags:
            if tag[1] in ('NN', 'NNS', 'NNP', 'NNPS'):
                noun_words.append(tag[0])
        return noun_words

    def is_verb_word(self, tag):
        if tag in ('VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'):
            return True
        else:
            return False

    def get_verb_words(self, tags, words=[]):
        verb_words = []
        for tag in tags:
            if self.is_verb_word(tag[1]):
                verb_words.append(tag[0])
        return verb_words

    def get_adjective_words(self, tags, words=[]):
        adjective_words = []
        for tag in tags:
            if tag[1] in ('JJ', 'JJR', 'JJS'):
                adjective_words.append(tag[0])
        return adjective_words

    def get_real_words(self, tags, words=[]):
        real_words = []
        function_word_tags = ['CC', 'DT', 'IN', 'PDT', 'RP', 'TO', 'UH']

        for _, tag in tags:
            if function_word_tags.count(tag) == 0:
                real_words.append(_)
        real_words = [i for i in set(real_words)]

        return real_words
