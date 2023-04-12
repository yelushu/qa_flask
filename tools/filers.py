def number_split(num):
    """
    数字格式化
    :param num:1234
    :return:1，234
    """
    return '{:,}'.format(int(num))