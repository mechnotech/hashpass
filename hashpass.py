import hashlib
import os


#pas = getpass.getpass("Пароль для шифровки :")
print('Результат появится в буфере обмена, можно вставить в браузере Ctrl + V')
pas = input("Ввеите фразу для шифровки :")
pas = pas + "secretphrase12"  # Секретная соль, нужно изменить под себя
result = hashlib.sha224(pas.encode()).hexdigest()
result = 'V!6' + result[5:21]  # Эти параметры тоже можно изменить, добавив спецсимволы, изменив размер среза
print('Результат в буфере обмена, можно вставить в браузере Ctrl + V')
cmd = 'echo ' + str(result) + '| clip'
os.system(cmd)
#input('Нажмите ENTER для выхода')


