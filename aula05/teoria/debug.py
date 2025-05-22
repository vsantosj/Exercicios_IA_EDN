import requests

response = requests.get('https://www.python.org')

if response.status_code == 200:
    print('Deu certo')
else:
    print(f'Deu ruim! erro {response.status_code}')
