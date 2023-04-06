# 僧迦罗语
import re
from typing import Tuple, Text, Dict, List


def is_a_sinhala_letter(s: Text):
    if len(s) != 1:
        return True
    # 僧伽罗语 Unicode 范围
    sinhala_lower_bound = 3456
    sinhala_upper_bound = 3583
    cp = ord(s[0])  # first letter of str
    if sinhala_lower_bound <= cp <= sinhala_upper_bound:
        return True
    return False

def contains_sinhala(s: Text):
    for c in s:
        if is_a_sinhala_letter(c):
            return True
    return False

# based on sinling sentence tokenize
class SinhalaTokenizer:
    def __init__(self):
        self.isolate_punctuations_with_spaces = False
        self.invalid_chars: List[Text] = [
            'Ê',
            '\u00a0',
            '\u2003',  # spaces
            '\ufffd',
            '\uf020',
            '\uf073',
            '\uf06c',
            '\uf190',  # unknown or invalid unicode chars
            '\u202a',
            '\u202c',
            '\u200f',  # direction control chars(for arabic, starting from right etc)
        ]
        self.line_tokenizing_chars: List[Text] = ['.', '?', '!', ':', ';', '\u2022']
        self.short_form_identifier: Text = '\u0D80'
        self.short_forms: List[Text] = [
            'ඒ.',
            'බී.',
            'සී.',
            'ඩී.',
            'ඊ.',
            'එෆ්.',
            'ජී.',
            'එච්.',
            'අයි.',
            'ජේ.',
            'කේ.',
            'එල්.',
            'එම්.',
            'එන්.',
            'ඕ.',
            'පී.',
            'කිව්.',
            'ආර්.',
            'එස්.',
            'ටී.',
            'යූ.',
            'වී.',
            'ඩබ.',
            'ඩබ්ලිව්.',
            'ඩබ්.',
            'එක්ස්.',
            'වයි.',
            'ඉසෙඩ්.',
            'පෙ.',
            'ව.',
            'රු.',
            'පා.',  # parliment
            '0.',
            '1.',
            '2.',
            '3.',
            '4.',
            '5.',
            '6.',
            '7.',
            '8.',
            '9.',
        ]

        #  init ignoring chars
        self.ignoring_chars: List[Text] = [
            '\u200c',
            '\u0160',
            '\u00ad',
            '\u0088',
            '\uf086',
            '\u200b',
            '\ufeff',
            'Á',
            'À',
            '®',
            '¡',
            'ª',
            'º',
            '¤',
            '¼',
            '¾',
            'Ó',
            'ø',
            '½',
            'ˆ',
            '',
            '¢',
            'ÿ',
            '·',
            'í',
            'Ω',
            '°',
            '×',
            'µ',
            '',
            '~',
            'ƒ',
            '',
            'ë',
            'Î',
            '‰',
            '»',
            '«',
            'à',
            '«',
            '·',
            '¨',
            '…',
            '⋆',
            '›',
            '¥',
            '⋆',
            '',
            '˝',
            '',
            '',
            '◊',
            'Ł',
            '',
            'ê',
            'Õ',
            'Ä',
            'á',
            'Ñ',
            'Í',
            '',
            'Ñ',
            'ç',
            'Æ',
            'ô',
            'Ž',
            '€',
            '§',
            'Æ',
            '÷',
            'é',
            '¯',
            'é',
            'æ',
            'î',
            'ï',
            'ä',
            'Ô',
            'õ',
            'È',
            'Ý',
            'ß',
            'õ',
            '',
            'ù',
            'å',
            'Ø',
            'Œ',
            'Ô',
            'Ü',
            '',
            'Ö',
            'Û',
            'Ï',
            'ñ',
            'ý',
            'œ',
            '¹',
            '',
            'É',
            '¯',
            'Ò',
        ]
        self.line_tokenizer_delims: Text = '[{}]'.format(re.escape(''.join(self.line_tokenizing_chars)))

    def split_sentences(self, doc, return_sinhala_only = False):
        # remove ignoring chars from document
        for ignoring_char in self.ignoring_chars:
            if ignoring_char in doc:
                doc = doc.replace(ignoring_char, '')

        # prevent short forms being splitted into sentences
        # Eg: පෙ.ව.kw
        for short_form in self.short_forms:
            representation = (
                short_form[0 : len(short_form) - 1] + self.short_form_identifier
            )
            doc = doc.replace(short_form, representation)

        sentences = []
        # split lines
        parts = re.split(r'{}'.format(self.line_tokenizer_delims), doc)
        for sentence in parts:
            sentence = sentence.replace(self.short_form_identifier, '.')
            sentence = sentence.strip()
            if contains_sinhala(
                sentence
            ):  # filter empty sentences and non-sinhala sentences
                sentences.append(sentence)
            elif not return_sinhala_only and len(sentence) != 0:
                sentences.append(sentence)
        return sentences


class SinhalaUtils:
    def get_sentences(self, text):
        sinhala_tok = SinhalaTokenizer()
        sentences = sinhala_tok.split_sentences(text)
        return sentences
