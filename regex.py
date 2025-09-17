import re
import sys

pattern = r'Hello'

text = "Hello Words"
result = re.search(pattern,text)
init, last = result.span()
if result:
    print(text[init:last])
    print(result.group())
    start = result.start()
    end = result.end()
    print(text[start:end])
else:
    print("No match")

text = "Encuentra la posicion donde paracece la palabra IA e indica donde comienza y donde termina!"

patron = "IA"
resultado = re.search(patron, text)

print(resultado.span())
print(f'{resultado.start()}, {resultado.end()}')

python = 'Me gusta programar en Python. Python es un lenguaje de programacion,' \
' no tan ficil de aprender. Auque ojo con Python, que es un lenguaje de programacion muy potente! '

patron = r'Python'
resultados = re.findall(patron, python)

def count_matches(resultados):
    count = 0
    if resultados is None:
        return count
    for _ in resultados:
        count += 1
    return count

print(type(resultados))
print(len(list(resultados)))
print(re.findall)
print(f'El patron se encontro {count_matches(resultados)} veces')

test = 'Encontre a Ana en el parque. Ana me dijo que Ana vendria a la fiesta. Ana , Ana, Ana...'
patron = r'Ana'
resultados = re.findall(patron, test)

print(type(resultados))
print(sys.version)

test = 'Ala Ana Ana'
resultado = re.findall(r'Ana', test)
print(f"Tipo: {type(resultado)}")
print(f"Contenido: {resultado}")


search_item = re.finditer(r'A.a', test)
for match in search_item:
    print(f"Match: {match.group()} - Start: {match.start()} - End: {match.end()}")

texto= 'La IA es lo mejor que a pasado en los ultimos tiempos. La IA llego para quedarse. La IA es el futuro. La iA, la ia, la IA...'
pattern = r'IA'
resultados = re.finditer(pattern, texto, re.IGNORECASE)

for match in resultados:
    print(f"Match: {match.group()} - Start: {match.start()} - End: {match.end()}")

replace = "ChatGPT"
new_text = re.sub(pattern, replace, texto, flags=re.IGNORECASE)
print(new_text)