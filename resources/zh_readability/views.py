from flask_restful import Resource, request
from utils.useForChineseInstance import ZHUtils
from resources.zh_readability.read_write_txt.acquire_pos import acquire_pos
from resources.zh_readability.data_loader import DataSet
from resources.zh_readability.get_features.feature1_23 import feature1_23
from resources.zh_readability.get_features.feature24_63 import feature24_63
# from resources.zh_readability.get_features.feature64_80 import feature64_80
# from resources.zh_readability.get_features.feature81_92 import feature81_92
# from resources.zh_readability.get_features.feature93_102 import feature93_102


def deal_pos(data_set):

    (
        data_set.v,
        data_set.m,
        data_set.a,
        data_set.d,
        data_set.j,
        data_set.q,
        data_set.r,
        data_set.c,
        data_set.b,
        data_set.i,
        data_set.n,
        data_set.all_noun,
        data_set.content_word,
        data_set.function_word,
        data_set.entity,
        data_set.named_entity,
        data_set.nonnamed_entity_noun,
        data_set.nonentity_noun,
    ) = acquire_pos(data_set)


# 处理 18 features
class Feature18Main(Resource):
    def post(self):
        raw_text = request.form['raw_text']
        zh_utils = ZHUtils()
        sentences = zh_utils.get_sentences(raw_text)
        words = zh_utils.get_words(sentences)
        tags = zh_utils.get_word_character(words)
        data_set = DataSet(raw_text, sentences, words, tags)
        deal_pos(data_set)

        data_set = feature1_23(data_set)
        data_set = feature24_63(data_set)
        # data_set = feature64_80(data_set)
        # data_set = feature81_92(data_set)
        # data_set = feature93_102(data_set)

        return data_set.features_dict


# 处理 22 features
class Feature22Main:
    pass
