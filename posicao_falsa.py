def posicao_falsa(funcao, di, ds, epsilon):
    """
    Método da Posição Falsa.

    funcao: função que queremos encontrar a raiz
    di: limite inferior do intervalo
    ds: limite superior do intervalo
    epsilon: precisão desejada
    """

    tabela = []

    # Calcula a função nos extremos do intervalo
    f_di = funcao(di)
    f_ds = funcao(ds)

    # Verifica se existe mudança de sinal
    if f_di * f_ds > 0:
        raise ValueError(
            "O intervalo não possui mudança de sinal."
        )

    erro = float("inf")
    dr_anterior = None
    iteracao = 0

    while erro > epsilon:

        iteracao += 1

        # Fórmula da Posição Falsa
        dr = (
            di * f_ds - ds * f_di
        ) / (
            f_ds - f_di
        )

        # Calcula f(dr)
        f_dr = funcao(dr)

        # Calcula o erro absoluto
        if dr_anterior is None:
            erro = float("inf")
        else:
            erro = abs(dr - dr_anterior)

        # Guarda os dados da iteração
        tabela.append({
            "iteracao": iteracao,
            "di": di,
            "ds": ds,
            "dr": dr,
            "f_dr": f_dr,
            "erro": erro
        })

        # Atualiza o intervalo
        if f_di * f_dr < 0:
            ds = dr
            f_ds = f_dr
        else:
            di = dr
            f_di = f_dr

        dr_anterior = dr

    return dr, tabela