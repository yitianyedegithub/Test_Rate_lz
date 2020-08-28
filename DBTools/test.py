import time
def test(link_word, **kwargs):
    link = ''
    for i in kwargs:
        if isinstance(kwargs[i], str):
            link += i + " = '" + kwargs[i] + "' " + link_word + " "
        else:
            link += i + " = " + str(kwargs[i]) + " " + link_word + " "
    # 将最后一个多余的连接符以及前后的空格去掉
    link = link[:-len(link_word) - 2]
    print(link)
    if link_word != ',':
        link = ' where ' + link
    return link


def test2(**kwargs):
    link = 'jddjjddjdj' + test('and', **kwargs)
    print(link)


if __name__ == '__main__':
    # test2(a="'1111'", c="'22222'")
    # test2(a=1, c=2)
    # test2(a='a',b='b')
    # test2(a='a', b=2)
    #print(type(1.256), type(1), str(1.25365))
    print(time.time(),time.strftime('%Y-%m-%d %H:%M:%S'),type(time.time()),type(time.strftime('%Y-%m-%d %H:%M:%S')))
