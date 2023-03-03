import hanlp
JA_HANLP = hanlp.load(hanlp.pretrained.mtl.NPCMJ_UD_KYOTO_TOK_POS_CON_BERT_BASE_CHAR_JA)
UNIVERSAL_HANLP = hanlp.load(
    hanlp.pretrained.mtl.UD_ONTONOTES_TOK_POS_LEM_FEA_NER_SRL_DEP_SDP_CON_MMINILMV2L6
)


from utils.useForEnglishInstance import EN_Utils
from utils.useForChineseInstance import ZH_Utils
from utils.useForJapanInstance import JP_Utils
from utils.useForIndonesiaFactory import ID_Utils
from utils.useForTagaloInstance import TA_Utils
from utils.useForFactory import Base_Utils

