import requests

# 1 - versão e métodos da biblioteca 
# print(requests.__version__)
# print(dir(requests))

# 2 - realizando requisição GET
link = 'https://www.google.com/search?q=dolar'
requisicao = requests.get(link)
print(requisicao)
print(requisicao.status_code)
print(requisicao.text)