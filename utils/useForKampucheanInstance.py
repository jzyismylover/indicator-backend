"""
柬埔寨语
"""
import re
from utils import BaseUtils

SENTENCE_SEPARATOR = ["◌៓", "។", "៕", "៖", "ៗ", "៘", "៙", "៚", "៛", "ៜ", "៝", "?", "!"]

class KAMUtils(BaseUtils):
    def get_sentences(self, text):
        sentences = re.split("[" + "".join(SENTENCE_SEPARATOR) + "]\s*", text)
        # 最后一项为 ""(只有一句/最后存在特殊标点)
        if sentences[-1]:
            return sentences
        return sentences[:-1]