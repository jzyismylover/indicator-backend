"""
他加禄语(菲律宾语)
"""
import re
import hanlp
from utils.useForFactory import Base_Utils

SPECIAL_CHARS = ['.', ',', '!', '?', '\n']

Hanlp = hanlp.load(
    hanlp.pretrained.mtl.UD_ONTONOTES_TOK_POS_LEM_FEA_NER_SRL_DEP_SDP_CON_MMINILMV2L6
)


class TA_Utils(Base_Utils):
    def get_sentences(self, text):
        sentences = re.split('[?!.,]', text)
        print(sentences)
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
