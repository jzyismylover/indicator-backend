"""
泰语
"""
import re
from utils.useForFactory import BaseUtils

class THUtils(BaseUtils):
    def get_sentences(self, text):
        # 按换行空格切分小短句
        sentences = re.split(r" +", text, re.U)
        sentences = [s.strip() for s in sentences]
        sentences = [s for s in sentences if len(s) > 0]
        
        return sentences
