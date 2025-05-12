height = float(input('Digite sua altura'))
weight = float(input('Digite seu peso'))

imc = weight / (height**2)

print(f'Seu IMC atual é: {imc:.2f}')


if (imc < 18.5):
    print('Abaixo do peso')
elif(imc < 25):
    print('Peso normal')
elif(imc < 30):
    print('Sobrepeso')
else:
    print("Acima do peso")