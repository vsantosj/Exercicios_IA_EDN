try:
    numero =int(input('Digite um numero'))
    print(f'Você digitou o número {numero}')
except ValueError:
    print('Isso não é u númeto inteiro! Por favor, verifique')