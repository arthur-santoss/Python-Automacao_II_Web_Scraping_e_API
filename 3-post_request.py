import requests

# 1 - Dados em Dicionário
new_data = {
    'userId': 1,
    'id':1,
    'title':'Aprendendo Python',
    'body':'Manipulando informações da API com Requests'
}

# 2 - Endpoint da API
url = 'https://jsonplaceholder.typicode.com/posts'

# 3 - Envio de dados

post_response = requests.post(
    url,
    json=new_data    
)

print(post_response.status_code)


# 4 - Listar a informação
post_response_json = post_response.json()
print(post_response_json)

