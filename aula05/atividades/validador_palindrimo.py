def validar_palindromo(texto):

    texto_processado = ''

    for caractere in texto.lower():
        if caractere.isalnum():
            texto_processado += caractere

    return texto_processado == texto_processado[::-1]


texto = input("Digite uma palavra ou frase: ")
resultado = validar_palindromo(texto)

if resultado:
    resposta = "Sim"
else:
    resposta = "Não"

print(f"'{texto} é um palíndromo? {resposta}")