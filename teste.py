import re

#modelo para testar conjunto de palavras
PT = ["023.123.123-12","023-123.123.123","12.234.521-12","123.1.2.12-12"]

reCPF1 = re.compile(r"([0-9]{3}.){2}[0-9]{3}-[0-9]{2}")

for i in PT:
    resultado = re.fullmatch(reCPF1,i)
    print(i, ": ", resultado)