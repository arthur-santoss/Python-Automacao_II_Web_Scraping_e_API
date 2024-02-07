# coding: utf-8
import sys
from bs4 import BeautifulSoup


# 1 - Importando arquivo local
with open('pages/index.html', 'r', encoding='utf-8') as file_html:
     content = file_html.read()
    #  print(content)
     soup = BeautifulSoup(content, 'lxml')
     print(soup.prettify())
     
# 2 - Recuperando títulos das vagas
     vagas = soup.find('h5')
     cursos = soup.find_all('h5')
    #  print(cursos)
    #  for curso in cursos:
    #      print(curso.text)
    
# 3 - pegando todas as informações
course_cards = soup.find_all('div',class_='card')
# print(course_cards)
for course in course_cards:
    # print(course.h5.text)
    # print(course.p.text)
    # print(course.a.text.split()[-1])
    
    name = course.h5.text
    description = course.p.text
    price = course.a.text.split()[-1]
    
    print(f'{name} com descrição {description}, custa {price}')