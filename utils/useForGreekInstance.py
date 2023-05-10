import nltk
from utils.useForFactory import BaseUtils

extra_abbreviations = [
    'κτλ.',
    'κλπ.',
    'κ.ά',
    'π.χ.',
    ' λ.χ.',
    'κ.ο.κ.',
    'Δηλ.',
    'Κος.',
    'Κ.',
    'Κα.',
    'Δίδα',
    'π.Χ.',
    'B.C.',
    'μ.Χ.',
    'A.D.',
    'π.μ.',
    'a.m.',
    'μ.μ.',
    'p.m.',
    'ΥΓ.',
    'PS.',
    'σελ.',
    'p.',
]

class GreekUtils(BaseUtils):
    def get_sentences(self, text):
        tokenizer = nltk.data.load('tokenizers/punkt/greek.pickle')
        tokenizer._params.abbrev_types.update(extra_abbreviations)
        sentences = tokenizer.tokenize(text)
        return sentences
    
if __name__ == '__main__':
    raw_text = ''
    greek_utils = GreekUtils()
    sentences = greek_utils.get_sentences(raw_text)
    print(raw_text)