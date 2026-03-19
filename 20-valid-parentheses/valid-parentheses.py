class Solution:
    def isValid(self, s: str) -> bool:
        # Стек для хранения открывающих скобок
        stack = []

        # Словарь соответствия закрывающей скобки открывающей
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            # Если символ - открывающая скобка, кладём в стек
            if ch in "([{":
                stack.append(ch)
            else:
                # Если стек пуст, значит закрывать нечего
                if not stack:
                    return False

                # Проверяем соответствие типа скобки
                if stack[-1] == pairs[ch]:
                    stack.pop()
                else:
                    return False

        # Если стек пуст - все скобки корректно закрылись
        return len(stack) == 0