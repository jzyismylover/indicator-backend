# 乌克兰语音节提取函数

def Ukrainian_syllables_count(word):
    vowels = "аеиоуюяєїі"
    syllables = 0
    last_was_vowel = False
    for char in word:
        if char in vowels:
            if not last_was_vowel:
                syllables += 1
            last_was_vowel = True
        else:
            last_was_vowel = False
    if word.endswith("е"):
        syllables -= 1
    if syllables == 0:
        syllables = 1
    return syllables