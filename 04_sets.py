import re

user = 'yoeDev@65_'
pattern = r'^[\w._@]+$'
result = re.findall(pattern,user)
if result: print('User valido')
else: print('User Invalido')

emails = ['lo.que.+sea@shoppping.online', 'michael@gov.co.uk'] 

pattern = r'^[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}$'
result = [e for e in emails if re.match(pattern, e)]

if result: print(f'Emails validos: {result}')
else: print('No se encontraron emails validos')

# La negacion ^ dentro de los corchetes []
pattern = r'[^aeiou]'  #busca los caracteres que no son vocales 
print(re.findall(pattern, 'This is an example'))