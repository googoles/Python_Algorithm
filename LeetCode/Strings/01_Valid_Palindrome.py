import collections
from typing import Deque
import re

class Solution:

    # def isPalindrome(self, s: str) -> bool:
    #     texts = []
    #     for chars in s:
    #         if chars.isalnum():
    #             texts.append(chars.lower())
    #
    #     while len(texts) > 1:
    #         if texts.pop(0) != texts.pop():
    #             return False
    #
    #     return True

# # Second Method
#
#     def isPalindrome(self, s: str) -> bool:
#
#         strs: Deque = collections.deque()
#
#         for char in s:
#             if char.isalnum():
#                 strs.append(char.lower())
#
#         while len(strs) > 1:
#             if strs.popleft() != strs.pop():
#                 return False
#         return True

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # Using
        s = re.sub('[^a-z0-9]','',s)

        return s == s[::-1]


# if __name__ == "__main__:":
a = Solution()
print(a.isPalindrome("A man, a plan, a canal: Panama"))
print(a.isPalindrome("race a car"))






