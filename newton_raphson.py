def newton_raphson(funcao, derivada, d0, epsilon, max_iter=100):
    """
    Método de Newton-Raphson
    funcao: f(d)
    derivada: f'(d)
    d0: estimativa inicial para o deslocamento 
    epsilon: precisão desejada
    max_iter: número máximo de iterações
    """
    tabela = []
    d_atual = d0
    erro = float("inf")
    iteracao = 0

    while erro > epsilon and iteracao < max_iter:
        iteracao += 1
        f_d = funcao(d_atual)
        df_d = derivada(d_atual)

        if df_d == 0:
            raise ValueError("A derivada é zero. Não é possível continuar.")
        
        #fórmula de Newton-Raphson: d_{k+1} = d_k - f(d_k)/f'(d_k)
        d_proximo = d_atual - f_d / df_d

        #cálculo do erro absuluto 
        erro = abs(d_proximo - d_atual)

        #guarda os dados da iteração
        tabela.append({
            "iteracao": iteracao,
            "di": d_atual,
            "f_dr": f_d,
            "ds": df_d,
            "dr": d_proximo,
            "erro": erro
        })

        d_atual = d_proximo

    return d_atual, tabela
