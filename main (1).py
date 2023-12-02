# import os

          # Exercício 1: Criar um Diretório**

# with open('new_dir3', 'w') as new_dir3:
#  os.mkdir('new_dir3')

          # Exemplo 2: Entrar em um Diretório**

# import os
# with os.scandir('Aula22)') as entrada:
#     for arquivo in entrada:
#          if arquivo.is_file():
#              print(f'Arquivo encontrado: {arquivo.name}')

          # Exercício 3: Renomear um Diretório**
#os.rename('new_dir', 'new_dir2')

          # Exercício 4: Remover um Diretório**  
import shutil
shutil.rmtree('teste.txt')

          
          # Exercício 5: Listar Arquivos em um Diretório**

import os
with os.scandir('Aula22') as entrada:
    for arquivo in entrada:
        if arquivo.is_file():
            print(f'Arquivo encontrado: {arquivo.name}')
