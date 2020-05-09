import re

#
# def solution(files):
#
#     print()

example = ['img12.png', 'img10.png', 'img02.png', 'img1.png', 'IMG01.GIF', 'img2.JPG']
example2 = ['F-5 Freedom Fighter', 'B-50 Superfortress', 'A-10 Thunderbolt 2','F-14 Tomcat']

# ex1_rule = re.compile('(^[\D]*)')
# a = ex1_rule.finditer(example)
def solution(files):

    temp = [re.split(r"([\d]+)",s) for s in files]
    # print(temp)

    sort = sorted(temp, key = lambda x: (x[0].lower(), int(x[1])))
    # print(sort)

    return [''.join(s) for s in sort]