import re
from utils.useForFactory import BaseUtils

# based on separatrice
# but a splitter "razdel" may be must better
# but now need to avoid adding some extra package into project
# to keep out project dependence clean
class Separatrice:
    def __init__(self) -> None:
        self.alphabets = "([А-Яа-я])"
        self.acronyms = "([А-Яа-я][.][А-Яа-я][.](?:[А-Яа-я][.])?)"
        self.prefixes = "(Mr|Mrs|Ms|акад|чл.-кор|канд|доц|проф|ст|мл|ст. науч|мл. науч|рук|тыс|млрд|млн|кг|км|м|мин|сек|ч|мл|нед|мес|см|сут|проц)[.]"
        self.starters = "(Mr|Mrs|Ms|Dr)"
        self.websites = "[.](com|net|org|io|gov|ru|xyz|ру)"
        self.suffixes = "(Inc|Ltd|Jr|Sr|Co)"
        self.conjs = '(, что|чтобы|, когда| несмотря на то что| вопреки|, а также| либо| но| зато|, а| тогда|, а то| так что| чтоб| затем| дабы| коль скоро| если бы| если б| коль скоро| тогда как| как только| подобно тому как| будто бы)'
        self.introductory = '(вот где где,|не-а,|и ещё|во-первых|во-вторых|конечно|несомненно|без всякого сомнения|очевидно|безусловно|разумеется|само собой разумеется|бесспорно|действительно,|наверное|возможно|верно|вероятно|по всей вероятности|может быть|быть может|должно быть|кажется|казалось бы|видимо|по-видимому|пожалуйста|в самом деле|подлинно|правда|не правда ли|в сущности|по существу|по сути|надо полагать|к счастью|к несчастью|по счастью|по несчастью|к радости|к огорчению|к прискорбию|к досаде|к сожалению|к удивлению|к изумлению|к ужасу|к стыду|говорят|сообщают|передают|по словам|по сообщению|по сведениям|по мнению|по-моему|по-твоему|по-нашему|по-вашему|на мой взгляд|по слухам|по преданию|помнится|слышно|дескать|говорят|сообщают|передают|по словам|по сообщению|по сведениям|по мнению|по-моему|по-твоему|по-нашему|по-вашему|на мой взгляд|по слухам|по преданию|помнится|слышно|дескать|словом|одним словом|иными словами|другими словами|иначе говоря|коротко говоря|попросту сказать|мягко выражаясь|если можно так сказать|если можно так выразиться|с позволения сказать|лучше сказать|так сказать|что называется и другие; слова собственно|вообще|вернее|точнее|скорее |видишь ли|видите ли|понимаешь ли|понимаете ли|знаешь ли|знаете ли|пойми|поймите|поверьте|послушайте|согласитесь|вообразите|представьте себе|извините|простите|веришь ли|верите ли|пожалуйста|спасибо|привет|пасиб|прив|здравствуйте|доброго дня|доброго вечера)'

    # split text into sentences
    def into_sents(self, text):
        flag = False
        if text[-1] != '.' and text[-1] != '!' and text[-1] != '?':
            text += '.'
            flag = True
        text = " " + text + "  "
        text = text.replace("\n", " ")
        text = re.sub(' ' + self.prefixes, "\\1<prd>", text)
        text = re.sub(self.websites, "<prd>\\1", text)
        if "Ph.D" in text:
            text = text.replace("Ph.D.", "Ph<prd>D<prd>")
        text = re.sub("\s" + self.alphabets + "[.] ", " \\1<prd> ", text)
        text = re.sub(self.acronyms + " " + self.starters, "\\1<stop> \\2", text)
        text = re.sub(
            self.alphabets + "[.]" + self.alphabets + "[.]" + self.alphabets + "[.]",
            "\\1<prd>\\2<prd>\\3<prd>",
            text,
        )
        text = re.sub(
            self.alphabets + "[.]" + self.alphabets + "[.]", "\\1<prd>\\2<prd>", text
        )
        text = re.sub(
            " " + self.suffixes + "[.] " + self.starters, " \\1<stop> \\2", text
        )
        text = re.sub(" " + self.suffixes + "[.]", " \\1<prd>", text)
        text = re.sub(" " + self.alphabets + "[.]", " \\1<prd>", text)
        if "”" in text:
            text = text.replace(".”", "”.")
        if "\"" in text:
            text = text.replace(".\"", "\".")
        if "!" in text:
            text = text.replace("!\"", "\"!")
        if "?" in text:
            text = text.replace("?\"", "\"?")
        text = text.replace(". ", ".<stop>")
        text = text.replace("? ", "?<stop>")
        text = text.replace("! ", "!<stop>")
        text = text.replace("<prd>", ".")
        sentences = text.split("<stop>")
        sentences = sentences[:-1]
        if flag == True:
            sentences[-1] = sentences[-1][:-1]
        sentences = [s.strip() for s in sentences if s not in ["!", "?", '.']]
        return sentences


class RussianUtils(BaseUtils):
    def get_sentences(self, text):
        split_r = Separatrice()
        sentences = split_r.into_sents(text)
        return sentences