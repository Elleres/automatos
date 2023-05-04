import re
#data e hora
datahora = ["12/23/5235 21:45:88", "44/44/44 44:44:44", "07/10/2003 03:45:05", "2/3/2012 6:23", "23/34/567812:12:12"]
cadeia_aceita = []
cadeia_rejeitada = []
reDH = re.compile(r"[0-9]{2}/[0-9]{2}/[0-9]{4} [0-9]{2}:[0-9]{2}:[0-9]{2}")

for dh in datahora:
    resultado = re.fullmatch(reDH, dh)
    if resultado != None:
        cadeia_aceita.append(dh)
    else:
        cadeia_rejeitada.append(dh)

print("Cadeia aceita: {}\nCadeia rejeitada: {}".format(cadeia_aceita, cadeia_rejeitada))

#número real com ou sem sinal
num = ["+1.45", "-2.0", "0", "0.0", "1.", ".25", "-"]
cadeia_aceita = []
cadeia_rejeitada = []
reNUM = re.compile(r"[+ -]?[0-9]+(\.[0-9]+)?")

for item in num:
	resultado = re.fullmatch(reNUM, item)
	if resultado != None:
        	cadeia_aceita.append(item)
	else:
        	cadeia_rejeitada.append(item)

print("Número aceito: {}\nNúmero rejeitado: {}".format(cadeia_aceita, cadeia_rejeitada))

#casais heterossexuais com a filha mais velha mulher e o filho mais novo homem
casais = ["HHmhmhmhmmhm", "HMmmmmhmh", "MHm", "MMhmhmmmhm", "MHmhhmhmh", "MHmhhhh", "HMmmmmh", "MHmmm", "HMhhm", "HHmhmh"]
cadeia_aceita = []
cadeia_rejeitada = []
recasais = re.compile(r"(MH|HM)m[h m]*h")

for casal in casais:
	resultado = re.fullmatch(recasais, casal)
	if resultado != None:
        	cadeia_aceita.append(casal)
	else:
        	cadeia_rejeitada.append(casal)

print("Casal aceito: {}\nCasal rejeitado: {}".format(cadeia_aceita, cadeia_rejeitada))
