import re
from utils.useForFactory import Base_Utils
from hanlp_restful import HanLPClient

HanLP = HanLPClient(
    url='https://www.hanlp.com/api',
    auth='MTkxOUBiYnMuaGFubHAuY29tOjdGd0I3STZPQ0xoU2lvdHo=',
    language='mul',
)


class JP_Utils(Base_Utils):
    def __init__(self) -> None:
        super().__init__()

    def get_sentences(self, text: str):
        sentences = re.split(r'[！，。？、]', text)
        return sentences

    def get_words(self, sentences):
        words = []
        tags = []
        for sentence in sentences:
            if sentence is '':
                continue
            ans = HanLP.parse(sentence)
            words.extend([i for i in ans['tok'][0]])
            tags.extend([i for i in ans['pos'][0]])

        self.tags = tags
        return words

    def get_word_character(self, words):
        return self.tags

    def is_adjective_words(self, tag):
        if re.match('JJ', tag) is not None:
            return True
        else:
            return False

    def is_verb_word(self, tag):
        if re.match('VV', tag) is not None:
            return True
        else:
            return False

    def is_real_word(self, tag):
        pattern = re.compile(r'JJ|VV|VA|NR|M|DT')
        if re.match(pattern, tag) is not None:
            return True
        else:
            return False
