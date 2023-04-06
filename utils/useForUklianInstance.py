# 乌克兰语言
import re
import six
from utils.useForFactory import BaseUtils

#
ABBRS = """
ім.
о.
вул.
просп.
бул.
пров.
пл.
г.
р.
див.
п.
с.
м.
""".strip().split()

SYMBOLS = ['.', '!', '?', '…', '»', ',']
LINE_TOKENIZER_DELIMS = re.escape('[{}]'.format(''.join(SYMBOLS)))


class UklianUtils(BaseUtils):
    # based on tokenize-uk
    def get_sentences(self, string):
        string = six.text_type(string)

        spans = []
        for match in re.finditer('[^\s]+', string):
            spans.append(match)
        spans_count = len(spans)

        rez = []
        off = 0
        flag = False

        for i in range(spans_count):
            tok = string[spans[i].start() : spans[i].end()]
            if i == spans_count - 1:
                rez.append(string[off : spans[i].end()])
            elif tok[-1] in SYMBOLS:
                if tok[-1] == ',':
                    flag = True
                else:
                    start = re.search(LINE_TOKENIZER_DELIMS, tok).start()
                    tok1 = tok[start - 1]
                    next_tok = string[spans[i + 1].start() : spans[i + 1].end()]
                    if (
                        next_tok[0].isupper()
                        and not tok1.isupper()
                        and not (tok[-1] != '.' or tok1[0] == '(' or tok in ABBRS)
                    ):
                        flag = True
            if flag is True:
                rez.append(string[off : spans[i].end() - 1]) # 删除 symbol
                off = spans[i + 1].start()
                flag = False
        return rez


if __name__ == '__main__':
    ukUtils = UklianUtils()
    text = """Результати цих досліджень опубліковано в таких колективних працях, як «Статистичні параметри 
        стилів», «Морфемна структура слова», «Структурна граматика української мови Проспект», «Частотний словник сучасної української художньої прози», «Закономірності структурної організації науково-реферативного тексту», «Морфологічний аналіз наукового тексту на ЕОМ», «Синтаксичний аналіз наукового тексту на ЕОМ», «Використання ЕОМ у лінгвістичних дослідженнях» та ін. за участю В.І.Перебийніс, 
        М.М.Пещак, М.П.Муравицької, Т.О.Грязнухіної, Н.П.Дарчук, Н.Ф.Клименко, Л.І.Комарової, В.І.Критської, 
        Т.К.Пуздирєвої, Л.В.Орлової, Л.А.Алексієнко, Т.І.Недозим."""
    sentences = ukUtils.get_sentences(text)
    print(sentences)
