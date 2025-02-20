# 对应语种文本处理实例
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
    GreekUtils,
    HebrewUtils,
    HindiUtils,
    MalayUtils,
    PolishUtils,
    SerbianUtils,
    UrduUtils
)

# 通用指标名与对应处理方法映射
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

# 不可增量指标
EXCLUDE_CULMULATIVE_INDICATORS = ['writerView', 'verbDistance', 'adjustModel']
CUMYLATIVE_INDICATORS = list(filter(lambda item: item not in EXCLUDE_CULMULATIVE_INDICATORS, COMMON_INDICATOR_HANDLER_MAPPING.keys()))

# 英文可读性指标名与方法的映射
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
    'en': ENUtils, # 英语
    'zh': ZHUtils, # 汉语
    'ja': JAUtils, # 日语
    'id': IDUtils, # 印尼语
    'tl': TAUtils, # 菲律宾语
    'th': THUtils, # 泰语
    'lo': LAOUtils, # 老挝语
    'my': BUUtils, # 缅甸语
    'vi': VietnaUtils, # 越南语
    'km': KAMUtils, # 高棉语
    'ko': KoreanUtils, # 韩语
    'es': SpanishUtils, # 西班牙语
    'pt': PortugueseUtils, # 葡萄牙语
    'bn': BengaliUtils, # 孟加拉语
    'fa': PersianUtils, # 波斯语
    'ar': ArabyUtils, # 阿拉伯语
    'tr': Turkishutils, # 土耳其语
    'cs': CzechUtils, # 捷克语
    'fr': FrenchUtils, # 法语
    'de': GermanyUtils, # 德国语
    'it': ItalianUtils, # 意大利语
    'ru': RussianUtils, # 俄罗斯语
    'sv': SwedishUtils, # 瑞典语
    'uk': UklianUtils, # 乌克兰语
    'el': GreekUtils, # 希腊语
    'he': HebrewUtils, # 希伯来语
    'hi': HindiUtils, # 印地语
    'ms': MalayUtils, # 马来语
    'pl': PolishUtils, # 波兰语
    'sr': SerbianUtils, # 塞尔维亚语
    'ur': UrduUtils # 乌尔都语
}
