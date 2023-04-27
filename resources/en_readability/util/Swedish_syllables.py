# 瑞典语音节提取函数

# 瑞典语单词的音节划分规则也有很多种，具体取决于单词中的元音和辅音组合。以下是一些常见的规则：
#
# 一般情况下，一个单词里有几个元音音素，就有几个音节。
# 两个元音之间的一个辅音或一个半辅音应属于下一个音节。
# 以辅音音素结尾的音节叫闭音节。
# 音节划分一般要遵循“辅元优先结合”的原则。

def Swedish_syllables_count(word):
    vowels = "aeiouyåäö"
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
    if syllables == 0:
        syllables = 1
    return syllables