# 문자열 배열을 받아 애너그램 단위로 그룹핑하라

import collections

strs = ["eat","tea","tan","ate","nat","bat"]

anagram = collections.defaultdict(strs)

for words in strs:
    anagram[''.join(sorted(words))].append(words)

print(anagram.values())