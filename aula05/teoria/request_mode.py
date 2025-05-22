import requests

response = requests.get('https://www.python.org')

if response.status_code == 200
    print('Deu certo')

    print(response.text[:100])
else:
    print((f'Não deu certo {response.status_code}'))