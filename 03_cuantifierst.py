import re

text = "The rain in Spain. but the rain in spain stays mainly in the plain. because the rain is in spain"

pattern = r'a*' #aparece 0 o mas veces
result = re.findall(pattern, text)
print(len(result))

pattern = r'a+' #aparece 1 o mas veces
result = re.findall(pattern, text)
print(len(result))

#encuentra las palabras de mas de 4 letras
pattern = r'\b\w{4,6}\b' #busca las palabras que terminan en ain
result = re.findall(pattern, text)  
print(result)
print(len(result))

pattern = r'\b\w{6,}\b' #busca las palabras que terminan en ain
result = re.findall(pattern, text)  
print(result)
print(len(result))