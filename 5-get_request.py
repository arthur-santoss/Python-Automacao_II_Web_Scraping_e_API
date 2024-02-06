import requests

# 1 - mapeando informação
headers = {'X-Github-Api-Version': '2022-11-28'}

base_api = 'https://api.github.com'
user = 'OneBitCodeBlog'
url = f'{base_api}/users/{user}/repos'

print(url)

# 2- realizando a equisição
response = requests.get(url, headers=headers)
print(response.status_code)
print(len(response.json()))
print(response.json())