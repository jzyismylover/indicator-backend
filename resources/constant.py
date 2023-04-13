# 常量
from utils import (
    ENUtils,
    ZHUtils,
    IDUtils,
    TAUtils,
    JAUtils,
    THUtils,
    LAOUtils,
    BUUtils,
    VietnaUtils,
    KAMUtils,
    KoreanUtils,
    SpanishUtils,
    PortugueseUtils,
    BengaliUtils,
    PersianUtils,
    ArabyUtils,
    Turkishutils,
    CzechUtils,
    FrenchUtils,
    GermanyUtils,
    ItalianUtils,
    RussianUtils,
    UklianUtils,
    SwedishUtils,
)

COMMON_INDICATOR_HANDLER_MAPPING = {
    'words': 'getTotalWords',
    'dicts': 'getDictWords',
    'hapaxs': 'getHapaxWords',
    'ttr': 'getTTRValue',
    'hpoint': 'getHPoint',
    'entropy': 'getEntroyValue',
    'r1': 'getR1Value',
    'rr': 'getRRValue',
    'rrmc': 'getRRmcValue',
    'tc': 'getTCValue',
    'secondTc': 'getSecondTCValue',
    'activity': 'getAcitvityValue',
    'descriptivity': 'getDescriptivityValue',
    'l': 'getLValue',
    'curveLength': 'getCurveLengthValue',
    'lambda': 'getLambdaValue',
    'adjustModel': 'getAdjustModuleValue',
    'gini': 'getGiniValue',
    'r4': 'getR4Value',
    'writerView': 'getWriterView',
    'verbDistance': 'getVerbDistance',
}

EXCLUDE_CULMULATIVE_INDICATORS = ['writerView', 'verbDistance', 'adjustModel']
CUMYLATIVE_INDICATORS = list(filter(lambda item: item not in EXCLUDE_CULMULATIVE_INDICATORS, COMMON_INDICATOR_HANDLER_MAPPING.keys()))

READABILITY_INDICATOR_HANDLER_MAPPING = {
    'ari': 'getARI',
    'rix': 'getRIX',
    'fleschreading': 'getFleschReading',
    'fleschkincaid': 'getFlsechKincaidGrade',
    'gunning': 'getGunningFog',
    'smog': 'getSmog',
    'colemanliau': 'getColemanLiauIndex',
    'dalechall': 'getDaleChallIndex',
    'lwIndex': 'getLWIndex',
}


LANGUAGE_HANDLER_MAPPER = {
    'en': ENUtils,
    'zh': ZHUtils,
    'ja': JAUtils,
    'id': IDUtils,
    'tl': TAUtils,
    'th': THUtils,
    'lo': LAOUtils,
    'my': BUUtils,
    'vi': VietnaUtils,
    'km': KAMUtils,
    'ko': KoreanUtils,
    'es': SpanishUtils,
    'pt': PortugueseUtils,
    'bn': BengaliUtils,
    'fa': PersianUtils,
    'ar': ArabyUtils,
    'tr': Turkishutils,
    'cs': CzechUtils,
    'fr': FrenchUtils,
    'de': GermanyUtils,
    'it': ItalianUtils,
    'ru': RussianUtils,
    'sv': SwedishUtils,
    'uk': UklianUtils,
}
