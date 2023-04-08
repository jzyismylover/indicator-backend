# 法语音节提取函数
# 法语单词的音节划分规则有很多种，具体取决于单词中的元音和辅音组合。以下是一些常见的规则：
#
# 两个元音相连，音节从中间分开，如 théâtre（剧院）。
# 两个元音之间的单辅音属于下一个音节，如 Noël（圣诞节）。
# 以辅音字母结尾的单词，最后一个辅音字母属于下一个音节，如 livre（书）。
# 以元音字母结尾的单词，最后一个元音字母属于最后一个音节，如 café（咖啡）。
# 以“e”结尾的单词，通常不发音，但是如果“e”前面是“é”、“è”、“ê”、“ë”、“î”、“ï”、“û”或“ü”，则“e”发音。

def French_syllables_count(word):
    vowels = "aeiouy"
    syllables = 0
    last_was_vowel = False
    for char in word:
        if char in vowels:
            if not last_was_vowel:
                syllables += 1
            last_was_vowel = True
        else:
            last_was_vowel = False
    if word.endswith("e"):
        syllables -= 1
    if word.endswith("le"):
        syllables += 1
    if syllables == 0:
        syllables = 1
    return syllables