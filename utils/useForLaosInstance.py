# -*- coding: utf-8 -*-

import re
from utils.useForFactory import BaseUtils

SENTENCE_SEPARATOR = [
    "ສັນຍາລັກ",
    "ຄຳຖາມ",
    "ຄຳແວ່ນຕອນຮັບຮອງ",
    "ຕົວກອງ",
    "ຕົວເລືອກ",
    "ຕົວເລືອກຂອງລັດຖະບານ",
    "?",
    "!",
    ",",
    "."
]


class LAOUtils(BaseUtils):
    def get_sentences(self, text):
        """
        句号（ສັນຍາລັກ）：表示句子的结束，和中文、英文等语言中的句号类似。
        问号（ຄຳຖາມ）：表示疑问，和中文、英文等语言中的问号类似。
        感叹号（ຄຳແວ່ນຕອນຮັບຮອງ）：表示感叹或强调，和中文、英文等语言中的感叹号类似。
        逗号（ຕົວກອງ）：表示短暂的停顿或分隔，和中文、英文等语言中的逗号类似。
        冒号（ຕົວເລືອກ）：表示引用或提示，和中文、英文等语言中的冒号类似。
        分号（ຕົວເລືອກຂອງລັດຖະບານ）：表示句子的分割或连接，和中文、英文等语言中的分号类似。
        括号（ປຸ່ມ）：表示插入的内容或说明，和中文、英文等语言中的括号类似。
        引号（ຊອກຫາ）：表示引用的内容或强调，和中文、英文等语言中的引号类似。
        """
        pattern = re.compile(r'[?!,.]|ສັນຍາລັກ|ຄຳຖາມ|ຄຳແວ່ນຕອນຮັບຮອງ|ຕົວກອງ')
        sentences = pattern.split(text)
        sentences = [s.strip() for s in sentences]
        sentences = [s for s in sentences if len(s) > 0]

        return sentences
