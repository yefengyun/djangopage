# coding=utf-8
from django.utils.safestring import mark_safe

def culpage(current_page, total, per_item):
    """
    计算开始，结束，和总页数
    :param current_page: 当前页
    :param total: 记录总数
    :param per_item: 每页数量
    :return: start开始位置，end结束位置，page_num[0]总页数
    """
    start = per_item * (current_page - 1)
    end = per_item * current_page
    page_num = divmod(total, per_item)
    page_num = list(page_num)

    if page_num[1] != 0:
        page_num[0] += 1

    if current_page > page_num[0]:
        start = 0
        end = per_item
    elif current_page == page_num[0]:
        end = start + page_num[1]

    return start, end, page_num[0]


def gen_html(currenpage, allpage, url, per_item):
    """
    生成html
    :param currenpage: 当前页
    :param allpage: 所有页
    :param url:网址
    :param per_item: 显示页数
    :return: html 分页字符串
    """
    per_sum = 2 * per_item + 1
    html = []
    html.append("<a href='{}/{}/'>首页</a>".format(url, 1))
    if currenpage == 1:
        html.append("<a href='{}/{}/'>上一页</a>".format(url, currenpage))
    else:
        html.append("<a href='{}/{}/'>上一页</a>".format(url, currenpage - 1))

    if per_sum > allpage:
        for i in range(1, per_sum + 1):
            if i == currenpage:
                html.append("<a style='color:red;' href='{}/{}/'>第{}页</a>".format(url, i, i))
            else:
                html.append("<a href='{}/{}/'>第{}页</a>".format(url, i, i))
    else:
        if currenpage < per_item + 1:
            for i in range(1, per_sum + 1):
                if i == currenpage:
                    html.append("<a style='color:red;' href='{}/{}/'>第{}页</a>".format(url, i, i))
                else:
                    html.append("<a  href='{}/{}/'>第{}页</a>".format(url, i, i))

        elif currenpage > allpage - per_item:
            for i in range(allpage - per_sum + 1, allpage + 1):
                if i == currenpage:
                    html.append("<a style='color:red;' href='{}/{}/'>第{}页</a>".format(url, i, i))
                else:
                    html.append("<a  href='{}/{}/'>第{}页</a>".format(url, i, i))

        else:
            for i in range(currenpage - per_item, currenpage + per_item + 1):
                if i == currenpage:
                    html.append("<a style='color:red;' href='{}/{}/'>第{}页</a>".format(url, i, i))
                else:
                    html.append("<a  href='{}/{}/'>第{}页</a>".format(url, i, i))

    if currenpage == allpage:
        html.append("<a href='{}/{}/'>下一页</a>".format(url, currenpage))
    else:
        html.append("<a href='{}/{}/'>下一页</a>".format(url, currenpage + 1))

    html.append("<a href='{}/{}/'>尾页</a>".format(url, allpage))
    return mark_safe(''.join(html))
