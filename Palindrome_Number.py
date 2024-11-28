class Solution(object):
    def isPalindrome(self, x):
        list_x = list(str(x))
        list_x_revesed = list_x[::-1]
        if list_x == list_x_revesed:
            return True
        else:
            return False
