import re
# string = '(Dave)'
# print(re.sub('[^A-Za-z0-9]','',string))
# pattern = re.compile('D.A')
#
# pattern.search('DAA')
# pattern.search('D1A')
# pattern.search("d0A D1A 0111")
string = "1-----(Dave)!@   1"
# print(re.sub('[^A-Za-z0-9]', '', string))
# pattern = re.compile('D?A')
# print(pattern.search("DDA"))
# print(pattern.search("DDDDDDDDDDDDDDDDDDDDDDDDDDDDA"))
pattern = re.compile('[a-zA-Z0-9]')
print(pattern.search('abcde'))