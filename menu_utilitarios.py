"""
Menu de Utilitários em Python
-------------------------------
Programa simples com três funcionalidades, escolhidas por menu:

1. Verificador de número (par/ímpar e positivo/negativo/zero)
2. Calculadora (soma, subtração, multiplicação e divisão)
3. Tabuada de um número

Autora: Emilly Lorrany Alves dos Santos
"""


def verificar_numero():
    """Verifica se um número é par ou ímpar, e se é positivo, negativo ou zero."""
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        print(f"O número {numero} é par")
    else:
        print(f"O número {numero} é ímpar")

    if numero > 0:
        print("O número é positivo")
    elif numero < 0:
        print("O número é negativo")
    else:
        print("O número é zero")


def calculadora():
    """Realiza operações básicas (+, -, *, /) entre dois números."""
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Escolha a operação (+, -, *, /): ")

    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        if num2 == 0:
            print("Erro: Divisão por zero!")
            return
        resultado = num1 / num2
    else:
        print("Erro: Operação inválida!")
        return

    print(f"Resultado: {num1} {operacao} {num2} = {resultado}")


def tabuada():
    """Exibe a tabuada de um número, de 1 a 10."""
    numero = int(input("Digite um número: "))
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


def main():
    print("Escolha uma opção:")
    print("1 - Verificar número (par/ímpar, positivo/negativo)")
    print("2 - Calculadora")
    print("3 - Tabuada")
    opcao = int(input("Opção: "))

    if opcao == 1:
        verificar_numero()
    elif opcao == 2:
        calculadora()
    elif opcao == 3:
        tabuada()
    else:
        print("Opção inválida!")


if __name__ == "__main__":
    main()
