# Trabalho de Cálculo Numérico

Projeto desenvolvido para a disciplina de Cálculo Numérico.

## Tema 1

Métodos numéricos para encontrar raízes de equações:

- Posição Falsa
- Newton-Raphson

### Função utilizada

O problema utiliza a função:

f(d) = a·d - d·ln(d)

onde:

- d é o deslocamento da extremidade do foguete, em centímetros;
- a é um parâmetro de ajuste.

O objetivo é determinar o deslocamento do foguete e verificar se ele ultrapassa o limite de segurança de 2 cm.

### Método da Posição Falsa

Neste projeto foi implementado o método da Posição Falsa para encontrar a raiz da função.

### Análise de segurança

A partir da função utilizada, foi analisado o valor do parâmetro `a` para determinar quando o foguete ultrapassa o limite de 2 cm.

O programa permite informar diferentes valores de `a`, intervalo de isolamento e precisão (`epsilon`), apresentando o resultado e a tabela das iterações.

## Estrutura do projeto

- `main.py` — execução principal do programa e classe `Foguete`;
- `funcoes.py` — função matemática utilizada no problema;
- `posicao_falsa.py` — implementação do método da Posição Falsa.

## Teste padrão

Para validação do método da Posição Falsa, foi utilizado o teste solicitado:

- `a = 1`
- Intervalo de isolamento: `(2, 3)`
- `epsilon = 10^-5`

Resultado aproximado:

`d = 2.718282 cm`

Como o deslocamento encontrado é maior que 2 cm, o foguete explode.

## Diagrama de classes

O diagrama de classes do projeto será disponibilizado nesta seção.

## Diagrama de classes

![Diagrama de classes](diagramacn.png)
