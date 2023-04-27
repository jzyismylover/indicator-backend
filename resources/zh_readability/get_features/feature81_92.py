# -*-  coding:utf-8 -*-
from feature_bean.entity_feature import EntityFeature
from feature_bean.named_entity_feature import NamedEntityFeature
from feature_bean.nonentity_noun import NonentityNoun
from feature_bean.nonnamed_entity_noun_feature import NonnamedEntityNounFeature


def feature81_92(data_set):


    # 文章实体词
    entity_feature = EntityFeature(data_set.entity)
    data_set.features_dict["81|ED-81|"] = round(entity_feature.get_num_of_entity(), 4)
    data_set.features_dict["82|ED-82|"] = round(entity_feature.get_num_of_unique_entity(), 4)
    data_set.features_dict["83|ED-83|"] = round(entity_feature.get_percentage_entity_per_doc(data_set.all_word_pos), 4)
    data_set.features_dict["84|ED-84|"] = round(entity_feature.get_percentage_unique_entity_per_doc(data_set.all_word_pos), 4)
    data_set.features_dict["85|ED-85|"] = entity_feature.get_average_entity_per_sentence(data_set.v_lines)
    data_set.features_dict["86|ED-86|"] = entity_feature.get_average_unique_entity_per_sentence(data_set.v_lines)
    # 命名实体词
    named_entity_feature = NamedEntityFeature(data_set.named_entity)
    data_set.features_dict["87|ED-87|"] = round(named_entity_feature.get_percentage_named_entity_per_doc(data_set.all_word_pos), 4)
    data_set.features_dict["88|ED-88|"] = named_entity_feature.get_average_named_entity_per_sentence(data_set.v_lines)
    data_set.features_dict["89|ED-89|"] = round(named_entity_feature.get_percentage_named_entity_in_entity(data_set.entity), 4)
    # 非命名实体词
    nonnamed_entity_noun_feature = NonnamedEntityNounFeature(data_set.nonnamed_entity_noun)
    data_set.features_dict["90|ED-90|"] = round(nonnamed_entity_noun_feature.get_percentage_not_name_entity_noun_per_doc(data_set.all_word_pos), 4)
    data_set.features_dict["91|ED-91|"] = nonnamed_entity_noun_feature.get_average_not_name_entity_noun_per_sentence(data_set.v_lines)
    # 单句非命名实体词
    nonentity_noun_feature = NonentityNoun(data_set.nonentity_noun)
    data_set.features_dict["92|ED-92|"] = nonentity_noun_feature.get_average_not_entity_noun_per_sentence(data_set.v_lines)

    return data_set
