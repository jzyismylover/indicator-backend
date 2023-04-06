"""
通用指标计算函数
"""
import math
from utils import (
    ENUtils,
    ZHUtils,
    BaseUtils,
    IDUtils,
    TAUtils,
    JAUtils,
    THUtils,
    LAOUtils,
    BUUtils,
    VietnaUtils,
    KAMUtils,
    KoreanUtils,
    SpanishUtils,
    PortugueseUtils,
    BengaliUtils,
    PersianUtils,
    ArabyUtils,
    Turkishutils,
    CzechUtils,
    FrenchUtils,
    GermanyUtils,
    ItalianUtils,
    RussianUtils,
    UklianUtils,
    SwedishUtils
)

LANGUAGE_HANDLER_MAPPER = {
    'en': ENUtils,
    'zh': ZHUtils,
    'ja': JAUtils,
    'id': IDUtils,
    'tl': TAUtils,
    'th': THUtils,
    'lo': LAOUtils,
    'my': BUUtils,
    'vi': VietnaUtils,
    'km': KAMUtils,
    'ko': KoreanUtils,
    'es': SpanishUtils,
    'pt': PortugueseUtils,
    'bn': BengaliUtils,
    'fa': PersianUtils,
    'ar': ArabyUtils,
    'tr': Turkishutils,
    'cs': CzechUtils,
    'fr': FrenchUtils,
    'dr': GermanyUtils,
    'it': ItalianUtils,
    'ru': RussianUtils,
    'sv': SwedishUtils,
    'uk': UklianUtils
}


class CommonIndicatorHandler:
    def __init__(self, text, lg_type) -> None:
        self.handler = self.getHandler(lg_type)
        self.sentences = self.handler.get_sentences(text)
        self.words = self.handler.get_words(self.sentences)

        FRE_ANS = self.handler.get_word_frequency(self.words)
        self.hapax = FRE_ANS['hapax']
        self.frequency = FRE_ANS['frequency']
        self.frequency_words = FRE_ANS['frequency_words']

        self.tags = []
        self.h_value = 0
        self.real_words = []

    def getHandler(self, lg_type='en') -> BaseUtils:
        return LANGUAGE_HANDLER_MAPPER[lg_type]()

    def handleTokenizen(self):
        return self.words

    def handleSpeechTagging(self):
        if self.tags:
            return self.tags
        tags = self.handler.get_word_character(self.words)
        self.tags = tags

        word_tags = []
        for i in range(len(self.words)):
            word_tags.append([self.words[i], self.tags[i]])

        return word_tags
    
    def getTotalWords(self):
        return len(self.words)
    
    def getDictWords(self):
        return len(self.frequency)

    def getHapaxWords(self):
        return len(self.hapax)

    def getTTRValue(self):
        ans = len(self.frequency) / len(self.words)
        return ans

    def getHPoint(self):
        h_value = 0
        for num, fre in enumerate(self.frequency):
            if num + 1 == fre:
                h_value = fre
                break

        if h_value == 0:
            fi = 0
            fj = 0
            ri = 0
            rj = 0
            for num, fre in enumerate(self.frequency):
                if num + 1 <= fre:
                    fi = fre
                    ri = num + 1
            for num, fre in enumerate(self.frequency):
                if num + 1 >= fre:
                    fj = fre
                    rj = num + 1
                    break
            h_value = (rj * fi - ri * fj) / (rj - ri + fi - fj)

        self.h_value = h_value
        return h_value

    def getEntroyValue(self):
        N = len(self.words)
        H = 0

        for num in self.frequency:
            rate = num / N
            H += rate * math.log2(rate)

        return -H

    def getR1Value(self):
        N = len(self.words)
        h = self.h_value
        if self.h_value == 0:
            h = self.getHPoint()
        t = 0
        for i, num in enumerate(self.frequency):
            if (i + 1) > h:
                break
            t += num

        Fh = t / N
        Fh_ = Fh - (h**2) / (2 * N)
        R1 = 1 - Fh_

        return R1

    def getRRValue(self):
        N = len(self.words)
        RR = 0
        for num in self.frequency:
            RR += (num / N) ** 2

        return RR

    def getRRmcValue(self):
        RR = self.getRRValue()
        V = len(self.frequency)
        RRmc = (1 - math.sqrt(RR)) / (1 - 1 / math.sqrt(V))

        return RRmc

    def getTCValue(self):
        Tr = 0

        h = self.h_value
        if self.h_value == 0:
            h = self.getHPoint()

        if len(self.tags) == 0:
            self.tags = self.handler.get_word_character(self.words)
        if len(self.real_words) == 0:
            self.real_words = self.handler.get_real_words(self.tags, self.words)

        try:
            for i, fr in enumerate(self.frequency):
                if i + 1 > h:
                    break
                word = self.frequency_words[i]
                if self.real_words.count(word) != 0:
                    Tr += ((h - (i + 1)) * fr) / (h * (h - 1) * self.frequency[0])
        except:
            Tr = 0  

        return Tr * 2

    def getSecondTCValue(self):
        Tr = 0
        h = self.h_value
        f = self.frequency
        if self.h_value == 0:
            h = self.getHPoint()
        if len(self.tags) == 0:
            self.tags = self.handler.get_word_character(self.words)
        if len(self.real_words) == 0:
            self.real_words = self.handler.get_real_words(self.tags, self.words)

        try:
            for i in range(math.ceil(h), math.floor(2 * h) + 1):
                word = self.frequency_words[i - 1]
                if self.real_words.count(word) != 0:
                    fr = f[i - 1]
                    Tr += ((h - i) * fr) / (h * (h - 1) * f[0])
        except:
            Tr = 0

        return Tr * 2

    def getAcitvityValue(self):
        if len(self.tags) == 0:
            self.tags = self.handler.get_word_character(self.words)
        verb_words = self.handler.get_verb_words(self.tags, self.words)
        adjective_words = self.handler.get_adjective_words(self.tags, self.words)
        verb_words_len = len(verb_words)
        adjective_words_len = len(adjective_words)

        if verb_words_len == 0:
            return 0
        elif adjective_words_len == 0:
            return 1

        return verb_words_len / (verb_words_len + adjective_words_len)

    def getDescriptivityValue(self):
        if len(self.tags) == 0:
            self.tags = self.handler.get_word_character(self.words)
        verb_words = self.handler.get_verb_words(self.tags, self.words)
        adjective_words = self.handler.get_adjective_words(self.tags, self.words)
        verb_words_len = len(verb_words)
        adjective_words_len = len(adjective_words)

        if verb_words_len == 0:
            return 1
        elif adjective_words_len == 0:
            return 0

        return adjective_words_len / (verb_words_len + adjective_words_len)

    def getLValue(self):
        L = 0
        f = self.frequency
        for i in range(0, len(f) - 1):
            distance = (f[i] - f[i + 1]) ** 2
            L += math.sqrt(distance + 1)

        return L

    def getCurveLengthValue(self):
        f = self.frequency
        LR = 0
        L = 0
        if self.h_value == 0:
            self.getHPoint()

        for i in range(0, len(f) - 1):
            distance = (f[i] - f[i + 1]) ** 2
            if i + 1 < self.h_value:
                LR += math.sqrt(distance + 1)
            L += math.sqrt(distance + 1)

        R = 1 - LR / L

        return R

    def getLambdaValue(self):
        L = self.getLValue()
        N = len(self.words)
        lambda_v = (L * math.log10(N)) / N

        return lambda_v

    def getAdjustModuleValue(self):
        h = self.h_value
        if h == 0:
            h = self.getHPoint()

        f = self.frequency
        V = len(self.frequency)
        N = len(self.words)
        f1 = f[0]
        M = math.sqrt((f1 / h) ** 2 + (V / h) ** 2)

        A = M / math.log10(N)

        return A

    def getGiniValue(self):
        V = len(self.frequency)
        N = len(self.words)
        c1 = 0
        for i, num in enumerate(self.frequency):
            c1 += (i + 1) * num
        c1 = 2 * c1 / N
        G = (V + 1 - c1) / V

        return G

    def getR4Value(self):
        G = self.getGiniValue()
        R4 = 1 - G
        return R4

    def getHapaxValue(self):
        N = len(self.words)
        rate = len(self.hapax) / N

        return rate

    def getWriterView(self):
        f = self.frequency
        V = len(self.frequency)
        f1 = f[0]
        h = self.h_value
        if h == 0:
            h = self.getHPoint()

        r1 = h - 1
        r2 = f1 - h
        r3 = h - 1
        r4 = V - h

        t1 = -(r1 * r2 + r3 * r4)
        t2 = math.sqrt(r1**2 + r2**2)
        t3 = math.sqrt(r3**2 + r4**2)

        if t2 == 0 or t3 == 0:
            return 0

        cosa = t1 / (t2 * t3)

        return cosa

    def getVerbDistance(self):
        verb_V = 0
        verb_idx_list = []
        if len(self.tags) == 0:
            self.tags = self.handler.get_word_character(self.words)

        for i, tag in enumerate(self.tags):
            if self.handler.is_verb_word(tag):
                verb_idx_list.append(i)

        for i in range(0, len(verb_idx_list) - 1):
            verb_V += verb_idx_list[i + 1] - verb_idx_list[i]

        if len(verb_idx_list) == 0:
            return 0

        verb_V = verb_V / (len(verb_idx_list) - 1)

        return verb_V

    def getZipf(self):
        ll = 0
        tword = self.frequency[0]
        zipf = dict()
        avg = 0
        for i, num in enumerate(self.frequency):
            if num == tword:
                avg += i + 1
            else:
                zipf[str(tword)] = tword * avg / (i - ll)
                ll = i
                avg = i + 1
                tword = num
                if tword == 1:
                    break

        return zipf
