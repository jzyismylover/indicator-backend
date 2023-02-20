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
    def get_sentences(self, text):
        p = re.compile(r'(“.*?”)|(.*?[。！？…]{1,2}”?)')
        text = text.replace('\n', '')
        sentences = []
        for i in p.finditer(text):
            temp = ''
            start = i.start()
            end = i.end()
            for k in range(start, end):
                temp += text[k]
            if temp != '':
                sentences.append(temp)
        return sentences

    def get_words(self, sentences, is_cut_word=True) -> list:
        words = []
        for sentence in sentences:
            if is_cut_word == False:
                words.extend(i for i in convert(sentence, 'zh-cn').strip().split(' '))
            else:
                words.extend(
                    [i for i in jieba.cut(sentence.strip()) if i not in SYMBOLS]
                )
        return words

    def get_word_frequency(self, words) -> None:
        hapax = []
        words_set = set(words)

        temp = []
        frequency = []
        for i in words_set:
            if len(i) >= 1:
                _ = re.findall('[\u4e00-\u9fa5]', i)
                if len(_) != 0:
                    temp.append(i)

        for word in temp:
            num = words.count(word)
            if num == 1:
                hapax.append(word)
            frequency.append({'word': word, 'num': num})
        frequency = sorted(
            frequency, key=lambda row: (row['num'], row['word']), reverse=True
        )

        return {
            'frequency': list(map(lambda row: row['num'], frequency)),
            'frequency_words': list(map(lambda row: row['word'], frequency)),
            'hapax': hapax,
        }

    def get_word_character(self, words):
        postagger = Postagger(POS_MODEL_PATH)
        tags = [i for i in postagger.postag(words)]
        return tags

    def get_noun_words(self, tags, words):
        noun_words = []
        for i, tag in enumerate(tags):
            if tag in ('g', 'j', 'n', 'nh', 'ni', 'nl', 'ns', 'nz', 'x'):
                noun_words.append(words[i])
        return noun_words

    def is_verb_word(self, tag):
        if tag in ('v'):
            return True
        else:
            return False

    def is_adjective_word(self, tag):
        if tag in ('a', 'b'):
            return True
        else:
            return False

    def is_real_word(self, tag):
        REAL_WORDS_TAG = ['c', 'd', 'e', 'g', 'h', 'i', 'o', 'u', 'wp', 'a', 'b']
        if tag in REAL_WORDS_TAG:
            return True
        else:
            return False
