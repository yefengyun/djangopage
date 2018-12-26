# coding:utf-8

def string_int(arg, defualt):
    """
    字符转数字
    :param arg: 带转字符
    :param defualt: 出错默认值
    :return: 数字
    """
    try:
        page = int(arg)
    except Exception as e:
        page = defualt

    return page
