import re

#anular el signifcado del sombolo con la \ barra invertida

text = "The rain in Spain. but the rain in spain stays mainly in the plain. because the rain is in spain"

pattern = r'\.'  #busca las palabras que terminan en ain
result = re.findall(pattern, text)
print(len(result))

personal_data = "Mi numero de telefono es 123-456-7890. Mi numero de telefono del trabajo es +598-654-3210."

pattern = r'\+\d{3}-\d{3}-\d{4}'  #buscamos el numero de telefono con codigo de pais
result = re.findall(pattern, personal_data) 
if result:
    print(f'Si el numero es de Uruguay: {result}')
else:
    print("No se encontraron numeros de telefono")

username = '45kakahghjghjgj'
pattern = r'^\w{8,}'  #busca si el username tiene al menos 8 caracteres alfanumericos y comenzar con letras
result = re.findall(pattern, username) 
if result:
    print(f'Username valido: {result}')
else:
    print("Username invalido, debe tener al menos 5 caracteres alfanumericos")

list_file = 'Document.txt, Presentation.pptx, Image.jpeg, Music.mp3, Video.txt, Web.txt, Data.csv, Script.py'

pattern = r'\w+\.txt'  #busca los archivos que terminan en .txt
result = re.findall(pattern, list_file) 
print(f'Archivos con extension .txt: {result}')