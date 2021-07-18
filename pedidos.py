# -*- coding: utf-8 -*-

import requests

## O primeiro argumento é o arquivo de saída e o segundo o modo de acesso, "w"
# para sobrescrever, "a" para escrever no final.
file = open("pedidos.csv", "w")

# Número do primeiro pedido
min = 6

# Número seguinte ao último pedido (ex. deve ser 42, se o número do último
# pedido for 41).
max = 241

## Vetores de identificadores:
# O primeiro elemento deve existir no arquivo html somente logo antes de uma
# ocorrência do campo.
# O segundo elemento deve identificar o exato começo do campo após a ocorrência
# do primeiro elemento no arquivo html.
prod_ref = ["media-body", "editar\">"]
tam_ref = ["Tamanhos dos Moletons", "<strong>"]
qtd_ref = ["Qtd", "\">"]


## Cookies de seção
# Deve conter o cookie sessionid.
# ex:	'sessionid'	:	'H4shMu1t0R34l15ta'
cookies = {
}

users = []

## Acha o campo referenciado por ref a partir de html[index] e incrementa
# index para o índice do final do campo.
# Retorna o valor do campo e o index incrementado.
def search(html, index, ref):
	index = html.find(ref[0], index)
	index = html.find(ref[1], index) + len(ref[1])

	return html[index:html.find("<", index)].strip() , index

# Itera sobre os ids dos pedidos.
for id in range(min, max):
	page = requests.get(f"https://app.lojaintegrada.com.br/painel/pedido/{id}/detalhar", cookies = cookies)
	
	# Arquivo html da página do pedido.
	html = page.content.decode("utf-8")

	# Número de ocorrências do primeiro identificador.
	n = html.count(prod_ref[0])
	# Verifica se o primeiro identificador ocorre no arquivo.
	if n == 0:
		print(f"Erro no pedido {id}: identificador \"" + prod_ref[0] + "\" não existe")
		exit()

	# Verifica se os identificadores existem na mesma quantidade (um por item).
	if n != html.count(tam_ref[0]):
		print(f"Erro no pedido {id}: identificadores não estão batendo")
		exit()

	# Verifica o status do pedido.
	if html.count("Pedido Pago") <  3:
		print(f"Pedido {id} com status diferente de \"Pedido Pago\"")
		continue

	index = 0
	# Itera sobre cada item de um pedido, registrando este no arquivo.
	for i in range(n):
		prod, index = search(html, index, prod_ref)
		tam, index = search(html, index, tam_ref)
		qtd, index = search(html, index, qtd_ref)
		file.write(prod + "\t" + tam + "\t" + qtd + "\n")

file.close()

# Essa função pode ser usada para examinar o html como visto pelo programa.
"""
with open("teste_page.html", "w") as teste:
	id = 42
	teste.write(requests.get(f"https://app.lojaintegrada.com.br/painel/pedido/{id}/detalhar", cookies = cookies).content.decode("utf-8"))
"""
