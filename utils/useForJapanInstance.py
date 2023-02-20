import re
import hanlp
from utils.useForFactory import Base_Utils
from hanlp.components.mtl.multi_task_learning import MultiTaskLearning

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

Hanlp: MultiTaskLearning = hanlp.load(
    hanlp.pretrained.mtl.NPCMJ_UD_KYOTO_TOK_POS_CON_BERT_BASE_CHAR_JA
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
