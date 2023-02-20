import re
from utils.useForFactory import Base_Utils
from hanlp_restful import HanLPClient

HanLP = HanLPClient(
    url='https://www.hanlp.com/api',
    auth='MTkxOUBiYnMuaGFubHAuY29tOjdGd0I3STZPQ0xoU2lvdHo=',
    language='mul',
)


class ID_Utils(Base_Utils):
    def get_sentences(self, text):
        sentences = re.split(r'[?!.,]', text)
        return sentences

    def get_words(self, sentences):
        words = []
        tags = []

        for i, sentence in enumerate(sentences):
            if sentence is '':
                continue
            ans = HanLP.parse(sentence)
            words.extend([x for x in ans['tok'][0]])
            tags.extend([x for x in ans['pos'][0]])

        self.tags = tags
        return words

    def get_word_character(self, words):
        return self.tags