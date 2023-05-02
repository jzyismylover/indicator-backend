from flask_restful import Resource, request
from utils.useForChineseInstance import ZHUtils
from utils.json_response import make_success_response
from resources.zh_readability.read_write_txt.acquire_pos import acquire_pos
from resources.zh_readability.data_loader import DataSet
from resources.zh_readability.get_features.feature1_23 import feature1_23
from resources.zh_readability.get_features.feature24_63 import feature24_63
from resources.zh_readability.get_features.feature64_80 import feature64_80
from resources.zh_readability.get_features.feature81_92 import feature81_92
from resources.zh_readability.get_features.feature93_102 import feature93_102


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


# 基于18个显著特征的可读性测度线性回归模型
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
        data_set = feature64_80(data_set)
        data_set = feature81_92(data_set)
        data_set = feature93_102(data_set)
        feature_dir = data_set.features_dict

        _readability = (
            -7.9291
            + 1.2441 * feature_dir['86|ED-86|']
            + 0.0408 * feature_dir['71|P-71|']
            + 1.7763 * feature_dir['73|CL-73|']
            + 0.7466 * feature_dir['74|CL-74|']
            - 29.524 * feature_dir['31|F-31|']
            + 0.1073 * feature_dir['30|F-30|']
            + 3.7729 * feature_dir['41|N-41|']
            - 0.5338 * feature_dir['43|N-43|']
            - 0.0677 * feature_dir['94|CO-94|']
            + 36.4785 * feature_dir['95|CO-95|']
            + 1.533 * feature_dir['96|CO-96|']
            - 7.7032 * feature_dir['8|WC-8|']
            + 6.2422 * feature_dir['9|WC-9|']
            - 5.9512 * feature_dir['13|WC-13|']
            - 0.3011 * feature_dir['18|SC-18|']
            - 0.3069 * feature_dir['19|SC-19|']
            + 0.3473 * feature_dir['20|SC-20|']
            + 1.4679 * feature_dir['7|CC-7|']
        )

        return make_success_response(data={'level': _readability})


# 基于22个显著特征的可读性测度线性回归模型
class Feature22Main:
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
        data_set = feature64_80(data_set)
        data_set = feature81_92(data_set)
        data_set = feature93_102(data_set)
        feature_dir = data_set.feature_dir

        _readability = (
            -8.9283
            + 1.1216 * feature_dir['86|ED-86|']
            - 0.0083 * feature_dir['78|S-78|']
            + 0.0531 * feature_dir['71|P-71|']
            + 1.6339 * feature_dir['73|CL-73|']
            + 0.7545 * feature_dir['74|CL-74|']
            - 2.0576 * feature_dir['24|A-24|']
            - 27.6036 * feature_dir['31|F-31|']
            + 0.0826 * feature_dir['30|F-30|']
            + 3.8044 * feature_dir['41|N-41|']
            - 0.5288 * feature_dir['43|N-43|']
            - 0.0672 * feature_dir['94|CO-94|']
            + 37.7010 * feature_dir['95|CO-95|']
            + 1.6960 * feature_dir['96|CO-96|']
            - 7.2546 * feature_dir['8|WC-8|']
            + 5.8566 * feature_dir['9|WC-9|']
            - 6.1643 * feature_dir['13|WC-13|']
            - 0.2996 * feature_dir['18|SC-18|']
            - 0.3681 * feature_dir['19|SC-19|']
            + 0.3550 * feature_dir['20|SC-20|']
            - 0.0024 * feature_dir['2|D-22|']
            + 0.0023 * feature_dir['23|D-23|']
            + 1.611 * feature_dir['7|CC-7|']
        )

        return make_success_response(data={'level': _readability})
