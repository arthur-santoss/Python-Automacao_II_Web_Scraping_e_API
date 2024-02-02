import requests

# 1 - API JsonPlaceHolder
url = 'https://jsonplaceholder.typicode.com/posts/1'

# 2 - Requisição GET
reponse = requests.get(url)
print(reponse)
print(reponse.status_code)

# 3 - Exeplo de tratamento
if reponse.status_code == 200:
    print('código de sucesso foi retornado')
else:
    print('A requisição não foi retornada corretamente')
    
# 4 - Pegar os dados
reponse_json = reponse.json()
print(reponse_json)