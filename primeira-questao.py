import re

""" Resolução da primeira questão.
    Para executar o programa, vá até a linha 115, altere a expressão regular que você deseja testar e a
    cadeia que será analisada.
    Para fazer isso, mude a variável fraseTeste e altere o primeiro parâmetro
    da função fullmatch para uma das expressões regulares abaixo.
"""
# Nome, nome do meio e sobrenome

# Considere os seguintes alfabetos Σ = {a, b, c, …, z}, Γ = {A, B, C, …, Z} e N = {0, 1, 2, …, 9}.

# 1) Nome, nome do meio e sobrenome devem vir separados por um espaço apenas

reNome1 = re.compile(r"([A-z]+ ){2}[A-z]+")

# 2) O nome do meio é opcional

reNome2 = re.compile(r"[A-z]+ ([A-z]+ )?[A-z]+")

# 3) Nome e sobrenome devem ser ambos não vazios

reNome3 = re.compile(r"[A-z]+ ([A-z]+ )?[A-z]+")

# 4) Não deve aceitar caracteres especiais ou números

reNome4 = re.compile(r"([A-z]+ ){2}[A-z]+")

# 5) O primeiro símbolo do nome e sobrenome, e do nome do meio se existir, deve ser
# do alfabeto Γ e os outros símbolos devem ser do alfabeto Σ

reNome5 = re.compile(r"[A-Z][a-z]+ ([A-Z][a-z]+ )?[A-Z][a-z]+")

# Email

# 1) Sentenças devem conter um, e apenas um, símbolo “@”

reEmail1 = re.compile(r"[A-z0-9]*@{1}[A-z0-9]*")

# 2) Excetuando o símbolo “@”, as sentenças possuem apenas símbolos de Σ

reEmail2 = re.compile(r"[A-z0-9]*@[a-z]+")

# 3) Sentenças não devem começar com o símbolo “@”

reEmail3 = re.compile(r"[A-z0-9]+@[A-z0-9]*")

# 4) Sentenças devem terminar com a subcadeia “.com.br” ou “.br”

reEmail4 = re.compile(r"[A-z0-9]*@[A-z0-9]*((\.com\.br)|(\.br))")

# 5) Sentenças devem ter, pelo menos, um símbolo de Σ entre o símbolo “@” e a
# subcadeia “.com.br” ou a subcadeia “.br”

reEmail5 = re.compile(
    r"[A-Z0-9]*[a-z]+[A-z0-9]*@[A-Z0-9]*[a-z]+[A-z0-9]*((\.com\.br)|(\.br))")

# Senhas

# 1) Sentenças podem conter símbolos de Σ ∪ Γ ∪ N

reSenhas1 = re.compile(r"[A-z0-9]+")

# 2) Sentenças devem ter pelo menos um símbolo de Γ e outro de N

reSenhas2 = re.compile(
    r"(([a-z]*[A-Z]+[0-9]+)|([a-z]*[0-9]+[A-Z]+)|([A-Z]+[a-z]*[0-9]+)|([A-Z]+[0-9]+[a-z]*)|([0-9]+[A-Z]+[a-z]*)|([0-9]+[a-z]*[A-Z]+))")

# 3) Sentenças devem ter comprimento igual a 8

reSenhas3 = re.compile(r"[A-z0-9]{8}")

# CPF

# 1) Sentenças devem ter o formato xxx.xxx.xxx-xx, onde x pertence a N

reCPF1 = re.compile(r"([0-9]{3}.){2}[0-9]{3}-[0-9]{2}")

# Telefone

# 1) Sentenças devem ter um dos formatos seguintes

reTel = re.compile(
    r"((\([0-9]{2}\) 9[0-9]{4}-[0-9]{4})|(\([0-9]{2}\) 9[0-9]{4}[0-9]{4})|([0-9]{2} 9[0-9]{8}))")

# Data e Horário

# 1) Sentenças devem ter o formato dd/mm/aaaa hh:mm:ss, onde d, m, a, h, m, s N.

reDH = re.compile(
    r"[0-9]{2}/[0-9]{2}/[0-9]{1,4} [0-2][0-9]:[0-5][0-9]:[0-5][0-9]")

# Número real com ou sem sinal

# 1) Sentenças devem começar com um dos símbolos do alfabeto {+, -, ε}

reNum1 = re.compile(r"[+ -]?[0-9A-z]*")

# 2) Em seguida, as sentenças devem ter, pelo menos, um símbolo do alfabeto N

reNum2 = re.compile(r"[+ -]?[0-9]+")

# 3) Em seguida, as sentenças devem ter, exatamente, um símbolo separador “.”

reNum3 = re.compile(r"[+ -]?[0-9]+\.")

# 4) Em seguida, as sentenças devem finalizar com, pelo menos, um símbolo de N

reNum4 = re.compile(r"[+ -]?[0-9]+\.[0-9]+")

# 5) Exceção: números sem a parte fracionária também devem ser aceitos

reNum5 = re.compile(r"[+ -]?[0-9]+(\.[0-9]+)?")


reNum = re.compile(r"[+ -]?[0-9]+(\.[0-9]+)?")

fraseTeste = "AAAA210A"
resultado = re.fullmatch(reSenhas3, fraseTeste)
print(resultado)
