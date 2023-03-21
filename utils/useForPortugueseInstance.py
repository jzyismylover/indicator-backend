"""
葡萄牙语
"""
import nltk


class PortugueseUtils:
    def get_sentences(self, text):
        # based on nltk pickle sentence tokenize
        tokenizer = nltk.data.load('tokenizers/punkt/portuguese.pickle')
        sentences = tokenizer.tokenize(text)
        return sentences
