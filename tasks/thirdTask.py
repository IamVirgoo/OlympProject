def main(coins_matrix):
    # Получаем количество строк и столбцов в матрице
    coin_matrix_row_length, coin_matrix_colum_length = len(coins_matrix), len(coins_matrix[0])

    # Создаем пустую матрицу dp для хранения суммы монет на каждой позиции
    dp = [[0] * coin_matrix_colum_length for _ in range(coin_matrix_row_length)]

    # Заполняем первую строку и первый столбец матрицы dp суммами монет следующих строк и столбцов
    dp[0][0] = coins_matrix[0][0]
    for i in range(1, coin_matrix_colum_length):
        dp[0][i] = dp[0][i-1] + coins_matrix[0][i]
    for i in range(1, coin_matrix_row_length):
        dp[i][0] = dp[i-1][0] + coins_matrix[i][0]

    # Заполняем остальные ячейки матрицы dp
    for i in range(1, coin_matrix_row_length):
        for j in range(1, coin_matrix_colum_length):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + coins_matrix[i][j]

    # Возвращаем максимальное количество монет в комнате
    print(dp[coin_matrix_row_length-1][coin_matrix_colum_length-1])


# Проверяем на корректность и вызываем необходимую функцию
if __name__ == "__main__":
    # Вводим количество строк и столбцов матрицы
    n, m = map(int, input().split())
    matrix = []
    # В цикле вводим элементы матрицы
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    # Вызываем необходимую функцию
    main(matrix)
