class Solution:
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            # Если это число, просто кладём в стек
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
            else:
                # Сначала достаём правый операнд
                b = stack.pop()
                # Потом левый операнд
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    # Деление должно идти с усечением к нулю
                    stack.append(int(a / b))

        return stack[-1]