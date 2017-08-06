class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        left = ["(", "[", "{"]
        right = [")", "]", "}"]

        for char in s:
            if char in left:
                stack.append(char)
            else:
                if not stack:
                    return False
                if left.index(stack.pop()) != right.index(char):
                    return False
        if stack:
            return False
        return True