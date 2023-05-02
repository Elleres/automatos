import re

""" Resolução da segunda questão.
    Para executar o programa, vá até a linha ALTERAR LINHA, altere a expressão regular que você deseja testar e a
    cadeia que será analisada.
    Para fazer isso, mude a variável fraseTeste e altere o primeiro parâmetro
    da função fullmatch para uma das expressões regulares abaixo.
"""

# A) Casais heterossexuais mais velhos que os filhos com pelo menos duas filhas mulheres,
# ou pelo menos um filho homem, ou ainda pelo menos dois filhos homens e uma filha mulher.


# reA = re.compile(r"(MH|HM)[m h]")

# B) Casais heterossexuais mais velhos que os filhos e com uma quantidade ímpar de filhas
# mulheres.

reB = re.compile(r"(HM|MH)h*mh*(h*mh*mh*)*")

# C) Casais heterossexuais mais velhos que os filhos, com a filha mais velha mulher e o filho
# mais novo homem

reC = re.compile(r"(MH|HM)m[h m]*h")

# D) Casais homossexuais mais velhos que os filhos, com pelo menos seis filhos, em que os
# dois primeiros filhos formam um casal e os últimos também.

reD = re.compile(r"(MM|HH)(hm|mh)[h m]{2}[h m]*(hm|mh)")

# E) Casais homossexuais mais velhos que os filhos, em que o sexo dos filhos é alternado
# conforme a ordem de nascimento

reE = re.compile(r"(MM|HH)(hm)|(mh)")

# F) Casais homossexuais mais velhos que os filhos, com qualquer quantidade de filhos
# homens e mulheres, mas que não tiveram dois filhos homens consecutivos.

reF = re.compile(r"(MM|HH)(mm|hm|m)*(h|mh)?")

# G)  Arranjo de no mínimo x∈ℕ e no máximo y∈ℕ , com x>0 , y>0 , e x≤y , de
# adultos (Hs ou Ms) mais velhos que os filhos, com qualquer quantidade de filhos
# homens e mulheres, mas que os três filhos mais novos não foram homens.

reG = re.compile(r"(M|H)+(h|m)*(m|mh|mhh)|\\s|h|hh")

fraseTeste = "MMhmhmhmhm"
resposta = re.fullmatch(reG, fraseTeste)

print(resposta)
