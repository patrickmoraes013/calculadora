"""
Calculadora simples em Python
Suporta: +, -, *, /, //, %, **, raiz quadrada
"""

import math


def adicionar(a: float, b: float) -> float:
    """Soma dois números."""
    return a + b


def subtrair(a: float, b: float) -> float:
    """Subtrai b de a."""
    return a - b


def multiplicar(a: float, b: float) -> float:
    """Multiplica dois números."""
    return a * b


def dividir(a: float, b: float) -> float:
    """Divide a por b."""
    if b == 0:
        raise ValueError("Erro: divisão por zero não é permitida.")
    return a / b


def divisao_inteira(a: float, b: float) -> int:
    """Divisão inteira de a por b."""
    if b == 0:
        raise ValueError("Erro: divisão por zero não é permitida.")
    return int(a) // int(b)


def resto(a: float, b: float) -> float:
    """Resto da divisão de a por b (módulo)."""
    if b == 0:
        raise ValueError("Erro: divisão por zero não é permitida.")
    return a % b


def potencia(a: float, b: float) -> float:
    """a elevado à potência b."""
    return a ** b


def raiz_quadrada(a: float) -> float:
    """Raiz quadrada de a."""
    if a < 0:
        raise ValueError("Erro: não existe raiz quadrada de número negativo.")
    return math.sqrt(a)


def mostrar_menu():
    """Exibe o menu de operações."""
    print("\n" + "=" * 40)
    print("         CALCULADORA SIMPLES")
    print("=" * 40)
    print("  1. Adição (+)")
    print("  2. Subtração (-)")
    print("  3. Multiplicação (*)")
    print("  4. Divisão (/)")
    print("  5. Divisão inteira (//)")
    print("  6. Resto/Módulo (%)")
    print("  7. Potência (**)")
    print("  8. Raiz quadrada (√)")
    print("  0. Sair")
    print("=" * 40)


def main():
    while True:
        mostrar_menu()
        opcao = input("\nEscolha uma operação: ").strip()

        if opcao == "0":
            print("\nAté logo!")
            break

        # Operações que precisam de um único número
        if opcao == "8":
            try:
                num = float(input("Digite o número: "))
                resultado = raiz_quadrada(num)
                print(f"\n√{num} = {resultado}")
            except ValueError as e:
                print(f"\n{e}")
            continue

        # Operações que precisam de dois números
        if opcao in ("1", "2", "3", "4", "5", "6", "7"):
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                resultado = None

                if opcao == "1":
                    resultado = adicionar(num1, num2)
                    print(f"\n{num1} + {num2} = {resultado}")
                elif opcao == "2":
                    resultado = subtrair(num1, num2)
                    print(f"\n{num1} - {num2} = {resultado}")
                elif opcao == "3":
                    resultado = multiplicar(num1, num2)
                    print(f"\n{num1} × {num2} = {resultado}")
                elif opcao == "4":
                    resultado = dividir(num1, num2)
                    print(f"\n{num1} ÷ {num2} = {resultado}")
                elif opcao == "5":
                    resultado = divisao_inteira(num1, num2)
                    print(f"\n{num1} // {num2} = {resultado}")
                elif opcao == "6":
                    resultado = resto(num1, num2)
                    print(f"\n{num1} % {num2} = {resultado}")
                elif opcao == "7":
                    resultado = potencia(num1, num2)
                    print(f"\n{num1} ^ {num2} = {resultado}")

            except ValueError as e:
                print(f"\n{e}")
            except ZeroDivisionError:
                print("\nErro: divisão por zero não é permitida.")
        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
