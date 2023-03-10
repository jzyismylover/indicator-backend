"""
他加禄语(菲律宾语)
"""
import re
from utils.useForFactory import BaseUtils

class TAUtils(BaseUtils):
    def get_sentences(self, text):
        sentences = re.split('[?!.,]', text)
        print(sentences)
        return sentences
