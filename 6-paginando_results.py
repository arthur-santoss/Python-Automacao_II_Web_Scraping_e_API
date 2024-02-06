import requests
from collections import Counter

# 1 - autenticação GitHub
with open('token_github.txt', 'r') as f:
    vlr_token = f.readline()
    
acess_token = vlr_token
headers = {
    'Authorization': 'Bearer ' + acess_token,
    'X-Github-Api-Version': '2022-11-28'
}

# 2 - Mapeando informações
base_api = 'https://api.github.com'
user = 'arthur-santoss'
url = f'{base_api}/users/{user}/repos'

# 3 - Organizando os dados
repost_list = []
for page_num in range(1,3):
    try:
        url_page = f'{url}page={page_num}'
        response = requests.get(url,headers=headers)
        repost_list.append(response.json())
    except:
        repost_list.append(None)
        
# 4 - Apresentando os dados
# print(len(repost_list))
# print(repost_list[0][2]['name'])

# 5 - Pegando o nome de cada repositório
name_repos = []
for page in repost_list:
    for repo in page:
        # print(repo['name'])
        name_repos.append(repo['name'])
# print(len(name_repos))
# print(name_repos[:10])

# 6 - pegando a linguagem de cada repositório
lang_repos = []
for page in repost_list:
    for repo in page:
        lang_repos.append(repo['language'])
# print(len(lang_repos))
# print(lang_repos[:10])        

# 7 - contando ocorrências das linguagens
print(Counter(lang_repos))

