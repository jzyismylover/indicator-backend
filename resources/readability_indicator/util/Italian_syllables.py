# 意大利语音节提取函数
def Italian_syllables_count(word):
    # 元音字母
    vowels = "aeiou"
    # 音节数
    count = 0
    # 遍历单词中的每个字母
    for i in range(len(word)):
        # 如果当前字母是元音字母
        if word[i] in vowels:
            # 如果当前字母是第一个字母或者前一个字母不是元音字母
            if i == 0 or word[i-1] not in vowels:
                # 音节数加一
                count += 1
    # 如果单词以e结尾，且倒数第二个字母不是元音字母，则音节数减一
    if word.endswith("e") and word[-2] not in vowels:
        count -= 1
    return count

# 测试代码
print(Italian_syllables_count("casa"))  # 2
print(Italian_syllables_count("cosa"))  # 2
print(Italian_syllables_count("cucina"))  # 3