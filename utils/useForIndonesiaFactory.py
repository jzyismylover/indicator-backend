import re
import hanlp
from utils.useForFactory import Base_Utils
from utils import UNIVERSAL_HANLP as Hanlp

class ID_Utils(Base_Utils):
    def get_sentences(self, text):
        sentences = re.split(r'[?!.,]', text)
        return sentences

    def get_words(self, sentences):
        words = []
        tags = []

        for sentence in sentences:
            if len(sentences) == 0:
                continue
            ans = Hanlp(sentence, tasks='ud')
            words.extend([x for x in ans['tok']])
            tags.extend([x for x in ans['pos']])

        self.tags = tags
        return words

    def get_word_character(self, words):
        return self.tags