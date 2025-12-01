import json

arquivo_json = 'data/vendas.json'

def calculo_comissao(valor):
    if valor >= 500:
        return valor * 0.05
    elif valor >= 100:
        return valor * 0.01
    else:
        return valor * 0.0

def calcular_comissao_total(dados_json):
    try:
        dados = json.loads(dados_json)
        vendas = dados.get('vendas', [])
    except json.JSONDecodeError:
        print("Erro: Falha ao decodificar o JSON.")
        return {}

    comissao_por_vendedor = {}

    for venda in vendas:
        vendedor = venda.get('vendedor')
        valor = venda.get('valor', 0.0)

        comissao = calculo_comissao(valor)

        if vendedor:
            if vendedor in comissao_por_vendedor:
                comissao_por_vendedor[vendedor]['total_vendas'] += valor
                comissao_por_vendedor[vendedor]['total_comissao'] += comissao
            else:
                comissao_por_vendedor[vendedor] = {
                    'total_vendas': valor,
                    'total_comissao': comissao
                }

    return comissao_por_vendedor

def exibir_resultados(resultados):
    print(f"{'VENDEDOR':<20} | {'TOTAL VENDAS':>15} | {'COMISSÃO TOTAL':>15}")
    print("=" * 55)

    
    for vendedor, dados in resultados.items():
        total_vendas = dados['total_vendas']
        total_comissao = dados['total_comissao']

        print(
            f"{vendedor:<20} | R${total_vendas:10.2f} | R${total_comissao:10.2f}"
        )

    print("=" * 55)

# Execução do Programa
if __name__ == "__main__":
    with open(arquivo_json, 'r') as file:
        dados_vendas_json = file.read()
    resultados = calcular_comissao_total(dados_vendas_json)
    exibir_resultados(resultados)