class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operators = ["+", "-", "*", "/"]
        ptr = 0
        stack = []
        for item in tokens:
            if item not in operators:
                stack.append(int(item))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                operator = item
                result = 0
                if operator == "+":
                    result = operand1 + operand2
                elif operator == "-":
                    result = operand1 - operand2
                elif operator == "*":
                    result = operand1 * operand2
                else:
                    result = int(operand1 * 1.0 / operand2)
                stack.append(result)
        return stack[0]
