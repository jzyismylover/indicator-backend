"""
韩语
"""
import re


class KoreanUtils:
    def get_sentences(self, text):
        pattern = re.compile("(?<=[.?!\n])\s*")
        sentences = pattern.split(text)
        if sentences[-1]:
            return sentences
        else:
            return sentences[0:-1]


if __name__ == "__main__":
    korean = KoreanUtils()
    korean_text = '안녕하세요? 만나서 반갑습니다. 저는 한국어를 배우고 있습니다.'
    sentences = korean.get_sentences(korean_text)
    print(sentences)
