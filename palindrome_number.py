"""
Palindrome Number
Determine whether an integer is a palindrome. Do this without extra space
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            result_state = False
        else:
            s = str(x)
            n = len(s)
            result_state = True
            if n % 2 == 0:
                n_len = int(n / 2)
            else:
                n_len = int(n // 2)
            for i in range(n_len):
                if s[i] != s[n - 1 - i]:
                    result_state = False
                    break
        return result_state
