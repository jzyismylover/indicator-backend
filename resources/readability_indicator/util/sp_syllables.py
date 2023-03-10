"""
西班牙音节提取函数

西班牙语有强元音（a, e, o）和弱元音（i, u），它们会影响音节的划分

1,大多数音节以元音结尾。
2,两个元音之间的辅音和第二个元音组成一个音节。
3,两个相邻的辅音分属两个不同的音节。
4,西班牙语中有强元音和弱元音。一个强元音和一个或多个弱元音可以组成一个音节。两个相邻的弱元音组成一个双元音。
5,一些辅音不会分开，例如ch, ll, rr等。
6,如果三个辅音连在一起，通常第一个辅音属于前一个音节，后两个辅音属于后一个音节。
7,前缀是单独的一个音节。
"""

def spanish_syllable_count(word):
  vowels = "aeiou" # 定义元音字母
  strong_vowels = "aeo" # 定义强元音字母
  weak_vowels = "iu" # 定义弱元音字母
  count = 0 # 初始化音节数为0
  i = 0 # 初始化索引为0
  while i < len(word):
    if word[i] in vowels: # 如果当前字母是元音，说明开始了一个新的音节
      count += 1 # 音节数加一
      i += 1 # 索引加一，继续遍历下一个字母
      if i < len(word) and word[i-1] in weak_vowels and word[i] in weak_vowels: # 如果当前字母和前一个字母都是弱元音，说明它们组成了一个双元音，属于同一个音节
        i += 1 # 索引加一，跳过第二个弱元音，继续遍历下一个字母
      while i < len(word) and word[i] not in vowels: # 如果当前字母不是元音，说明它是辅音，属于同一个音节
        i += 1 # 索引加一，继续遍历下一个字母
    else: # 如果当前字母不是元音，说明它是辅音，在第一个元音之前的辅音不属于任何音节，可以跳过
      i += 1 # 索引加一，继续遍历下一个字母
  return count # 返回最后的音节数


print(spanish_syllable_count("paralelepípedo"))