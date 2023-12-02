# MANIPULANDO DIRETORIOS

# With - nome do arquivo + r(Ler), ou seja, precisa do nome do arquivo, seguido do que será feito.
#No replit precisa fazer o upload do arquivo, no VSCODE - colocar todo o caminha da pasta
# import os


# with open ('file.txt','r') as arquivo:
#  conteudo =  arquivo.read()
#  print(conteudo)

#Criar novo diretorio
# import os
# with open('file.txt', 'w') as arquivo:
#   os.mkdir('novoarquivo')


# # scandir - scaneia todos os arquivos da pasta
# #Exemplo 1: Criar um Diretório**
# import os

# with os.scandir('novo') as entrada:
#       for arquivo in entrada:
#          print(f'Diretório encontrado: {arquivo.name}')

# #Exemplo 2: Entrar em um Diretório**
# import os

# with os.scandir('novo') as entrada:
#     for arquivo in entrada:
#          if arquivo.is_file():
#              print(f'Arquivo encontrado: {arquivo.name}')

##Exemplo 3: Renomear um Arquivo ou pasta 
# import os

# os.rename('novo', 'newarq') #diretorio
# os.rename('novo', 'new.txt') #Arquivo

#Exemplo 4: Remover um Diretório**
# import shutil

# shutil.rmtree('novapasta')

#Exemplo 6: Copiar Arquivos de um Diretório para Outro**


import shutil
os.rename('exemplo.txt', 'test5.txt')
