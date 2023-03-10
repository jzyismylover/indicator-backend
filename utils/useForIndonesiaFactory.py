import re
from utils.useForFactory import BaseUtils

class IDUtils(BaseUtils):
    def get_sentences(self, text):
        sentences = re.split(r'[?!.,]', text)
        return sentences