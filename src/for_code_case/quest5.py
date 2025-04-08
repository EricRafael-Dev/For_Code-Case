def quest5(matriz):

    for i in range(len(matriz)):
        if i == 0:
            max_sum = matriz[i].copy()
            max_mult = matriz[i].copy()
        else:
            for j in range(len(matriz[i])):
                max_sum[j] = max_sum[j] + matriz[i][j]
                max_mult[j] = max_mult[j] * matriz[i][j]

    rows_max = [indice for indice, valor in enumerate(max_sum) if valor == max(max_sum)]
    cols_max = [indice for indice, valor in enumerate(max_mult) if valor == max(max_mult)]

    # communs = list(set(rows_max) & set(cols_max))
    return rows_max, cols_max

quest5([
    [1, 2, 3, 3],
    [4, 5, 6, 6],
    [7, 8, 9, 9]
]
)