from funcoes import funcao
from posicao_falsa import posicao_falsa
import math 

LIMITE_A = math.log(2)

class Foguete:
    def __init__(self, a, di, ds, epsilon):
        self.a = a
        self.di = di
        self.ds = ds
        self.epsilon = epsilon

    def calcular_posicao(self):
        def f(d):
            return funcao(d, self.a)

        return posicao_falsa(
            f,
            self.di,
            self.ds,
            self.epsilon
        )


def main():

    print("======================================")
    print("       TRABALHO DE CÁLCULO NUMÉRICO")
    print("          TEMA 1 - FOGUETE")
    print("          MÉTODO DA POSIÇÃO FALSA")
    print("======================================")

    # Entrada da quantidade de foguetes
    n = int(input("\nNúmero de foguetes: "))

    # Entrada da precisão
    epsilon = float(input("Precisão (epsilon): "))

    # Processa cada foguete
    for i in range(1, n + 1):

        print(f"\n========== FOGUETE {i} ==========")

        # Dados do foguete
        a = float(input("Valor de a: "))
        di = float(input("Limite inferior do isolamento: "))
        ds = float(input("Limite superior do isolamento: "))

        # Cria o objeto foguete
        foguete = Foguete(a, di, ds, epsilon)

        # Cria a função para o valor de a informado
        def f(d):
            return funcao(d, a)

        try:

            # Calcula a posição usando o método da Posição Falsa
            raiz, tabela = foguete.calcular_posicao()

            # Resultado
            print("\n===== RESULTADO =====")
            print(f"Deslocamento encontrado: {raiz:.6f} cm")
            print(f"Número de iterações: {len(tabela)}")

            # Verifica o limite de segurança
            if raiz > 2:
                print("Status: FOGUETE EXPLODE")
            else:
                print("Status: FOGUETE NÃO EXPLODE")

            # Analisa o valor de a
            if a <= LIMITE_A:
                print(f"Valor de a está dentro do limite ({LIMITE_A:.6f}).")
            else:
                print(f"Valor de a ultrapassa o limite ({LIMITE_A:.6f}).")

            # Tabela das iterações
            print("\n===== TABELA DE ITERAÇÕES =====")

            print(
                f"{'Iter.':<8}"
                f"{'di':<12}"
                f"{'ds':<12}"
                f"{'dr':<12}"
                f"{'f(dr)':<15}"
                f"{'Erro':<15}"
            )

            for linha in tabela:

                print(
                    f"{linha['iteracao']:<8}"
                    f"{linha['di']:<12.6f}"
                    f"{linha['ds']:<12.6f}"
                    f"{linha['dr']:<12.6f}"
                    f"{linha['f_dr']:<15.6f}"
                    f"{linha['erro']:<15.6f}"
                )

        except ValueError as erro:

            print(f"\nErro: {erro}")


if __name__ == "__main__":
    main()