import math
from resources.readability_indicator.util.syllables import count
from utils import ENUtils


class Readability:
    def __init__(self, text: str) -> None:
        self.handler = ENUtils()
        self.sentences = self.handler.get_sentences(text)
        self.words = self.handler.get_words(self.sentences)
        self.analyze_text()

    def analyze_text(self):
        self.char_count = self.get_char_count()
        self.syllable_count = self.get_syllables(self.words)
        self.complexwords_count = self.get_complex_word_count()

    def get_char_count(self):
        characters = 0
        for word in self.words:
            characters += len(word)

        return characters

    def get_complex_word_count(self):
        words = self.words
        sentences = self.sentences
        complex_words = 0
        found = False
        cur_word = []

        for word in words:
            cur_word.append(word)
            if self.get_syllables(cur_word) >= 3:
                if not (word[0].isupper()):
                    complex_words += 1
                else:
                    for sentence in sentences:
                        if str(sentence).startswith(word):
                            found = True
                            break
                    if found:
                        complex_words += 1
                        found = False

        cur_word.remove(word)
        return complex_words

    def get_syllables(self, words):
        syllableCount = 0
        for word in words:
            syllableCount += count(word)

        return syllableCount

    """
    可读性指标计算
    """

    def getARI(self):
        score = 0.0
        if len(self.words) > 0:
            score = (
                4.71 * (self.char_count / len(self.words))
                + 0.5 * (len(self.words) / len(self.sentences))
                - 21.43
            )

        return score

    def getARIGradeLevels(self):
        score = self.getARI()
        score = math.ceil(score)
        if score <= 1:
            return 'K'
        elif score <= 2:
            return '1 - 2'
        elif score <= 3:
            return '3'
        elif score <= 4:
            return '4'
        elif score <= 5:
            return '5'
        elif score <= 6:
            return '6'
        elif score <= 7:
            return '7'
        elif score <= 8:
            return '8'
        elif score <= 9:
            return '9'
        elif score <= 10:
            return '10'
        elif score <= 11:
            return '11'
        elif score <= 12:
            return '12'
        elif score <= 13:
            return 'college'
        else:
            return 'college_graduate'

    def getRIX(self):
        long_word_count = 0
        for word in self.words:
            if len(word) >= 6:
                long_word_count += 1

        return long_word_count / len(self.sentences)

    def getFleschReading(self):
        ASL = len(self.words) / len(self.sentences)
        ASW = self.syllable_count / len(self.words)
        FRE = 206.835 - (1.015 * ASL) - (84.6 * ASW)

        return FRE

    def getFlsechKincaidGrade(self):
        ASL = len(self.words) / len(self.sentences)
        ASW = self.syllable_count / len(self.words)
        FKG = (0.39 * ASL) + (11.8 * ASW) - 15.59

        return FKG

    def getGunningFog(self):
        ASL = len(self.words) / len(self.sentences)
        foggy_word_count = 0
        for word in self.words:
            if self.get_syllables([word]) >= 3:
                foggy_word_count += 1

        PHW = self.complexwords_count / len(self.words)
        GF = 0.4 * (ASL + PHW)

        return GF

    def getSmog(self):
        complex_words_count = self.complexwords_count
        sentences = len(self.sentences)
        SMOG = math.sqrt(complex_words_count * 30 / sentences) + 3

        return SMOG

    def getColemanLiauIndex(self):
        score = 0.0
        words_cnt = len(self.words)
        sentences_cnt = len(self.sentences)

        if words_cnt > 0.0:
            score = (
                (5.88 * (self.char_count / words_cnt))
                - (29.6 * (sentences_cnt / words_cnt))
                - 15.8
            )
        return round(score, 4)

    def getDaleChallIndex(self):
        word_cnt = len(self.words)
        sentence_cnt = len(self.sentences)
        complex_prc = self.complexwords_count / word_cnt * 100
        if complex_prc <= 5:
            return 0

        return 0.1579 * complex_prc + 0.0496 * word_cnt / sentence_cnt + 3.6365

    def getLWIndex(self):
        word_cnt = len(self.words)
        sentence_cnt = len(self.sentences)
        total = self.complexwords_count * 3 + (word_cnt - self.complexwords_count)
        index = total / sentence_cnt
        if index > 20:
            index = total / 2
        else:
            index = (total - 2) / 2

        return index
