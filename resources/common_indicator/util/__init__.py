"""
通用指标计算函数
"""
import math


def getTTRValue(*, frequency, words):
    ans = len(frequency) / len(words)
    return ans


def getHPoint(*, frequency):
    h_value = 0
    for num, fre in enumerate(frequency):
        if num + 1 == fre:
            h_value = fre
            break

    if h_value == 0:
        fi = 0
        fj = 0
        ri = 0
        rj = 0
        for num, fre in enumerate(frequency):
            if num + 1 <= fre:
                fi = fre
                ri = num + 1
        for num, fre in enumerate(frequency):
            if num + 1 >= fre:
                fj = fre
                rj = num + 1
                break
        h_value = (rj * fi - ri * fj) / (rj - ri + fi - fj)

    return h_value


def getEntroyValue(*, frequency, words):
    N = len(words)
    H = 0

    for num in frequency:
        rate = num / N
        H += rate * math.log2(rate)

    return H


def getR1Value(*, frequency, words, h_value):
    N = len(words)
    h = h_value
    t = 0
    for i, num in enumerate(frequency):
        if (i + 1) > h:
            break
        t += num

    Fh = t / N
    h = h_value
    Fh_ = Fh - (h**2) / (2 * N)
    R1 = 1 - Fh_

    return R1

def getRRValue(*, words, frequency):
    N = len(words)
    RR = 0
    for num in frequency:
        RR += (num / N) ** 2

    return RR


def getRRmcValue(*, frequency, words, RR):
    if RR is None:
      RR = getRRValue(frequency=frequency, words=words)
    V = len(frequency)
    RRmc = (1 - math.sqrt(RR)) / (1 - 1 / math.sqrt(V))

    return RRmc


def getTCValue(*, frequency, h_value, frequency_words, real_words):
    Tr = 0
    h = h_value
    for i, fr in enumerate(frequency):
        if i + 1 > h:
            break
        word = frequency_words[i]
        if real_words.count(word) != 0:
            Tr += ((h - (i + 1)) * fr) / (h * (h - 1) * frequency[0])

    return Tr * 2


def getSecondTCValue(*, frequency, h_value, frequency_words, real_words):
    Tr = 0
    h = h_value
    f = frequency
    for i in range(math.ceil(h), math.floor(2 * h) + 1):
        word = frequency_words[i - 1]
        if real_words.count(word) != 0:
            fr = f[i - 1]
            Tr += ((h - i) * fr) / (h * (h - 1) * f[0])

    return Tr * 2


def getAcitvityValue(*, verb_words, adjective_words):
    verb_words_len = len(verb_words)
    adjective_words_len = len(adjective_words)
    activity = verb_words_len / (verb_words_len + adjective_words_len)

    return activity


def getDescriptivityValue(*, verb_words, adjective_words):
    verb_words_len = len(verb_words)
    adjective_words_len = len(adjective_words)
    descriptivity = adjective_words_len / (verb_words_len + adjective_words_len)

    return descriptivity


def getLValue(*, frequency):
    L = 0
    for i in range(0, len(frequency) - 1):
        distance = (frequency[i] - frequency[i + 1]) ** 2
        L += math.sqrt(distance + 1)

    return L


def getCurveLengthValue(*, frequency, h_value):
    f = frequency
    LR = 0
    L = 0
    for i in range(0, len(f) - 1):
        distance = (f[i] - f[i + 1]) ** 2
        if i + 1 < h_value:
            LR += math.sqrt(distance + 1)
        L += math.sqrt(distance + 1)

    R = 1 - LR / L

    return R


def getLambdaValue(*, frequency, words, L):
    if L is None:
      L = getLValue(frequency=frequency)
    N = len(words)
    lambda_v = (L * math.log10(N)) / N

    return lambda_v


def getGiniValue(*, frequency, words):
    V = len(frequency)
    N = len(words)
    c1 = 0
    for i, num in enumerate(frequency):
        c1 += (i + 1) * num
    c1 = 2 * c1 / N
    G = (V + 1 - c1) / V

    return G


def getR4Value(*, frequency, words):
    G = getGiniValue(frequency=frequency, words=words)
    R4 = 1 - G
    return R4


def getHapaxValue(*, words, hapax):
    N = len(words)
    rate = len(hapax) / N

    return rate


def getWriterView(*, frequency, h_value):
    h = h_value
    f = frequency
    V = len(frequency)
    f1 = f[0]

    r1 = h - 1
    r2 = f1 - h
    r3 = h - 1
    r4 = V - h

    t1 = -(r1 * r2 + r3 * r4)
    t2 = math.sqrt(r1**2 + r2**2)
    t3 = math.sqrt(r3**2 + r4**2)

    cosa = t1 / (t2 * t3)

    return cosa


def getVerbDistance(*, tags, is_verb_word):
    verb_V = 0
    verb_idx_list = []
    for i, tag in enumerate(tags):
        if is_verb_word(tag):
            verb_idx_list.append(i)

    for i in range(0, len(verb_idx_list) - 1):
        verb_V += verb_idx_list[i + 1] - verb_idx_list[i]
    verb_V = verb_V / (len(verb_idx_list) - 1)

    return verb_V


def getZipf(*, frequency, frequency_words):
    print(frequency, frequency_words)
    ll = 0
    tword = frequency[0]
    zipf = dict()
    avg = 0
    for i, num in enumerate(frequency):
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
