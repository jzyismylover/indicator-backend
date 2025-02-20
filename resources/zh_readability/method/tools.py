# -*-  coding:utf-8 -*-
import os


def unique(l):
    """
    函数作用：列表去重
    para:未去重列表
    return:已去重列表
    """
    return list(set(l))


def write_file(file_name, l):
    """
    函数作用：把列表内容写进文件名为fileName的txt文件中
    para:要写入的文件名，列表
    return:
    """
    if not os.path.exists(os.path.split(file_name)[0]):
        os.makedirs(os.path.split(file_name)[0])
    f = open(file_name, "w", encoding="utf-8")
    count = 0
    for each in l:
        each = each.replace("\n", "")
        count += 1
        if count == len(l):
            f.write(each)
        else:
            f.write(each + "\n")
    f.close()


def get_num_of_lines(path):
    """
    这个函数用于得到文章的句子数
    para:文本路径
    return:句子数目
    """
    f = open(path, "r", encoding="utf-8")
    content = f.readlines()
    num = 0
    for i in content:
        if i.replace("\n", "") != "":
            if i.split():
                num += 1
    return num


def check_file(basedir, sub_dirs, filename):
    lacks = []

    for each in sub_dirs:
        # ic文件夹下的文件后缀名不同，所以需要做特殊处理
        if each == basedir + "/ic/":
            filename = filename.replace(".txt", "_ctb_bi_both.txt")

        filepath = each + filename
        if not os.path.exists(filepath):
            lacks.append(each.replace(basedir, ""))

    return lacks


# 检查所有文件的大小是否正常，cws、pos、cp、dp、ic文档大小都应该比v1大
def check_file_size(basedir, dataset, filename):
    # file_size1 = os.path.getsize(dataset.base_dir1+filename)
    # sub_dirs1 = [dataset.base_ws_dir1, dataset.base_pos_dir1, dataset.baseneCPDir1]
    # check_result = checkFileSizeImpl(basedir, sub_dirs1, filename, file_size1)
    #
    # file_size2 = os.path.getsize(dataset.base_dir2 + filename)
    # sub_dirs2 = [dataset.base_ws_dir2, dataset.base_pos_dir2, dataset.base_cp_dir2]
    # check_result += checkFileSizeImpl(basedir, sub_dirs2, filename, file_size2)
    #
    # file_size3 = os.path.getsize(dataset.base_dir3 + filename)
    # sub_dirs3 = [dataset.base_ws_dir3, dataset.base_pos_dir3, dataset.base_cp_dir3, dataset.base_dp_dir3,
    #               dataset.base_ic_dir]
    # check_result += checkFileSizeImpl(basedir, sub_dirs3, filename, file_size3)

    file_size = os.path.getsize(dataset.base_dir + filename)
    sub_dirs = [dataset.base_ws_dir, dataset.base_pos_dir, dataset.base_cp_dir, dataset.base_dp_dir]
    check_result = check_file_size_impl(basedir, sub_dirs, filename, file_size)

    return check_result


def check_file_size_impl(basedir, sub_dirs, filename, file_size):
    lacks = []

    for each in sub_dirs:
        # 替换ic_mid和ic文件夹下文件的后缀名，方便统一处理
        if each == basedir + "/ic_mid/":
            filename = filename.replace("_ctb_bi_both.txt", ".txt.parsed")
            filename += '.txt'
        elif each == basedir + "/ic/":
            filename = filename.replace(".txt", "_ctb_bi_both")
            filename += '.txt'

        filepath = each + filename
        temp_size = os.path.getsize(filepath)
        if temp_size < file_size:
            lacks.append(each.replace(basedir, ""))

    return lacks
