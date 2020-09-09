# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
import re
from collections import Counter

# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["a"]
filtered_paragraph = re.sub(r'[^\w]',' ',paragraph)
params = filtered_paragraph.lower()
texts = params.split()
filtered_text = []
for text in texts:
    if text not in banned:
        filtered_text.append(text)

counts = Counter(filtered_text)
print(counts.most_common(1)[0][0])

# import re
# from collections import Counter
#
#
# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         filtered_paragraph = re.sub(r'[^\w]', ' ', paragraph)
#         params = filtered_paragraph.lower()
#         texts = params.split()
#         filtered_text = []
#         for text in texts:
#             if text not in banned:
#                 filtered_text.append(text)
#
#         counts = Counter(filtered_text)
#
#         return counts.most_common(1)[0][0]