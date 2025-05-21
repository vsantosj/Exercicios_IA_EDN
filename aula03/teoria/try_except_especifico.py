try:
    numerador = int(input("Digite o numerador: "))
    denominador = int(input("Digite o denominador: "))
    resultado = numerador / denominador
    print(f"O resultado é {resultado}")
except ValueError:
    #Erro de tipo
    print("Insira apenas números")
except ZeroDivisionError:
    #Erro de divisão por zero
    print("Não é possível dividir por zero")