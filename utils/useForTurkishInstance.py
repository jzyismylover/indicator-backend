"""
土耳其语
"""
import nltk
from utils.useForFactory import BaseUtils


class Turkishutils(BaseUtils):
    def get_sentences(self, text):
        # based on nltk pickle sentence tokenize
        tokenizer = nltk.data.load('tokenizers/punkt/turkish.pickle')
        sentences = tokenizer.tokenize(text)
        return sentences