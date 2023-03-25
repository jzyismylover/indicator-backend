"""
阿拉伯语
"""
import re
from utils.useForFactory import BaseUtils


class ArabyUtils(BaseUtils):
    def get_sentences(self, text):
        # based on pyarabic araby.py(sentence_tokenize)
        text = re.sub(u"([.,:;،؟?\n])+([\n\t\r ])+", r"\1<SPLIT>", text, re.UNICODE)
        sentences = re.split("<SPLIT>", text)
        return sentences