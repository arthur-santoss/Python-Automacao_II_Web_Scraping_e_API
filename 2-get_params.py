import requests

# 1 - API JsonPlaceHolder
url = 'https://jsonplaceholder.typicode.com/posts/'

# 2 - adicionando um payLoad
paylaod = {
    "id": [1, 2, 3, 4, 5], 
    "userId": 1
}

# 3 - Realizando requisição
response = requests.get(url, params=paylaod)
# print(response)
# print(response.json() )

# 4 - Melhorar a legibilidade
response_json = response.json()
for i in response_json:
    print(i, '\n')