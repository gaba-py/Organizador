#criar um programa que pegue uma pasta que esta com arquivos de diversos tipos e
# coloque em pastas separadas de acordo com a extensão do arquivo

# CASO QUEIRA FAZER O USO DESTE CÓDIGO, E NECESSÁRIO MODIFICAR O CAMINHO DA PASTA DE DOWNLOADS,
# PARA A PASTA QUE DESEJA ORGANIZAR

import os
import shutil

# E necessario modificar o caminho da pasta de 'Downloads' para a pasta que deseja organizar
downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')

for file in os.listdir(downloads_folder):
    filename, file_extension = os.path.splitext(file)
    file_extension = file_extension[1:]
    print(filename, file_extension)

    folder_to_organize_files = f'{downloads_folder}/{file_extension}'

    if not os.path.isdir(folder_to_organize_files):
        os.mkdir(folder_to_organize_files)

    shutil.move(f'{downloads_folder}/{file}', f'{folder_to_organize_files}/{file}')

print(downloads_folder)