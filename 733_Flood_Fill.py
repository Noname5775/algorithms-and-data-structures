class Solution:
    def floodFill(self, image, sr, sc, color):
        # Исходный цвет стартовой клетки
        original_color = image[sr][sc]

        # Если цвет уже совпадает с новым, ничего менять не нужно
        if original_color == color:
            return image

        rows = len(image)
        cols = len(image[0])

        def dfs(r, c):
            # Проверяем выход за границы
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            # Если цвет не совпадает с исходным, дальше идти нельзя
            if image[r][c] != original_color:
                return

            # Перекрашиваем текущую клетку
            image[r][c] = color

            # Идём во все 4 стороны
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image