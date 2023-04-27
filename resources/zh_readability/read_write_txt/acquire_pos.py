# -*-  coding:utf-8 -*-


def acquire_pos(dataset):
    lfm = dataset.lfm

    # 根据各类标签获得各类词
    v1 = lfm.get_feature("v")  # 动词
    m1 = lfm.get_feature("m")  # 数词
    a1 = lfm.get_feature("a")  # 形容词
    d1 = lfm.get_feature("d")  # 副词
    j1 = lfm.get_feature("j")  # 缩略词
    q1 = lfm.get_feature("q")  # 量词
    r1 = lfm.get_feature("r")  # 代词
    c1 = lfm.get_feature("c")  # 连词
    b1 = lfm.get_feature("b")  # 区别词
    i1 = lfm.get_feature("i")  # 习语或者成语
    n1 = lfm.get_feature("n ")  # 普通名词

    all_noun_pattern = ["nl", "ni", "ns", "nt", "nz", "n ", "nd", "nh"]  # 所有的名词
    all_noun1 = lfm.get_multi_feature(all_noun_pattern)

    content_word_pattern = ["v", "m", "a", "d", "i", "j", "q", "r", "b", "z", "ws", "g"]
    content_word1 = all_noun1 + lfm.get_multi_feature(content_word_pattern)  # 实词

    function_pattern = ["c", "e", "h", "o", "k", "u", "x"]
    function_word1 = lfm.get_multi_feature(function_pattern)  # 功能词

    entity_pattern = ["ni", "ns", "nh", "nt", "nz"]
    entity1 = lfm.get_multi_feature(entity_pattern)  # 实体词

    named_entity_pattern = ["ni", "ns", "nh"]
    named_entity1 = lfm.get_multi_feature(named_entity_pattern)  # 命名实体

    not_name_entity_noun_pattern = ["n ", "nz", "nl", "nd", "nt"]
    not_name_entity_noun1 = lfm.get_multi_feature(not_name_entity_noun_pattern)  # 非命名实体名词

    not_e_noun_pattern = ["n ", "nl", "nd"]
    not_e_noun1 = lfm.get_multi_feature(not_e_noun_pattern)  # 非实体词


    return (v1, m1, a1, d1, j1, q1, r1, c1, b1, i1, n1, all_noun1, content_word1, function_word1,
            entity1, named_entity1, not_name_entity_noun1, not_e_noun1)
