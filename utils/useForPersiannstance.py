"""
波斯语
"""
import re
from utils.useForFactory import BaseUtils


class PersianUtils(BaseUtils):
    def get_sentences(self, text):
        # based on hazm SentenceTokenizer(pypi)
        pattern = re.compile(r"([!\.\?⸮؟]+)[ \n]+")
        text = pattern.sub(r"\1\n\n", text)
        return [
            sentence.replace("\n", " ").strip()
            for sentence in text.split("\n\n")
            if sentence.strip()
        ]


if __name__ == '__main__':
    persian = PersianUtils()
    persian_text = 'جدا کردن ساده است. تقریبا البته!'
    sentences = persian.get_sentences(persian_text)
    print(sentences)
