import re

text = "The rain in Spain. but the rain in spain stays mainly in the plain. because the rain is in spain"

pattern = r'a*' #aparece 0 o mas veces
result = re.findall(pattern, text)
print(len(result))

pattern = r'a+' #aparece 1 o mas veces
result = re.findall(pattern, text)
print(len(result))