class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = int(tokens[0])
        
        for tok in tokens:
            if tok == "+":
                rhs = stack.pop()
                lhs = stack.pop()
                stack.append(lhs + rhs)
            elif tok == "-":
                rhs = stack.pop()
                lhs = stack.pop()
                stack.append(lhs - rhs)
            elif tok == "*":
                rhs = stack.pop()
                lhs = stack.pop()
                stack.append(lhs * rhs)
            elif tok == "/":
                rhs = stack.pop()
                lhs = stack.pop()
                stack.append(int(lhs / rhs))
            else:
                stack.append(int(tok))
        return stack.pop()
        
