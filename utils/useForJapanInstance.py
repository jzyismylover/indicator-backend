import re
from utils.useForFactory import BaseUtils
from utils.constant import ZH_SPECIAL_WORDS as SYMBOLS

class JAUtils(BaseUtils):
    def __init__(self) -> None:
        super().__init__()

    def get_sentences(self, text: str):
        p = re.compile(r'(“.*?”)|(.*?[。！？…]{1,2}”?)')
        text = text.replace('\n', '')
        sentences = []
        for i in p.finditer(text):
            temp = text[i.start() : i.end()]
            if temp != '':
                sentences.append(temp.strip())

        return sentences
