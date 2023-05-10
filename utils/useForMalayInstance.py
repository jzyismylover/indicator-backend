import re
from unidecode import unidecode
from utils.useForFactory import BaseUtils

alphabets = '([A-Za-z])'
prefixes = (
    '(Mr|St|Mrs|Ms|Dr|Prof|Capt|Cpt|Lt|Mt|Puan|puan|Tuan|tuan|sir|Sir)[.]'
)
suffixes = '(Inc|Ltd|Jr|Sr|Co|Mo)'
starters = '(Mr|Mrs|Ms|Dr|He\\s|She\\s|It\\s|They\\s|Their\\s|Our\\s|We\\s|But\\s|However\\s|That\\s|This\\s|Wherever|Dia|Mereka|Tetapi|Kita|Itu|Ini|Dan|Kami|Beliau|Seri|Datuk|Dato|Datin|Tuan|Puan)'
acronyms = '([A-Z][.][A-Z][.](?:[A-Z][.])?)'
websites = '[.](com|net|org|io|gov|me|edu|my)'
another_websites = '(www|http|https)[.]'
digits = '([0-9])'
before_digits = '([Nn]o|[Nn]ombor|[Nn]umber|[Kk]e|=|al|[Pp]ukul)'
month = '([Jj]an(?:uari)?|[Ff]eb(?:ruari)?|[Mm]a(?:c)?|[Aa]pr(?:il)?|Mei|[Jj]u(?:n)?|[Jj]ula(?:i)?|[Aa]ug(?:ust)?|[Ss]ept?(?:ember)?|[Oo]kt(?:ober)?|[Nn]ov(?:ember)?|[Dd]is(?:ember)?)'
emails = r'(?:^|(?<=[^\w@.)]))(?:[\w+-](?:\.(?!\.))?)*?[\w+-]@(?:\w-?)*?\w+(?:\.(?:[a-z]{2,})){1,3}(?:$|(?=\b))'
title = r'Sdn\.|Bhd\.|Corp\.|Corporation\.|corp\.|Datuk\.|datuk\.|Datin.\|datin.\|Datik\.|datik\.|dr\.|Dr\.|DR\.|yb\.|YB\.|hj\.|HJ\.|Hj\.|ybm\.|YBM\.|Ybm\.|tyt\.|TYT\.|yab\.|YAB\.|Yab\.|ybm\.|YBM\.|Ybm\.|yabhg\.|YABHG.\|Yabhg\.|ybhg\.|YBHG\.|Ybhg\.|YBhg\.|phd\.|PhD\.'

def replace_sub(pattern, text, replace_left='.', replace_right='<prd>'):
    alls = re.findall(pattern, text)
    for a in alls:
        text = text.replace(a, a.replace(replace_left, replace_right))
    return text

# 基于 malaya/malaya/tokenizer.py/SentenceTokenizer
class MalayUtils(BaseUtils):
    def get_sentences(self, text):
      minimum_length = 5 # 超过该长度则认定为是字符

      t = '. '.join([s for s in text.split('\n') if len(s)])
      text = text + '.'
      text = unidecode(text)
      text = ' ' + text + '  '
      text = text.replace('\n', ' ')
      text = re.sub(prefixes, '\\1<prd>', text)
      text = replace_sub(emails, text)
      text = replace_sub(title, text)
      text = re.sub(websites, '<prd>\\1', text)
      text = re.sub(another_websites, '\\1<prd>', text)
      text = re.sub('[,][.]+', '<prd>', text)
      if '...' in text:
          text = text.replace('...', '<prd><prd><prd>')
      if 'Ph.D' in text:
          text = text.replace('Ph.D.', 'Ph<prd>D<prd>')
      text = re.sub('[.]\\s*[,]', '<prd>,', text)
      text = re.sub(before_digits + '\\s*[.]\\s*' + digits, '\\1<prd>\\2', text)
      text = re.sub(month + '[.]\\s*' + digits, '\\1<prd>\\2', text)
      text = re.sub('\\s' + alphabets + '[.][ ]+', ' \\1<prd> ', text)
      text = re.sub(acronyms + ' ' + starters, '\\1<stop> \\2', text)
      text = re.sub(
          alphabets + '[.]' + alphabets + '[.]' + alphabets + '[.]',
          '\\1<prd>\\2<prd>\\3<prd>',
          text,
      )
      text = re.sub(
          alphabets + '[.]' + alphabets + '[.]', '\\1<prd>\\2<prd>', text
      )
      text = re.sub(' ' + suffixes + '[.][ ]+' + starters, ' \\1<stop> \\2', text)
      text = re.sub(' ' + suffixes + '[.]', ' \\1<prd>', text)
      text = re.sub(' ' + alphabets + '[.]', ' \\1<prd>', text)
      text = re.sub(digits + '[.]' + digits, '\\1<prd>\\2', text)
      text = re.sub(digits + '[.]', '\\1<prd>', text)
      if '”' in text:
          text = text.replace('.”', '”.')
      if '"' in text:
          text = text.replace('."', '".')
      if '!' in text:
          text = text.replace('!"', '"!')
      if '?' in text:
          text = text.replace('?"', '"?')
      text = text.replace('.', '.<stop>')
      text = text.replace('?', '?<stop>')
      text = text.replace('!', '!<stop>')
      text = text.replace('<prd>', '.')
      sentences = text.split('<stop>')
      sentences = sentences[:-1]
      sentences = [s.strip() for s in sentences if len(s) > minimum_length]
      sentences = [s[:-1] if len(s) >= 2 and s[-2] in ';:-?!.' else s for s in sentences]
      return sentences

if __name__ == '__main__':
    raw_string = 'no. 1 polis bertemu dengan suspek di ladang getah. polis tembak pui pui pui bertubi tubi'
    malay_utils = MalayUtils()
    sentences = malay_utils.get_sentences(raw_string)
    print(sentences)