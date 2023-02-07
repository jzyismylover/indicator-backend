import os
import jieba
import os
import re
from zhconv import convert
from pyltp import Postagger
from utils.useForFactory import Base_Utils

LTP_DATA_DIR = os.path.join('static', 'ltp_data_v3.4.0')
POS_MODEL_PATH = os.path.join(LTP_DATA_DIR, 'pos.model')
SYMBOLS = [
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'V',
    'W',
    'X',
    'Y',
    'Z',
    '、',
    '1',
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z',
    '：',
    ')',
    '%',
    '。',
    '“',
    '0',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '）',
    ':',
    '！',
    '，',
    '',
    '；',
    '@',
    '(',
    ',',
    '!',
    '（',
    '/',
    '》',
    '&',
    '’',
    '.',
    '”',
    '《',
    '-',
    '—',
    '\n',
    '\u200b',
    'Ｔ',
    '®',
    '％',
    'Ｃ',
    '【',
    'Ｍ',
    '|',
    '…',
    ']',
    '】',
    '－',
    'ñ',
    '？',
    '＊',
    'Ｐ',
    '·',
    '[',
    'Ｘ',
    'Ｓ',
    ';',
    '+',
    'é',
    '‘',
    '"',
    '……',
    '／',
    '●',
    '?',
    '★★☆',
    '★☆',
    '——',
    '.....',
    '★',
    '#',
    '–',
    '＂',
    '~',
    '﹐',
    '★★★',
    '⊙',
    '_',
    '$',
]


class ZH_Utils(Base_Utils):
    def __init__(self, text, is_cut_word=True) -> None:
        self.text = text
        self.words = self.get_words(is_cut_word)
        self.hapax = []
        self.frequency_words = []
        self.frequency = self.get_word_frequency()
        self.tags = []
        self.real_words = []
        self.h_value = 0

    def get_words(self, is_cut_word=False) -> list:
        if is_cut_word == False:
            return convert(self.text, 'zh-cn').strip().split(' ')
        else:
            return [i for i in jieba.cut(self.text.strip()) if i not in SYMBOLS]

    def get_word_frequency(self) -> None:
        words_set = set(self.words)

        temp = []
        frequency = []
        for i in words_set:
            if len(i) >= 1:
                _ = re.findall('[\u4e00-\u9fa5]', i)
                if len(_) != 0:
                    temp.append(i)

        for word in temp:
            num = self.words.count(word)
            if num == 1:
                self.hapax.append(word)
            frequency.append({'word': word, 'num': num})

        frequency = sorted(frequency, key=lambda row: (row['num'], row['word']), reverse=True)
        self.frequency_words = list(map(lambda row: row['word'], frequency))
        return list(map(lambda row: row['num'], frequency))

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
        postagger = Postagger(POS_MODEL_PATH)
        self.tags = [i for i in postagger.postag(self.words)]

    def get_noun_words(self):
        if len(self.tags) == 0:
            self.get_word_character()

        noun_words = []
        for i, tag in enumerate(self.tags):
            if tag in ('g', 'j', 'n', 'nh', 'ni', 'nl', 'ns', 'nz', 'x'):
                noun_words.append(self.words[i])
        return noun_words

    def is_verb_word(self, tag):
        if tag in ('v'):
            return True
        else: 
            return False
    def get_verb_words(self):
        if len(self.tags) == 0:
            self.get_word_character()

        verb_words = []
        for i, tag in enumerate(self.tags):
            if self.is_verb_word(tag):
                verb_words.append(self.words[i])
        return verb_words

    def get_adjective_words(self):
        if len(self.tags) == 0:
            self.get_word_character()

        adjective_words = []
        for i, tag in enumerate(self.tags):
            if tag in ('a', 'b'):
                adjective_words.append(self.words[i])
        return adjective_words

    def get_real_words(self):
        if len(self.tags) == 0:
            self.get_word_character()

        function_word_tags = ['c', 'd', 'e', 'g', 'h', 'i', 'o', 'u', 'wp']
        for i, tag in enumerate(self.tags):
            if function_word_tags.count(tag) == 0:
                self.real_words.append(self.words[i])
        self.real_words = [i for i in set(self.real_words)]
