
## Two Pointer 방식
class Solution:

    def reverseString(self, s: list[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right] , s[left]
            left += 1
            right -= 1

    def reverseString(self, s : list[str]) -> None:

        s.reverse()




a = Solution()
print(a.reverseString(["h","e","l","l","o"]))
print(a.reverseString(["H","a","n","n","a","h"]))

