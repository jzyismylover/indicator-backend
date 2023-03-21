"""
葡萄语提取音节函数

1,一个单词中的每个元音字母（a, e, i, o, u）或者带重音符号或鼻音符号的元音字母（á, é, í, ó, ú, ã, õ）都是一个新的音节的开始。
2,一个单词中的每个辅音字母（b, c, d … z）都属于前面最近的元音字母所在的音节，除非它是第一个字母或者它和后面的辅音字母组成了双辅音。
双辅音是两个连续的辅音字母，它们可以在同一个发声位置发出，不需要移动舌头或嘴唇。
葡萄牙语中有以下几种双辅音：br (如 branco), cr (如 cravo), dr (如 dragão), fr (如 fruta), gr (如 grande), pr (如 prato), tr (如 trigo), vr (如 vrum); bl (如 blusa), cl (如 claro), fl (如 flor), gl (如 globo), pl (如 plano); ch (como chá); nh (como ninho); lh (como milho); rr (como carro); ss (como massa)。
双辅音属于后面最近的元音字母所在的 音节，除非它们是第一个字母。
3,如果一个单词以两个连续的相同元音字母结尾，例如 saia 或 ideia，这两个元 音不属于同一个 音节，而是分别属于前后两个 音节。
"""

def portuguese_syllable_count(word):
  vowels = "aeiouáéíóúãõàèìòùâêîôû" # 定义元音字母，包括重音和鼻音
  count = 0 # 初始化音节数为0
  i = 0 # 初始化索引为0
  while i < len(word):
    if word[i] in vowels: # 如果当前字母是元音，说明开始了一个新的音节
      count += 1 # 音节数加一
      i += 1 # 索引加一，继续遍历下一个字母
      while i < len(word) and word[i] not in vowels: # 如果当前字母不是元音，说明它是辅音，属于同一个音节
        i += 1 # 索引加一，继续遍历下一个字母
    else: # 如果当前字母不是元音，说明它是辅音，在第一个元音之前的辅音不属于任何音节，可以跳过
      i += 1 # 索引加一，继续遍历下一个字母
  return count
