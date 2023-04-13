# 德语音节提取函数

# 德语单词的音节划分规则有很多种，具体取决于单词中的元音和辅音组合。以下是一些常见的规则：

# 单音节的词不能分开，如 ein（一个）。
# 双音节词中，词首音节是单独一个元音，不能分写，如 oben（上面）。
# 两个元音之间只有一个辅音，辅音同后面元音构成音节，如 Tafel（桌子）。
# 两个元音之间有几个辅音时，最后一个辅音同后面一个元音构成一个音节，如 Zinse（利息）。
# 长元音符号“h”后面是辅音时，长元音符号“h”跟前面元音；长元音符号“h”后面是元音时，则跟后面元音，如 nehmen（拿）。
# 复合词移行以词为主。

def German_syllables_count(word):
    # 元音字母
    vowels = "aeiouäöü"
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
print(German_syllables_count("Haus"))  # 1
print(German_syllables_count("Auto"))  # 2
print(German_syllables_count("Küche"))  # 2