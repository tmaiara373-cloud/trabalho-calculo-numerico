from funcoes import funcao, derivada
from posicao_falsa import posicao_falsa
from newton_raphson import newton_raphson
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

    def calcular_newton_raphson(self):
        def f(d):
            return funcao(d, self.a)

        def df(d):
            return derivada(d, self.a)

        #Estimativa inicial para o deslocamento
        d0 = (self.di + self.ds) / 2.0

        return newton_raphson(
            f,
            df,
            d0,
            self.epsilon
        )

def main():

    # Entrada da quantidade de foguetes
    n = int(input("\nNúmero de foguetes: "))

    # Entrada da precisão
    epsilon = float(input("Precisão (epsilon): "))

    # Menu para escolha do método
    print("\nEscolha o método numérico:")
    print("1 - Posição Falsa")
    print("2 - Newton-Raphson")
    opcao_metodo = int(input("Opção (1 ou 2): "))

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
            # Seleciona o método numérico escolhido
            if opcao_metodo == 1:
                raiz, tabela = foguete.calcular_posicao()
                nome_metodo = "Posição Falsa"
                col_2 = "di"
                col_3 = "ds"
            elif opcao_metodo == 2:
                raiz, tabela = foguete.calcular_newton_raphson()
                nome_metodo = "Newton-Raphson"
                col_2 = "d_k"
                col_3 = "f'(d_k)"
            else:
                print("Opção de método inválida!")
                return

            # Resultado
            print(f"\n===== RESULTADO ({nome_metodo.upper()}) =====")
            print(f"Deslocamento encontrado: {raiz:.6f} cm")
            print(f"Número de iterações: {len(tabela)}")

            # Verifica o limite de segurança
            if raiz > 2:
                print("Status: FOGUETE EXPLODE")
            else:
                print("Status: FOGUETE NÃO EXPLODE")

            
            # Análise de segurança
            print("\n===== ANÁLISE DE SEGURANÇA =====")
            print(f"Limite de a: {LIMITE_A:.6f}")
            print(f"Valor de a: {a:.6f}")

            if a <= LIMITE_A:
                print("Conclusão: a <= ln(2)")
                print("Status: FOGUETE NÃO EXPLODE")
            else:
                print("Conclusão: a > ln(2)")
                print("Status: FOGUETE EXPLODE")

            # Tabela das iterações
            print(f"\n===== TABELA DE ITERAÇÕES ({nome_metodo.upper()}) =====")

            print(
                f"{'Iter.':<8}"
                f"{col_2:<12}"
                f"{col_3:<12}"
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