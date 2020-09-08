class Solution:
    def isPalindrome(self, s: str) -> bool:
        texts = []
        for chars in s:
            if chars.isalnum():
                texts.append(chars.lower())

        while len(texts) > 1:
            if texts.pop(0) != texts.pop():
                return False

        return True


# if __name__ == "__main__:":
a = Solution()
print(a.isPalindrome("A man, a plan, a canal: Panama"))
print(a.isPalindrome("race a car"))

