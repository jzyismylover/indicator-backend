import re
import hanlp
from utils.useForFactory import Base_Utils
from hanlp.components.mtl.multi_task_learning import MultiTaskLearning
from utils.constant import ZH_SPECIAL_WORDS as SYMBOLS
from utils import JA_HANLP as Hanlp


class JP_Utils(Base_Utils):
    def __init__(self) -> None:
        super().__init__()

    def get_sentences(self, text: str):
        p = re.compile(r'(“.*?”)|(.*?[。！？…]{1,2}”?)')
        text = text.replace('\n', '')
        sentences = []
        for i in p.finditer(text):
            temp = text[i.start() : i.end()]
            if temp != '':
                sentences.append(temp)

        return sentences

    def get_words(self, sentences):
        words = []
        for sentence in sentences:
            ans = Hanlp(sentence, tasks=['tok/fine'])
            words.extend([i for i in ans['tok/fine'] if i not in SYMBOLS])

        return words

    def get_word_character(self, words=[]):
        tags = Hanlp(words, tasks='pos/npcmj')
        return tags['pos/npcmj']

    def is_adjective_words(self, tag):
        if re.match('ADJI', tag) is not None:
            return True
        else:
            return False

    def is_verb_word(self, tag):
        if re.match('VB', tag) is not None:
            return True
        else:
            return False

    def is_real_word(self, tag):
        pattern = re.compile(r'ADJJ|N|NUM|VB')
        if re.match(pattern, tag) is not None:
            return True
        else:
            return False
