import re
from hanlp_restful import HanLPClient
from utils.useForFactory import Base_Utils

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


HanLP = HanLPClient(
    url='https://www.hanlp.com/api',
    auth='MTkxOUBiYnMuaGFubHAuY29tOjdGd0I3STZPQ0xoU2lvdHo=',
    language='mul',
)
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
        tags = []
        for sentence in sentences:
            words.extend([i for i in HanLP.parse(sentence)['tok'] if i not in SYMBOLS])
            tags.extend([i for i in HanLP.parse(sentence)['pos'] if i not in SYMBOLS])

        return words

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

    def get_word_character(self, words):
        return self.tags

    def get_adjective_words(self, tags, words):
        adjective_words = []
        for i, tag in enumerate(tags):
            if self.is_adjective_words(tag):
                adjective_words.append(words[i])

        return adjective_words

    def get_verb_words(self, tags, words):
        verb_words = []
        for i, tag in enumerate(tags):
            if self.is_verb_word(tag):
                verb_words.append(words[i])

        return verb_words

    def get_real_words(self, tags, words):
        real_words = []
        for i, tag in enumerate(tags):
            if self.is_real_word(tag):
                real_words.append(words[i])

        return [i for i in set(real_words)]

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
