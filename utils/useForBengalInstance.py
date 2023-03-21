"""
孟加拉语
"""

import nltk
from utils.useForFactory import BaseUtils


class BengaliUtils(BaseUtils):
    def get_sentences(self, text):
        # based for bnlp NLTKTokenizer(pypi)
        text = text.replace(".", "<dummy_bangla_token>")  # to deal with abbreviations
        text = text.replace("।", ".")
        tokens = nltk.tokenize.sent_tokenize(text)
        new_tokens = []
        for token in tokens:
            token = token.replace(".", "।")  # do operation in reverse order
            token = token.replace("<dummy_bangla_token>", ".")
            new_tokens.append(token)
        return new_tokens


if __name__ == '__main__':
    bengali = BengaliUtils()
    bengali_text = "আমি ভাত খাই। সে বাজারে যায়। তিনি কি সত্যিই ভালো মানুষ?"
    sentences = bengali.get_sentences(bengali_text)
    print(sentences)
